class ProductosMedios:
    def __init__(self, semilla1, semilla2):
        self.semilla1 = semilla1
        self.semilla2 = semilla2
        self.numeros_generados = []
    
    def generar(self, cantidad):
        # Validar que las semillas tengan 4 dígitos
        if self.semilla1 < 1000 or self.semilla1 > 9999 or self.semilla2 < 1000 or self.semilla2 > 9999:
            raise ValueError("Las semillas deben ser números de 4 dígitos")
        
        resultados = []
        valor_anterior = self.semilla1
        valor_actual = self.semilla2
        
        for _ in range(cantidad):
            # Multiplicar los dos valores
            producto = valor_anterior * valor_actual
            
            # Convertir a cadena y rellenar con ceros a la izquierda si es necesario
            producto_str = str(producto).zfill(8)
            
            # Extraer los 4 dígitos centrales
            if len(producto_str) > 4:
                medio = len(producto_str) // 2
                valor_anterior = valor_actual
                valor_actual = int(producto_str[medio-2:medio+2])
            else:
                valor_anterior = valor_actual
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