import numpy as np
import tkinter as tk
from tkinter import messagebox

# Función para crear entradas para la matriz
def crear_entradas_matriz():
    try:
        n = int(entrada_orden.get())
        if n <= 0:
            raise ValueError("El orden debe ser un número positivo")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
        return

    # Limpiar la ventana y crear entradas para la matriz
    for widget in frame_matriz.winfo_children():
        widget.destroy()

    global entradas
    entradas = []
    for i in range(n):
        fila = []
        for j in range(n):
            entrada = tk.Entry(frame_matriz, width=5)
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila.append(entrada)
        entradas.append(fila)

# Función para calcular el determinante
def calcular_determinante():
    try:
        n = int(entrada_orden.get())
        matriz = np.zeros((n, n))

        # Leer los valores de las entradas
        for i in range(n):
            for j in range(n):
                valor = float(entradas[i][j].get())
                matriz[i, j] = valor

        # Calcular el determinante
        determinante = np.linalg.det(matriz)
        messagebox.showinfo("Resultado", f"El determinante es: {determinante}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, asegúrate de que todos los valores sean números.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Determinantes")
ventana.geometry("400x400")

# Campo para ingresar el orden de la matriz
tk.Label(ventana, text="Ingresa el orden de la matriz:").pack(pady=10)
entrada_orden = tk.Entry(ventana)
entrada_orden.pack(pady=5)

# Botón para generar las entradas de la matriz
boton_generar = tk.Button(ventana, text="Generar matriz", command=crear_entradas_matriz)
boton_generar.pack(pady=10)

# Frame para colocar la matriz
frame_matriz = tk.Frame(ventana)
frame_matriz.pack()

# Botón para calcular el determinante
boton_calcular = tk.Button(ventana, text="Calcular determinante", command=calcular_determinante)
boton_calcular.pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()