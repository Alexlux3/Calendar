from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import config

class CalendarHandler:
    def __init__(self):
        self.service = self.obtener_servicio_calendar()
    
    def obtener_servicio_calendar(self):
        credentials = Credentials.from_service_account_file(config.CREDENTIALS_FILE, scopes=config.SCOPES)
        service = build('calendar', 'v3', credentials=credentials)
        return service
    
    def crear_evento(self, nombre, descripcion, inicio, fin):
        evento = {
            'summary': nombre,
            'description': descripcion,
            'start': {
                'dateTime': inicio,
                'timeZone': 'America/Mexico_City',
            },
            'end': {
                'dateTime': fin,
                'timeZone': 'America/Mexico_City',
            },
        }
        try:
            evento_resultado = self.service.events().insert(calendarId=config.CALENDAR_ID, body=evento).execute()
            print(f"Evento creado: {evento_resultado.get('htmlLink')}")
        except Exception as e:
            print(f"Error creando el evento en Google Calendar: {e}")
            raise
