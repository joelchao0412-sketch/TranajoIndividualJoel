import math
from scipy.stats import norm
class PruebaMedias:
    def __init__(self, numeros):
        self.numeros = numeros
        self.resultado = None
    
    def ejecutar(self, confianza=0.95):
        n = len(self.numeros)
        media = sum(self.numeros) / n if n > 0 else 0
        
        # Parámetros teóricos de U(0,1)
        media_teorica = 0.5
        varianza_teorica = 1/12
        
        # Error estándar de la media
        error_estandar = math.sqrt(varianza_teorica) / math.sqrt(n)
        
        # Valor crítico Z
        alfa = 1 - confianza
        z_critico = norm.ppf(1 - alfa/2)
        
        # Estadístico Z
        z_calc = (media - media_teorica) / error_estandar if error_estandar > 0 else 0
        
        # Límites de aceptación (como en el libro)
        LI = media_teorica - z_critico * (1 / math.sqrt(12*n))
        LS = media_teorica + z_critico * (1 / math.sqrt(12*n))
        
        # Verificación
        pasa = LI <= media <= LS
        
        self.resultado = {
            'media': media,
            'estadistico': z_calc,
            'z_critico': z_critico,
            'limite_inferior': LI,
            'limite_superior': LS,
            'pasa': pasa
        }
        
        return self.resultado
