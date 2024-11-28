from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError


class SheetsHandler:
    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.credentials = Credentials.from_service_account_file('calendario-442716-c265c5835810.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
        self.service = build('sheets', 'v4', credentials=self.credentials)

    def obtener_valores(self, rango):
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=rango).execute()
            return result.get('values', [])
        except HttpError as err:
            print(f"An error occurred: {err}")

    def guardar_eventos(self, eventos):
        values = []
        for celda, valor in eventos.items():
            row = {"range": celda, "values": [[valor]]}
            values.append(row)

        body = {"data": values, "valueInputOption": "RAW"}

        try:
            result = self.service.spreadsheets().values().batchUpdate(
                spreadsheetId=self.sheet_id, body=body).execute()
            print(f"Updated {result.get('totalUpdatedCells')} cells.")
        except HttpError as err:
            print(f"An error occurred: {err}")


    def reiniciar_eventos(self):
        rango = "Hoja 1!A2:G20"  # Ajusta el rango según tu hoja
        values = [["LIBRE"] * 5] * 20  # 20 filas y 5 columnas con "LIBRE"
        body = {
            'values': values
        }
        try:
            result = self.service.spreadsheets().values().update(
                spreadsheetId=self.sheet_id, range=rango, valueInputOption="RAW", body=body).execute()
            print(f"Reiniciado {result.get('updatedCells')} celdas.")
        except HttpError as err:
            print(f"An error occurred: {err}")
   

