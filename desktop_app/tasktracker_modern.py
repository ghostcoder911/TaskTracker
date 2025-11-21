#!/usr/bin/env python3
"""
Task Tracker Desktop Application - Modern Design
Beautiful GUI matching the web app
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font as tkfont
import json
import os
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials


class RoundedButton(tk.Canvas):
    """Custom rounded button widget"""
    def __init__(self, parent, text, command, bg_color="#764ba2", fg_color="white", 
                 width=200, height=50, font_size=14, **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, 
                          highlightthickness=0, bg=parent['bg'], **kwargs)
        self.command = command
        self.bg_color = bg_color
        self.hover_color = "#8b5fbf"
        self.fg_color = fg_color
        self.text = text
        self.font_size = font_size
        
        # Draw rounded rectangle
        self.rounded_rect = self.create_rounded_rectangle(0, 0, width, height, 
                                                          radius=10, fill=bg_color)
        self.text_obj = self.create_text(width//2, height//2, text=text, 
                                        fill=fg_color, font=("Arial", font_size, "bold"))
        
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.config(cursor="hand2")
    
    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                 x1+radius, y1,
                 x2-radius, y1,
                 x2-radius, y1,
                 x2, y1,
                 x2, y1+radius,
                 x2, y1+radius,
                 x2, y2-radius,
                 x2, y2-radius,
                 x2, y2,
                 x2-radius, y2,
                 x2-radius, y2,
                 x1+radius, y2,
                 x1+radius, y2,
                 x1, y2,
                 x1, y2-radius,
                 x1, y2-radius,
                 x1, y1+radius,
                 x1, y1+radius,
                 x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def _on_click(self, event):
        self.command()
    
    def _on_enter(self, event):
        self.itemconfig(self.rounded_rect, fill=self.hover_color)
    
    def _on_leave(self, event):
        self.itemconfig(self.rounded_rect, fill=self.bg_color)


class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Tracker - Team Check-ins")
        self.root.geometry("700x800")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.primary_color = "#667eea"
        self.secondary_color = "#764ba2"
        self.bg_light = "#f8f9fa"
        self.text_dark = "#2d3748"
        self.text_light = "#718096"
        self.border_color = "#e2e8f0"
        
        self.root.configure(bg=self.bg_light)
        
        # Data
        self.user_name = ""
        self.check_type = ""
        self.current_question = 0
        self.responses = {}
        
        # Questions
        self.morning_questions = [
            {"id": "energy_check", "question": "Energy Check: What's your energy drink or vibe this morning?", "label": "Energy Check"},
            {"id": "progress", "question": "Progress: What key tasks did you complete yesterday?", "label": "Yesterday's Progress"},
            {"id": "focus", "question": "Today's Focus: What are the top 1-3 priorities you're focusing on today?", "label": "Today's Priorities"},
            {"id": "blockers", "question": "Blockers: Anything slowing you down or you need help with?", "label": "Blockers"},
            {"id": "mood", "question": "State of Mind: One word for how you're feeling as you start the day?", "label": "State of Mind"}
        ]
        
        self.evening_questions = [
            {"id": "wins", "question": "Wins: What did you accomplish today (big or small)?", "label": "Today's Wins"},
            {"id": "learnings", "question": "Learnings: Anything new you learned or discovered?", "label": "Learnings"},
            {"id": "challenges", "question": "Stuck Points: Any challenges you faced today?", "label": "Challenges"},
            {"id": "tomorrow", "question": "Tomorrow Prep: What will be your focus tomorrow?", "label": "Tomorrow's Focus"},
            {"id": "mood_end", "question": "Mood Check: How are you ending the day?", "label": "Ending Mood"}
        ]
        
        self.questions = []
        
        # Initialize Google Sheets
        self.sheets_client = None
        self.spreadsheet = None
        self.init_google_sheets()
        
        # Show welcome screen
        self.show_welcome_screen()
    
    def init_google_sheets(self):
        """Initialize Google Sheets connection"""
        try:
            creds_file = os.path.join(os.path.dirname(__file__), 'credentials.json')
            config_file = os.path.join(os.path.dirname(__file__), 'config.json')
            
            if not os.path.exists(creds_file) or not os.path.exists(config_file):
                return
            
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            spreadsheet_id = config.get('spreadsheet_id')
            if not spreadsheet_id:
                return
            
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            
            credentials = Credentials.from_service_account_file(creds_file, scopes=scope)
            self.sheets_client = gspread.authorize(credentials)
            self.spreadsheet = self.sheets_client.open_by_key(spreadsheet_id)
            
        except Exception as e:
            print(f"Warning: Could not connect to Google Sheets: {e}")
    
    def create_gradient_frame(self, parent, height):
        """Create a gradient-like frame"""
        canvas = tk.Canvas(parent, height=height, highlightthickness=0)
        canvas.pack(fill='x')
        
        # Create gradient effect with rectangles
        steps = 50
        for i in range(steps):
            y = i * (height / steps)
            color = self._interpolate_color(self.primary_color, self.secondary_color, i/steps)
            canvas.create_rectangle(0, y, 1000, y + (height/steps) + 1, fill=color, outline=color)
        
        return canvas
    
    def _interpolate_color(self, color1, color2, fraction):
        """Interpolate between two colors"""
        c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
        c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
        
        r = int(c1[0] + (c2[0] - c1[0]) * fraction)
        g = int(c1[1] + (c2[1] - c1[1]) * fraction)
        b = int(c1[2] + (c2[2] - c1[2]) * fraction)
        
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def show_welcome_screen(self):
        """Display welcome screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Gradient header
        header_canvas = self.create_gradient_frame(self.root, 180)
        
        # Title
        header_canvas.create_text(350, 60, text="Task Tracker", 
                                 font=("Arial", 42, "bold"), fill="white")
        header_canvas.create_text(350, 110, text="Engineering Team Check-ins", 
                                 font=("Arial", 18), fill="white")
        
        # Main content
        content = tk.Frame(self.root, bg="white")
        content.pack(fill='both', expand=True, padx=50, pady=40)
        
        # Name label
        name_label = tk.Label(content, text="Your Name", font=("Arial", 14, "bold"),
                             bg="white", fg=self.text_dark)
        name_label.pack(anchor='w', pady=(20, 10))
        
        # Name entry with border
        entry_frame = tk.Frame(content, bg=self.border_color, padx=2, pady=2)
        entry_frame.pack(fill='x', pady=(0, 30))
        
        self.name_entry = tk.Entry(entry_frame, font=("Arial", 16), relief='flat',
                                   bg="white", fg=self.text_dark, borderwidth=0)
        self.name_entry.pack(fill='x', ipady=12, ipadx=15)
        self.name_entry.focus()
        
        # Check-in type label
        type_label = tk.Label(content, text="Check-in Type", font=("Arial", 14, "bold"),
                             bg="white", fg=self.text_dark)
        type_label.pack(anchor='w', pady=(10, 15))
        
        # Radio buttons
        self.check_type_var = tk.StringVar(value="morning")
        
        # Morning option
        morning_frame = tk.Frame(content, bg=self.bg_light, padx=20, pady=15)
        morning_frame.pack(fill='x', pady=8)
        
        tk.Radiobutton(morning_frame, text="Start of Day (Morning)",
                      variable=self.check_type_var, value="morning",
                      font=("Arial", 14), bg=self.bg_light, fg=self.text_dark,
                      activebackground=self.bg_light, selectcolor=self.primary_color,
                      cursor="hand2").pack(anchor='w')
        
        # Evening option
        evening_frame = tk.Frame(content, bg=self.bg_light, padx=20, pady=15)
        evening_frame.pack(fill='x', pady=8)
        
        tk.Radiobutton(evening_frame, text="End of Day (Evening)",
                      variable=self.check_type_var, value="evening",
                      font=("Arial", 14), bg=self.bg_light, fg=self.text_dark,
                      activebackground=self.bg_light, selectcolor=self.primary_color,
                      cursor="hand2").pack(anchor='w')
        
        # Start button
        btn_container = tk.Frame(content, bg="white")
        btn_container.pack(pady=40)
        
        start_btn = tk.Button(btn_container, text="Start Check-in →", 
                             font=("Arial", 16, "bold"),
                             bg=self.secondary_color, fg="white",
                             padx=50, pady=15,
                             relief='flat', borderwidth=0,
                             cursor="hand2",
                             command=self.start_checkin)
        start_btn.pack()
        
        # Footer
        footer = tk.Label(content, 
                         text="Keep it crisp and honest - this helps us support each other better!",
                         font=("Arial", 11), bg="white", fg=self.text_light,
                         wraplength=550)
        footer.pack(side='bottom', pady=20)
    
    def start_checkin(self):
        """Start the check-in process"""
        self.user_name = self.name_entry.get().strip()
        
        if not self.user_name:
            messagebox.showerror("Error", "Please enter your name!")
            return
        
        self.check_type = self.check_type_var.get()
        self.questions = self.morning_questions if self.check_type == "morning" else self.evening_questions
        self.current_question = 0
        self.responses = {}
        
        self.show_question_screen()
    
    def show_question_screen(self):
        """Display question screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_canvas = self.create_gradient_frame(self.root, 140)
        
        # Name and type
        header_canvas.create_text(350, 35, text=self.user_name, 
                                 font=("Arial", 24, "bold"), fill="white")
        
        type_text = "Morning Check-in" if self.check_type == "morning" else "Evening Check-out"
        header_canvas.create_text(350, 70, text=type_text, 
                                 font=("Arial", 16), fill="white")
        
        # Progress
        progress_text = f"Question {self.current_question + 1} of {len(self.questions)}"
        header_canvas.create_text(350, 100, text=progress_text, 
                                 font=("Arial", 13), fill="white")
        
        # Progress bar
        header_canvas.create_rectangle(50, 125, 650, 135, 
                                       fill="#9BA3C0", outline="")
        progress_width = 600 * ((self.current_question + 1) / len(self.questions))
        header_canvas.create_rectangle(50, 125, 50 + progress_width, 135, 
                                       fill="white", outline="")
        
        # Content
        content = tk.Frame(self.root, bg="white")
        content.pack(fill='both', expand=True, padx=40, pady=30)
        
        # Question
        question = self.questions[self.current_question]
        q_label = tk.Label(content, text=question['question'], 
                          font=("Arial", 16, "bold"),
                          bg="white", fg=self.text_dark, justify='left',
                          wraplength=600)
        q_label.pack(pady=(20, 20), anchor='w')
        
        # Answer label
        answer_label = tk.Label(content, text="Your answer:", 
                               font=("Arial", 13, "bold"),
                               bg="white", fg=self.text_light)
        answer_label.pack(anchor='w', pady=(10, 8))
        
        # Text area with border
        text_border = tk.Frame(content, bg=self.border_color, padx=2, pady=2)
        text_border.pack(fill='x', pady=(0, 20))
        
        self.answer_text = scrolledtext.ScrolledText(text_border, 
                                                     font=("Arial", 14),
                                                     wrap='word', relief='flat',
                                                     bg="white", fg=self.text_dark,
                                                     borderwidth=0,
                                                     height=10,
                                                     padx=15, pady=15)
        self.answer_text.pack(fill='x')
        self.answer_text.focus()
        
        # Buttons
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=25, fill='x')
        
        # Back button
        if self.current_question > 0:
            back_btn = tk.Button(btn_frame, text="← Back", 
                                font=("Arial", 15, "bold"),
                                bg="#6c757d", fg="white",
                                padx=30, pady=12,
                                relief='flat', borderwidth=0,
                                cursor="hand2",
                                command=self.prev_question)
            back_btn.pack(side='left')
        
        # Next button
        next_btn = tk.Button(btn_frame, text="Next →", 
                            font=("Arial", 15, "bold"),
                            bg=self.secondary_color, fg="white",
                            padx=40, pady=12,
                            relief='flat', borderwidth=0,
                            cursor="hand2",
                            command=self.next_question)
        next_btn.pack(side='right')
    
    def next_question(self):
        """Move to next question"""
        answer = self.answer_text.get("1.0", "end-1c").strip()
        
        if not answer:
            messagebox.showwarning("Warning", "Please enter an answer!")
            return
        
        question = self.questions[self.current_question]
        self.responses[question['id']] = {
            'label': question['label'],
            'answer': answer,
            'timestamp': datetime.now().isoformat()
        }
        
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question_screen()
        else:
            self.finish_checkin()
    
    def prev_question(self):
        """Go back to previous question"""
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question_screen()
            
            question = self.questions[self.current_question]
            if question['id'] in self.responses:
                self.answer_text.delete("1.0", "end")
                self.answer_text.insert("1.0", self.responses[question['id']]['answer'])
    
    def finish_checkin(self):
        """Complete the check-in and save data"""
        data = {
            'user_name': self.user_name,
            'check_type': self.check_type,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'timestamp': datetime.now().isoformat(),
            'responses': self.responses
        }
        
        sheets_success = False
        if self.spreadsheet:
            try:
                self.save_to_sheets(data)
                sheets_success = True
            except Exception as e:
                print(f"Error saving to Google Sheets: {e}")
        
        self.save_locally(data)
        self.show_completion_screen(sheets_success)
    
    def save_to_sheets(self, data):
        """Save data to Google Sheets"""
        sheet_name = data['date']
        
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
        except:
            worksheet = self.spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=20)
            headers = ['Timestamp', 'Name', 'Type']
            for response in data['responses'].values():
                headers.append(response['label'])
            worksheet.append_row(headers)
        
        row = [
            data['time'],
            data['user_name'],
            'Morning Check-in' if data['check_type'] == 'morning' else 'Evening Check-out'
        ]
        
        for response in data['responses'].values():
            row.append(response['answer'])
        
        worksheet.append_row(row)
    
    def save_locally(self, data):
        """Save data to local JSON file as backup"""
        backup_file = os.path.join(os.path.dirname(__file__), 'checkins_backup.json')
        
        if os.path.exists(backup_file):
            with open(backup_file, 'r') as f:
                all_data = json.load(f)
        else:
            all_data = []
        
        all_data.append(data)
        
        with open(backup_file, 'w') as f:
            json.dump(all_data, f, indent=2)
    
    def show_completion_screen(self, sheets_success):
        """Display completion screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_canvas = self.create_gradient_frame(self.root, 160)
        header_canvas.create_text(350, 80, text="All Done!", 
                                 font=("Arial", 36, "bold"), fill="white")
        
        # Content
        content = tk.Frame(self.root, bg="white")
        content.pack(fill='both', expand=True, padx=50, pady=40)
        
        # Success message
        if sheets_success:
            msg = "Your responses have been saved to Google Sheets!"
            msg_bg = "#d4edda"
            msg_fg = "#155724"
        else:
            msg = "Your responses have been saved locally!"
            msg_bg = "#fff3cd"
            msg_fg = "#856404"
        
        msg_frame = tk.Frame(content, bg=msg_bg, padx=30, pady=25)
        msg_frame.pack(fill='x', pady=30)
        
        msg_label = tk.Label(msg_frame, text=msg, font=("Arial", 16),
                            bg=msg_bg, fg=msg_fg)
        msg_label.pack()
        
        # Summary
        summary_label = tk.Label(content, text="Your responses have been recorded.",
                                font=("Arial", 14), bg="white", fg=self.text_light)
        summary_label.pack(pady=20)
        
        # Buttons
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=40)
        
        new_btn = tk.Button(btn_frame, text="New Check-in", 
                           font=("Arial", 15, "bold"),
                           bg=self.secondary_color, fg="white",
                           padx=35, pady=13,
                           relief='flat', borderwidth=0,
                           cursor="hand2",
                           command=self.show_welcome_screen)
        new_btn.pack(side='left', padx=10)
        
        exit_btn = tk.Button(btn_frame, text="Exit", 
                            font=("Arial", 15, "bold"),
                            bg="#6c757d", fg="white",
                            padx=30, pady=13,
                            relief='flat', borderwidth=0,
                            cursor="hand2",
                            command=self.root.quit)
        exit_btn.pack(side='left', padx=10)


def main():
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

