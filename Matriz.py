class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[None for _ in range(columnas)] for _ in range(filas)]  # Matriz vacía de n x m

    def set_elemento(self, fila, columna, valor):
        """Establece un valor en la posición (fila, columna) después de verificar que es un número."""
        try:
            valor = float(valor)  # Convertir el valor a número (aceptamos enteros o decimales)
            self.matriz[fila][columna] = valor
            return True  # Indica que la inserción fue exitosa
        except ValueError:
            return False  # Indica que la inserción falló debido a un valor no numérico

    def obtener_matriz(self):
        """Devuelve la matriz completa."""
        return self.matriz
