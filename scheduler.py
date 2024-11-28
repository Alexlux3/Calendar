import schedule
import time
import requests

def job():
    print("Reiniciando el horario...")
    response = requests.get("https://79713d6d-a447-4b72-87a5-861539cca9a8-00-2v26es4fb2nnt.kirk.replit.dev/reiniciar")
    print("Respuesta del servidor:", response.status_code)

schedule.every().sunday.at("00:00").do(job)  # Ajusta el tiempo según sea necesario

while True:
    schedule.run_pending()
    time.sleep(1)
