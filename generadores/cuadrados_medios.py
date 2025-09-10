class CuadradosMedios:
    def __init__(self, semilla):
        self.semilla = semilla
        self.numeros_generados = []
    
    def generar(self, cantidad):
        # Validar que la semilla tenga 4 dígitos
        if self.semilla < 1000 or self.semilla > 9999:
            raise ValueError("La semilla debe ser un número de 4 dígitos")
        
        resultados = []
        valor_actual = self.semilla
        
        for _ in range(cantidad):
            # Elevar al cuadrado
            cuadrado = valor_actual ** 2
            
            # Convertir a cadena y rellenar con ceros a la izquierda si es necesario
            cuadrado_str = str(cuadrado).zfill(8)
            
            # Extraer los 4 dígitos centrales
            if len(cuadrado_str) > 4:
                medio = len(cuadrado_str) // 2
                valor_actual = int(cuadrado_str[medio-2:medio+2])
            else:
                valor_actual = 0
            
            # Normalizar dividiendo entre 10000 para obtener números [0,1)
            resultado = valor_actual / 10000.0
            resultados.append(resultado)
            
            # Si llegamos a cero, todos los siguientes serán cero
            if valor_actual == 0:
                resultados.extend([0.0] * (cantidad - len(resultados)))
                break
        
        self.numeros_generados = resultados
        return resultados