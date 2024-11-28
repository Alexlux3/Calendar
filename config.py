from google.oauth2 import service_account
from googleapiclient.discovery import build
CREDENTIALS_FILE = r'calendario-442716-c265c5835810.json'  # Asegúrate de que este sea el nombre correcto y la ubicación del archivo
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/calendar']
SHEET_ID = '18G-fwLYH0nhdJdhc-34A6tJNCxfkkZ9WLsWUGvR6r00'  # Reemplaza con el ID de tu Google Sheet
CALENDAR_ID = 'y873b76ab70332b3b20ef5d11657984934ca157c029152d84a1778529c534e0d8@group.calendar.google.com'  # Reemplaza con el ID de tu Google Calendar