class ScheduleHandler:
    def __init__(self, dias, horas):
        self.dias = dias
        self.horas = horas

    def calcular_rango(self, dia, hora):
        """
        Calcula el rango en Google Sheets basado en el día y la hora.
        """
        if dia not in self.dias or hora not in self.horas:
            raise ValueError("El día o la hora no son válidos.")

        dia_index = self.dias.index(dia) + 2  # +2 para la columna en Sheets
        hora_index = self.horas.index(hora) + 2  # +2 para la fila en Sheets
        columna = chr(64 + dia_index)  # Convierte el índice a una letra (A, B, C...)
        rango = f"Hoja 1!{columna}{hora_index}"
        return rango

