import tkinter as tk
from tkinter import messagebox
from Matriz import Matriz
from calculadoraDeterminante import CalculadoraDeterminante

class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Matriz Cuadrada")
        
        # Mensaje de bienvenida
        self.label_bienvenida = tk.Label(self.root, text="¡Bienvenido! Por favor, ingrese el tamaño de su matriz cuadrada.")
        self.label_bienvenida.pack(pady=10)
        
        # Recordatorio sobre la matriz cuadrada
        self.label_recordatorio = tk.Label(
            self.root, text="Recuerda que la matriz debe ser cuadrada para poder calcular su determinante.")
        self.label_recordatorio.pack(pady=5)
        
        # Entrada para el tamaño de la matriz cuadrada (n x n)
        self.label_tamanio = tk.Label(self.root, text="Tamaño de la matriz (n):")
        self.label_tamanio.pack()
        self.entry_tamanio = tk.Entry(self.root)
        self.entry_tamanio.pack()
        
        # Botón para confirmar el tamaño de la matriz
        self.boton_confirmar = tk.Button(self.root, text="Confirmar", command=self.verificar_orden)
        self.boton_confirmar.pack(pady=10)

        # Contenedor para las entradas de la matriz
        self.matriz_entradas = None
        self.boton_calcular = None
        self.boton_mostrar_proceso = None
        
        self.root.mainloop()
    
    def verificar_orden(self):
        """Verifica que la entrada para n sea un número entero mayor a 0 y que la matriz sea cuadrada."""
        try:
            n = int(self.entry_tamanio.get())
            
            if n <= 0:
                raise ValueError("El tamaño de la matriz debe ser mayor a 0.")
            
            # Crear instancia de la clase Matriz
            self.matriz = Matriz(n, n)  # Matriz cuadrada de n x n
            self.mostrar_matriz(n, n)  # Llamada para crear la interfaz de la matriz
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero mayor a 0 para el tamaño de la matriz.")
    
    def mostrar_matriz(self, filas, columnas):
        """Muestra una matriz de entradas para que el usuario ingrese los valores."""
        # Si ya existe una matriz de entradas, la eliminamos
        if self.matriz_entradas:
            for widget in self.matriz_entradas.winfo_children():
                widget.destroy()
            self.matriz_entradas.destroy()
        
        # Crear un nuevo contenedor para las entradas de la matriz
        self.matriz_entradas = tk.Frame(self.root)
        self.matriz_entradas.pack(pady=10)
        
        # Crear una entrada por cada elemento de la matriz
        self.entradas = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                entrada = tk.Entry(self.matriz_entradas, width=5)
                entrada.grid(row=i, column=j)
                fila.append(entrada)
            self.entradas.append(fila)
        
        # Botón para validar la matriz
        self.boton_validar = tk.Button(self.root, text="Validar Matriz", command=self.validar_matriz)
        self.boton_validar.pack(pady=10)
        
        # Botón para calcular el determinante
        self.boton_calcular = tk.Button(self.root, text="Calcular determinante", command=self.calcular_determinante)
        self.boton_calcular.pack(pady=10)
    
    def validar_matriz(self):
        """Valida que todos los elementos ingresados sean números y los guarda en la clase Matriz."""
        for i, fila in enumerate(self.entradas):
            for j, entrada in enumerate(fila):
                valor = entrada.get()
                if not self.matriz.set_elemento(i, j, valor):
                    messagebox.showerror("Error", f"El valor en la posición ({i+1},{j+1}) no es un número válido.")
                    return  # Detiene la validación si hay un error
        
        # Si todo está correcto, muestra la matriz ingresada
        messagebox.showinfo("Éxito", "Matriz ingresada correctamente.")
    
    def calcular_determinante(self):
        """Calcula el determinante usando la clase CalculadoraDeterminante y muestra el resultado."""
        matriz_valores = self.matriz.obtener_matriz()
        self.calculadora = CalculadoraDeterminante(matriz_valores)
        determinante = self.calculadora.calcular_determinante()
        
        # Mostrar el resultado del determinante
        messagebox.showinfo("Determinante", f"El determinante de la matriz es: {determinante}")
        
        # Botón para mostrar el proceso
        if not self.boton_mostrar_proceso:
            self.boton_mostrar_proceso = tk.Button(self.root, text="Mostrar proceso", command=self.mostrar_proceso)
            self.boton_mostrar_proceso.pack(pady=10)

    def mostrar_proceso(self):
        """Muestra el proceso de cálculo del determinante en una nueva ventana."""
        ventana_proceso = tk.Toplevel(self.root)
        ventana_proceso.title("Proceso de Cálculo del Determinante")
        
        # Obtener el proceso del cálculo
        pasos = self.calculadora.obtener_proceso()
        
        # Mostrar cada paso en la nueva ventana
        texto_proceso = tk.Text(ventana_proceso, wrap=tk.WORD, width=60, height=20)
        texto_proceso.pack(padx=10, pady=10)
        for paso in pasos:
            texto_proceso.insert(tk.END, paso + "\n")
        texto_proceso.config(state=tk.DISABLED)  # Desactivar edición

# Instancia la clase Interfaz para iniciar la aplicación
Interfaz()