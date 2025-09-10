
from scipy.stats import chi2

class PruebaVarianza:
    def __init__(self, numeros):
        self.numeros = numeros
        self.resultado = None
    
    def ejecutar(self, confianza=0.95):
        # Calcular varianza muestral
        n = len(self.numeros)
        if n <= 1:
            varianza = 0
        else:
            media = sum(self.numeros) / n
            suma_cuadrados = sum((x - media) ** 2 for x in self.numeros)
            varianza = suma_cuadrados / (n - 1)
        
        # Varianza teórica de U(0,1)
        varianza_teorica = 1/12
        
        # Nivel de significancia
        alfa = 1 - confianza
        gl = n - 1
        
        # Valores críticos de Chi²
        chi2_inf = chi2.ppf(alfa/2, gl)
        chi2_sup = chi2.ppf(1 - alfa/2, gl)
        
        # Límites de aceptación de la varianza
        LI = chi2_inf / (12 * (n - 1))
        LS = chi2_sup / (12 * (n - 1))
        
        # Determinar si pasa
        pasa = LI <= varianza <= LS
        
        # Guardar resultados
        self.resultado = {
            'varianza': varianza,
            'LI': LI,
            'LS': LS,
            'var_teorica': varianza_teorica,
            'pasa': pasa
        }
        
        return self.resultado
