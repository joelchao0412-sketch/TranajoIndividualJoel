import math
from scipy.stats import chi2

class ChiCuadrado:
    def __init__(self, numeros):
        self.numeros = numeros
        self.resultado = None
    
    def ejecutar(self, confianza=0.95):
        n = len(self.numeros)
        k = 10  # número de intervalos
        
        # Calcular frecuencias observadas
        frecuencias_obs = [0] * k
        for num in self.numeros:
            indice = min(int(num * k), k-1)  # asignar intervalo
            frecuencias_obs[indice] += 1
        
        # Frecuencia esperada
        frecuencia_esp = n / k
        
        # Estadístico Chi-cuadrado
        chi2_calc = sum(((obs - frecuencia_esp) ** 2) / frecuencia_esp for obs in frecuencias_obs)
        
        # Valor crítico de tablas
        valor_critico = chi2.ppf(confianza, k-1)
        
        # Resultado de la prueba
        pasa = chi2_calc <= valor_critico
        
        self.resultado = {
            'estadistico': chi2_calc,
            'valor_critico': valor_critico,
            'pasa': pasa,
            'intervalos': k,
            'frecuencias_obs': frecuencias_obs
        }
        
        return self.resultado
