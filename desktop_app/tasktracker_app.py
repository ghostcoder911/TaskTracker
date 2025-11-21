#!/usr/bin/env python3
"""
Task Tracker Desktop Application
A standalone GUI app for team check-ins that saves to Google Sheets
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Tracker - Team Check-ins")
        self.root.geometry("650x750")
        self.root.resizable(False, False)
        
        # Modern color scheme matching web app
        self.bg_gradient_start = "#667eea"
        self.bg_gradient_end = "#764ba2"
        self.bg_color = "#667eea"
        self.fg_color = "white"
        self.button_color = "#764ba2"
        self.button_hover = "#8b5fbf"
        self.light_bg = "#f8f9fa"
        self.border_color = "#e0e0e0"
        
        # Configure root background
        self.root.configure(bg=self.light_bg)
        
        # Data
        self.user_name = ""
        self.check_type = ""
        self.current_question = 0
        self.responses = {}
        
        # Questions
        self.morning_questions = [
            {"id": "energy_check", "question": "0️⃣ Energy Check:\nWhat's your energy drink or vibe this morning?", "label": "Energy Check"},
            {"id": "progress", "question": "1️⃣ Progress:\nWhat key tasks did you complete yesterday?", "label": "Yesterday's Progress"},
            {"id": "focus", "question": "2️⃣ Today's Focus:\nWhat are the top 1-3 priorities you're focusing on today?", "label": "Today's Priorities"},
            {"id": "blockers", "question": "3️⃣ Blockers:\nAnything slowing you down or you need help with?", "label": "Blockers"},
            {"id": "mood", "question": "4️⃣ State of Mind:\nOne word for how you're feeling as you start the day?", "label": "State of Mind"}
        ]
        
        self.evening_questions = [
            {"id": "wins", "question": "1️⃣ Wins:\nWhat did you accomplish today (big or small)?", "label": "Today's Wins"},
            {"id": "learnings", "question": "2️⃣ Learnings:\nAnything new you learned or discovered?", "label": "Learnings"},
            {"id": "challenges", "question": "3️⃣ Stuck Points:\nAny challenges you faced today?", "label": "Challenges"},
            {"id": "tomorrow", "question": "4️⃣ Tomorrow Prep:\nWhat will be your focus tomorrow?", "label": "Tomorrow's Focus"},
            {"id": "mood_end", "question": "5️⃣ Mood Check:\nHow are you ending the day?", "label": "Ending Mood"}
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
            # Check for credentials file
            creds_file = os.path.join(os.path.dirname(__file__), 'credentials.json')
            if not os.path.exists(creds_file):
                print("Warning: credentials.json not found. Data will be saved locally only.")
                return
            
            # Load config for spreadsheet ID
            config_file = os.path.join(os.path.dirname(__file__), 'config.json')
            if not os.path.exists(config_file):
                print("Warning: config.json not found. Data will be saved locally only.")
                return
            
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            spreadsheet_id = config.get('spreadsheet_id')
            if not spreadsheet_id:
                print("Warning: spreadsheet_id not in config. Data will be saved locally only.")
                return
            
            # Setup credentials
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            
            credentials = Credentials.from_service_account_file(creds_file, scopes=scope)
            self.sheets_client = gspread.authorize(credentials)
            self.spreadsheet = self.sheets_client.open_by_key(spreadsheet_id)
            print("✓ Connected to Google Sheets")
            
        except Exception as e:
            print(f"Warning: Could not connect to Google Sheets: {e}")
            print("Data will be saved to local file instead.")
            # Show warning in GUI
            import tkinter.messagebox as mb
            mb.showwarning("Google Sheets", 
                          "Could not connect to Google Sheets.\n"
                          "Data will be saved locally only.\n\n"
                          "Check:\n"
                          "1. credentials.json is in the folder\n"
                          "2. config.json has correct spreadsheet_id\n"
                          "3. Spreadsheet is shared with service account")
    
    def show_welcome_screen(self):
        """Display welcome screen"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main container with gradient-like background
        main_container = tk.Frame(self.root, bg=self.light_bg)
        main_container.pack(fill='both', expand=True)
        
        # Header with rounded corners effect
        header = tk.Frame(main_container, bg=self.bg_color, height=150)
        header.pack(fill='x', padx=0, pady=0)
        header.pack_propagate(False)
        
        # Title with symbol
        title_frame = tk.Frame(header, bg=self.bg_color)
        title_frame.pack(pady=(35, 5))
        
        symbol_label = tk.Label(title_frame, text="✓", font=("Helvetica", 40, "bold"),
                               bg=self.bg_color, fg="white")
        symbol_label.pack(side='left', padx=(0, 10))
        
        title = tk.Label(title_frame, text="Task Tracker", font=("Helvetica", 38, "bold"),
                        bg=self.bg_color, fg=self.fg_color)
        title.pack(side='left')
        
        subtitle = tk.Label(header, text="Engineering Team Check-ins", font=("Helvetica", 16),
                           bg=self.bg_color, fg=self.fg_color)
        subtitle.pack(pady=(0, 25))
        
        # Content card with shadow effect
        content_outer = tk.Frame(main_container, bg=self.light_bg)
        content_outer.pack(fill='both', expand=True, padx=30, pady=30)
        
        content = tk.Frame(content_outer, bg="white", relief='flat', borderwidth=0)
        content.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Name input
        name_label = tk.Label(content, text="Your Name", font=("Helvetica", 13, "bold"),
                             bg="white", fg="#333")
        name_label.pack(pady=(30, 8), anchor='w', padx=40)
        
        # Styled entry with rounded appearance
        entry_frame = tk.Frame(content, bg="#e8e8e8", relief='flat')
        entry_frame.pack(padx=40, fill='x', pady=5)
        
        # Add padding for rounded effect
        inner_entry_frame = tk.Frame(entry_frame, bg="white")
        inner_entry_frame.pack(fill='both', padx=2, pady=2)
        
        self.name_entry = tk.Entry(inner_entry_frame, font=("Helvetica", 15), 
                                   relief='flat', borderwidth=0,
                                   highlightthickness=0, fg="#333",
                                   bg="white")
        self.name_entry.pack(fill='x', ipady=12, ipadx=15)
        self.name_entry.focus()
        
        # Check-in type
        type_label = tk.Label(content, text="Check-in Type", font=("Helvetica", 13, "bold"),
                             bg="white", fg="#333")
        type_label.pack(pady=(25, 15), anchor='w', padx=40)
        
        self.check_type_var = tk.StringVar(value="morning")
        
        # Radio button container
        radio_frame = tk.Frame(content, bg="white")
        radio_frame.pack(padx=40, fill='x')
        
        # Morning option with styled frame
        morning_outer = tk.Frame(radio_frame, bg="#d0d0d0", relief='flat')
        morning_outer.pack(fill='x', pady=6)
        
        morning_frame = tk.Frame(morning_outer, bg="#f5f5f5", relief='flat')
        morning_frame.pack(fill='both', padx=2, pady=2)
        
        morning_icon = tk.Label(morning_frame, text="☀", font=("Helvetica", 20),
                               bg="#f5f5f5", fg="#FFA500")
        morning_icon.pack(side='left', padx=(15, 10), pady=14)
        
        morning_radio = tk.Radiobutton(morning_frame, text="Start of Day",
                                      variable=self.check_type_var, value="morning",
                                      font=("Helvetica", 14, "bold"), bg="#f5f5f5",
                                      activebackground="#f5f5f5", fg="#333",
                                      selectcolor="#667eea", cursor="hand2")
        morning_radio.pack(side='left', pady=14)
        
        # Evening option with styled frame
        evening_outer = tk.Frame(radio_frame, bg="#d0d0d0", relief='flat')
        evening_outer.pack(fill='x', pady=6)
        
        evening_frame = tk.Frame(evening_outer, bg="#f5f5f5", relief='flat')
        evening_frame.pack(fill='both', padx=2, pady=2)
        
        evening_icon = tk.Label(evening_frame, text="☾", font=("Helvetica", 20),
                               bg="#f5f5f5", fg="#4A5568")
        evening_icon.pack(side='left', padx=(15, 10), pady=14)
        
        evening_radio = tk.Radiobutton(evening_frame, text="End of Day",
                                      variable=self.check_type_var, value="evening",
                                      font=("Helvetica", 14, "bold"), bg="#f5f5f5",
                                      activebackground="#f5f5f5", fg="#333",
                                      selectcolor="#667eea", cursor="hand2")
        evening_radio.pack(side='left', pady=14)
        
        # Start button with shadow effect
        btn_container = tk.Frame(content, bg="white")
        btn_container.pack(pady=40)
        
        # Shadow effect
        shadow_frame = tk.Frame(btn_container, bg="#9BA3C0")
        shadow_frame.pack()
        
        btn_frame = tk.Frame(shadow_frame, bg=self.button_color)
        btn_frame.pack(padx=3, pady=3)
        
        start_btn = tk.Button(btn_frame, text="Start Check-in →", 
                             font=("Helvetica", 15, "bold"),
                             bg=self.button_color, fg="white", 
                             padx=55, pady=16,
                             relief='flat', borderwidth=0,
                             command=self.start_checkin, cursor="hand2",
                             activebackground=self.button_hover)
        start_btn.pack()
        
        # Footer
        footer_frame = tk.Frame(content, bg=self.light_bg)
        footer_frame.pack(side='bottom', fill='x', pady=15)
        
        footer = tk.Label(footer_frame, 
                         text="Keep it crisp and honest — this helps us support each other better!",
                         font=("Helvetica", 11), bg=self.light_bg, fg="#666",
                         wraplength=520)
        footer.pack(pady=15)
    
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
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.light_bg)
        main_container.pack(fill='both', expand=True)
        
        # Header
        header = tk.Frame(main_container, bg=self.bg_color, height=130)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        name_label = tk.Label(header, text=self.user_name, font=("Helvetica", 20, "bold"),
                             bg=self.bg_color, fg=self.fg_color)
        name_label.pack(pady=(15, 5))
        
        type_text = "☀ Morning Check-in" if self.check_type == "morning" else "☾ Evening Check-out"
        type_label = tk.Label(header, text=type_text, font=("Helvetica", 14),
                             bg=self.bg_color, fg=self.fg_color)
        type_label.pack(pady=2)
        
        progress_text = f"Question {self.current_question + 1} of {len(self.questions)}"
        progress_label = tk.Label(header, text=progress_text, font=("Helvetica", 11),
                                 bg=self.bg_color, fg=self.fg_color)
        progress_label.pack(pady=(5, 10))
        
        # Progress bar
        progress_bar_container = tk.Frame(main_container, bg=self.border_color, height=6)
        progress_bar_container.pack(fill='x')
        progress_bar_container.pack_propagate(False)
        
        progress_percent = (self.current_question + 1) / len(self.questions)
        progress_bar = tk.Frame(progress_bar_container, bg=self.button_color)
        progress_bar.place(x=0, y=0, relwidth=progress_percent, relheight=1)
        
        # Content card
        content_outer = tk.Frame(main_container, bg=self.light_bg)
        content_outer.pack(fill='both', expand=True, padx=30, pady=30)
        
        content = tk.Frame(content_outer, bg="white")
        content.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Question
        question = self.questions[self.current_question]
        q_label = tk.Label(content, text=question['question'], font=("Helvetica", 15, "bold"),
                          bg="white", justify='left', wraplength=520, fg="#333")
        q_label.pack(pady=(30, 25), padx=30)
        
        # Answer input
        answer_label = tk.Label(content, text="Your answer:", font=("Helvetica", 12, "bold"),
                               bg="white", fg="#555")
        answer_label.pack(anchor='w', padx=30, pady=(10, 5))
        
        # Text area with rounded border effect
        text_outer = tk.Frame(content, bg="#d0d0d0", relief='flat')
        text_outer.pack(padx=30, fill='both', expand=True)
        
        text_frame = tk.Frame(text_outer, bg="white")
        text_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        self.answer_text = scrolledtext.ScrolledText(text_frame, font=("Helvetica", 13),
                                                     width=50, height=8, wrap='word',
                                                     relief='flat', borderwidth=0,
                                                     highlightthickness=0, fg="#333",
                                                     bg="white",
                                                     padx=15, pady=12)
        self.answer_text.pack(fill='both', expand=True)
        self.answer_text.focus()
        
        # Buttons with shadow
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=25, padx=30, fill='x')
        
        # Next button with shadow
        next_shadow = tk.Frame(btn_frame, bg="#9BA3C0")
        next_shadow.pack(side='right')
        
        next_inner = tk.Frame(next_shadow, bg=self.button_color)
        next_inner.pack(padx=2, pady=2)
        
        next_btn = tk.Button(next_inner, text="Next →", font=("Helvetica", 14, "bold"),
                            bg=self.button_color, fg="white", padx=40, pady=13,
                            relief='flat', borderwidth=0,
                            command=self.next_question, cursor="hand2",
                            activebackground=self.button_hover)
        next_btn.pack()
        
        if self.current_question > 0:
            # Back button with shadow
            back_shadow = tk.Frame(btn_frame, bg="#9BA3C0")
            back_shadow.pack(side='left')
            
            back_inner = tk.Frame(back_shadow, bg="#6c757d")
            back_inner.pack(padx=2, pady=2)
            
            back_btn = tk.Button(back_inner, text="← Back", font=("Helvetica", 14),
                                bg="#6c757d", fg="white", padx=35, pady=13,
                                relief='flat', borderwidth=0,
                                command=self.prev_question, cursor="hand2",
                                activebackground="#5a6268")
            back_btn.pack()
    
    def next_question(self):
        """Move to next question"""
        answer = self.answer_text.get("1.0", "end-1c").strip()
        
        if not answer:
            messagebox.showwarning("Warning", "Please enter an answer!")
            return
        
        # Save answer
        question = self.questions[self.current_question]
        self.responses[question['id']] = {
            'label': question['label'],
            'answer': answer,
            'timestamp': datetime.now().isoformat()
        }
        
        # Move to next question or finish
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
            
            # Restore previous answer if exists
            question = self.questions[self.current_question]
            if question['id'] in self.responses:
                self.answer_text.delete("1.0", "end")
                self.answer_text.insert("1.0", self.responses[question['id']]['answer'])
    
    def finish_checkin(self):
        """Complete the check-in and save data"""
        # Prepare data
        data = {
            'user_name': self.user_name,
            'check_type': self.check_type,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'timestamp': datetime.now().isoformat(),
            'responses': self.responses
        }
        
        # Try to save to Google Sheets
        sheets_success = False
        if self.spreadsheet:
            try:
                self.save_to_sheets(data)
                sheets_success = True
            except Exception as e:
                print(f"Error saving to Google Sheets: {e}")
        
        # Always save locally as backup
        self.save_locally(data)
        
        # Show completion screen
        self.show_completion_screen(sheets_success)
    
    def save_to_sheets(self, data):
        """Save data to Google Sheets"""
        sheet_name = data['date']
        
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
        except:
            # Create new worksheet for this date
            worksheet = self.spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=20)
            
            # Add headers
            headers = ['Timestamp', 'Name', 'Type']
            for response in data['responses'].values():
                headers.append(response['label'])
            worksheet.append_row(headers)
        
        # Prepare row data
        row = [
            data['time'],
            data['user_name'],
            '🌅 Morning Check-in' if data['check_type'] == 'morning' else '🌇 Evening Check-out'
        ]
        
        for response in data['responses'].values():
            row.append(response['answer'])
        
        # Append the row
        worksheet.append_row(row)
        print("✓ Data saved to Google Sheets")
    
    def save_locally(self, data):
        """Save data to local JSON file as backup"""
        backup_file = os.path.join(os.path.dirname(__file__), 'checkins_backup.json')
        
        # Load existing data
        if os.path.exists(backup_file):
            with open(backup_file, 'r') as f:
                all_data = json.load(f)
        else:
            all_data = []
        
        # Append new data
        all_data.append(data)
        
        # Save back to file
        with open(backup_file, 'w') as f:
            json.dump(all_data, f, indent=2)
        
        print(f"✓ Data saved locally to {backup_file}")
    
    def show_completion_screen(self, sheets_success):
        """Display completion screen"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header = tk.Frame(self.root, bg=self.bg_color, height=140)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Success icon
        success_icon = tk.Label(header, text="✓", font=("Helvetica", 50, "bold"),
                               bg=self.bg_color, fg="white")
        success_icon.pack(pady=(25, 5))
        
        title = tk.Label(header, text="All Done!", font=("Helvetica", 28, "bold"),
                        bg=self.bg_color, fg=self.fg_color)
        title.pack(pady=(0, 20))
        
        # Content frame
        content = tk.Frame(self.root, bg="white")
        content.pack(fill='both', expand=True, padx=40, pady=40)
        
        # Success message
        if sheets_success:
            msg = "Your responses have been saved to Google Sheets!"
            msg_icon = "✓"
            msg_color = "#28a745"
        else:
            msg = "Your responses have been saved locally!\n(Google Sheets connection not available)"
            msg_icon = "i"
            msg_color = "#ffc107"
        
        msg_frame = tk.Frame(content, bg="#e8f5e9" if sheets_success else "#fff8e1",
                            relief='flat')
        msg_frame.pack(pady=30, padx=40, fill='x')
        
        msg_inner = tk.Frame(msg_frame, bg="#e8f5e9" if sheets_success else "#fff8e1")
        msg_inner.pack(pady=20, padx=20)
        
        icon_label = tk.Label(msg_inner, text=msg_icon, font=("Helvetica", 30, "bold"),
                             bg="#e8f5e9" if sheets_success else "#fff8e1",
                             fg=msg_color)
        icon_label.pack()
        
        msg_label = tk.Label(msg_inner, text=msg, font=("Helvetica", 14),
                            bg="#e8f5e9" if sheets_success else "#fff8e1",
                            fg="#333", wraplength=450)
        msg_label.pack(pady=(10, 0))
        
        # Summary
        summary_frame = tk.Frame(content, bg="#f0f0f0", relief='solid', borderwidth=1)
        summary_frame.pack(pady=20, padx=20, fill='both')
        
        summary_title = tk.Label(summary_frame, text="Your Responses:",
                                font=("Arial", 12, "bold"), bg="#f0f0f0")
        summary_title.pack(pady=10)
        
        for response in self.responses.values():
            resp_text = f"{response['label']}: {response['answer'][:50]}..."
            resp_label = tk.Label(summary_frame, text=resp_text, font=("Arial", 10),
                                 bg="#f0f0f0", wraplength=400, justify='left')
            resp_label.pack(pady=2, padx=10, anchor='w')
        
        # Buttons with shadow
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=30)
        
        # New check-in button
        new_shadow = tk.Frame(btn_frame, bg="#9BA3C0")
        new_shadow.pack(side='left', padx=8)
        
        new_inner = tk.Frame(new_shadow, bg=self.button_color)
        new_inner.pack(padx=2, pady=2)
        
        new_btn = tk.Button(new_inner, text="New Check-in", font=("Helvetica", 13, "bold"),
                           bg=self.button_color, fg="white", padx=30, pady=12,
                           relief='flat', borderwidth=0,
                           command=self.show_welcome_screen, cursor="hand2",
                           activebackground=self.button_hover)
        new_btn.pack()
        
        # Exit button
        exit_shadow = tk.Frame(btn_frame, bg="#9BA3C0")
        exit_shadow.pack(side='left', padx=8)
        
        exit_inner = tk.Frame(exit_shadow, bg="#6c757d")
        exit_inner.pack(padx=2, pady=2)
        
        exit_btn = tk.Button(exit_inner, text="Exit", font=("Helvetica", 13),
                            bg="#6c757d", fg="white", padx=30, pady=12,
                            relief='flat', borderwidth=0,
                            command=self.root.quit, cursor="hand2",
                            activebackground="#5a6268")
        exit_btn.pack()


def main():
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

