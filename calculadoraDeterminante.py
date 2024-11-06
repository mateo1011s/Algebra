class CalculadoraDeterminante:
    def __init__(self, matriz):
        self.matriz = matriz
        self.proceso = []  # Lista para almacenar el proceso paso a paso

    def calcular_determinante(self):
        """Calcula el determinante de la matriz y guarda el proceso paso a paso."""
        self.proceso.clear()  # Limpiamos el proceso para un cálculo nuevo
        determinante = self._determinante_cofactores(self.matriz)
        return determinante

    def _determinante_cofactores(self, matriz, nivel=0):
        """Método recursivo para calcular el determinante usando cofactores y registrar el proceso."""
        # Caso base: matriz de 1x1
        if len(matriz) == 1:
            return matriz[0][0]
        
        # Caso base: matriz de 2x2
        if len(matriz) == 2:
            det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
            self.proceso.append(f"{'  '*nivel}Determinante de 2x2: ({matriz[0][0]}*{matriz[1][1]}) - ({matriz[0][1]}*{matriz[1][0]}) = {det}")
            return det
        
        # Expansión por cofactores
        determinante = 0
        for columna in range(len(matriz)):
            # Submatriz excluyendo la primera fila y la columna actual
            submatriz = [fila[:columna] + fila[columna+1:] for fila in matriz[1:]]
            signo = (-1) ** columna
            cofactor = signo * matriz[0][columna]
            det_submatriz = self._determinante_cofactores(submatriz, nivel + 1)
            term = cofactor * det_submatriz
            determinante += term
            self.proceso.append(
                f"{'  '*nivel}Cofactor({0},{columna}) = {signo} * {matriz[0][columna]} * Determinante(submatriz) = {term}")
        
        self.proceso.append(f"{'  '*nivel}Determinante parcial en nivel {nivel}: {determinante}")
        return determinante

    def obtener_proceso(self):
        """Devuelve el proceso de cálculo como una lista de pasos."""
        return self.proceso
