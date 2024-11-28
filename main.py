from flask import Flask, render_template, request, redirect, url_for
from sheets_handler import SheetsHandler
from schedule_handler import ScheduleHandler
from config import SHEET_ID

main = Flask(__name__)

# Instancias de clases
sheets = SheetsHandler(SHEET_ID)
schedule = ScheduleHandler(
    dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    horas=["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20"]
)

@app.route("/")
def index():
    rango = "Hoja 1!A1:G20"  # Ajusta el rango según tu hoja
    datos_crudos = sheets.obtener_valores(rango)

    # Normaliza los datos (elimina espacios y asegura que "LIBRE" esté consistente)
    datos = []
    for fila in datos_crudos:
        datos.append([celda.strip() if celda else "LIBRE" for celda in fila])

    return render_template("index.html", datos=datos, schedule=schedule, chr=chr, enumerate=enumerate, len=len)

@app.route("/agregar_evento", methods=["POST"])
def agregar_evento():
    dia = request.form.get("dia")
    hora = request.form.get("hora")
    grupo = request.form.get("grupo")
    responsable = request.form.get("responsable")

    if not (dia and hora and grupo and responsable):
        return "Datos incompletos", 400

    # Determinar el rango de la celda
    rango = schedule.calcular_rango(dia, hora)

    # Obtener los datos actuales de la celda
    celda_actual = sheets.obtener_valores(rango)
    eventos = celda_actual[0][0].split("|") if celda_actual and celda_actual[0][0] != "LIBRE" else []

    if len(eventos) >= 4:
        return "La celda ya está llena", 400

    # Agregar el nuevo evento
    eventos.append(f"Grupo {grupo}: {responsable}")
    nuevo_valor = " | ".join(eventos)
    sheets.guardar_eventos({rango: nuevo_valor})

    # Redirige al índice para evitar reenvío del POST
    return redirect(url_for("index"))

@app.route('/eliminar_evento', methods=['POST'])
def eliminar_evento():
    # Obtener parámetros del formulario
    dia = request.form.get('dia')
    hora = request.form.get('hora')
    evento = request.form.get('evento')

    if not (dia and hora and evento):
        return "Datos incompletos", 400

    # Determinar el rango de la celda
    rango = schedule.calcular_rango(dia, hora)
    print(f"Rango calculado: {rango}")

    # Obtener los datos actuales de la celda
    celda_actual = sheets.obtener_valores(rango)
    print(f"Datos actuales en celda: {celda_actual}")

    eventos = celda_actual[0][0].split("|") if celda_actual and celda_actual[0][0] != "LIBRE" else []

    # Limpieza de espacios innecesarios
    eventos = [e.strip() for e in eventos]  # Elimina espacios al inicio y al final de cada evento
    print(f"Eventos después de limpiar: {eventos}")

    # Intentar eliminar el evento seleccionado
    if evento in eventos:
        eventos.remove(evento)
        nuevo_valor = " | ".join(eventos) if eventos else "LIBRE"
        sheets.guardar_eventos({rango: nuevo_valor})
        print(f"Evento eliminado: {evento}")
    else:
        print(f"El evento '{evento}' no se encontró en la lista de eventos.")

    # Redirige al índice para evitar reenvío del POST
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
