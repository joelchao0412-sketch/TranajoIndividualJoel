class MultiplicadorConstante:
    def __init__(self, semilla, constante):
        self.semilla = semilla
        self.constante = constante
        self.numeros_generados = []
    
    def generar(self, cantidad):
        # Validar que la semilla y la constante tengan 4 dígitos
        if self.semilla < 1000 or self.semilla > 9999 or self.constante < 1000 or self.constante > 9999:
            raise ValueError("La semilla y la constante deben ser números de 4 dígitos")
        
        resultados = []
        valor_actual = self.semilla
        
        for _ in range(cantidad):
            # Multiplicar por la constante
            producto = valor_actual * self.constante
            
            # Convertir a cadena y rellenar con ceros a la izquierda si es necesario
            producto_str = str(producto).zfill(8)
            
            # Extraer los 4 dígitos centrales
            if len(producto_str) > 4:
                medio = len(producto_str) // 2
                valor_actual = int(producto_str[medio-2:medio+2])
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