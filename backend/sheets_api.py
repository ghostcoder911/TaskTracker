import os
import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

class SheetsAPI:
    def __init__(self):
        self.client = None
        self.spreadsheet = None
        self.fallback_file = 'fallback_data.json'
        
        # Try to initialize Google Sheets connection
        try:
            self._initialize_sheets()
        except Exception as e:
            print(f"Warning: Could not initialize Google Sheets: {e}")
            print("Will use local fallback storage")
    
    def _initialize_sheets(self):
        """Initialize connection to Google Sheets"""
        # Check if credentials are available
        creds_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
        spreadsheet_id = os.environ.get('SPREADSHEET_ID')
        
        if not creds_json or not spreadsheet_id:
            raise Exception("Google Sheets credentials not configured")
        
        # Parse credentials
        creds_dict = json.loads(creds_json)
        
        # Define the scope
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Create credentials
        credentials = Credentials.from_service_account_info(creds_dict, scopes=scope)
        
        # Authorize the client
        self.client = gspread.authorize(credentials)
        
        # Open the spreadsheet
        self.spreadsheet = self.client.open_by_key(spreadsheet_id)
    
    def save_checkin(self, user_name, check_type, responses):
        """Save check-in data to Google Sheets or fallback storage"""
        data = {
            'user_name': user_name,
            'check_type': check_type,
            'timestamp': datetime.now().isoformat(),
            **responses
        }
        
        if self.spreadsheet:
            try:
                self._save_to_sheets(data)
                return True
            except Exception as e:
                print(f"Error saving to Google Sheets: {e}")
                self._save_to_fallback(data)
                return False
        else:
            self._save_to_fallback(data)
            return False
    
    def _save_to_sheets(self, data):
        """Save data to Google Sheets"""
        sheet_name = data['date']
        
        try:
            # Try to get existing worksheet
            worksheet = self.spreadsheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
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
            '🌅 Morning Check-in' if data['check_type'] == 'start' else '🌇 Evening Check-out'
        ]
        
        for response in data['responses'].values():
            row.append(response['answer'])
        
        # Append the row
        worksheet.append_row(row)
    
    def _save_to_fallback(self, data):
        """Save data to local JSON file as fallback"""
        # Load existing data
        if os.path.exists(self.fallback_file):
            with open(self.fallback_file, 'r') as f:
                all_data = json.load(f)
        else:
            all_data = []
        
        # Append new data
        all_data.append(data)
        
        # Save back to file
        with open(self.fallback_file, 'w') as f:
            json.dump(all_data, f, indent=2)
        
        print(f"Data saved to fallback file: {self.fallback_file}")

