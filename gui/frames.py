import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importamos las clases de generadores y pruebas
from generadores.cuadrados_medios import CuadradosMedios
from generadores.productos_medios import ProductosMedios
from generadores.multiplicador_constante import MultiplicadorConstante
from pruebas.chi_cuadrado import ChiCuadrado
from pruebas.prueba_medias import PruebaMedias
from pruebas.prueba_varianza import PruebaVarianza

class FrameCuadradosMedios(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        # Título
        tk.Label(self, text="Generador de Cuadrados Medios", 
                font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        
        # Contenido específico del generador
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Campos de entrada
        tk.Label(frame_contenido, text="Semilla inicial (4 dígitos):", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.semilla_entry = tk.Entry(frame_contenido)
        self.semilla_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        tk.Label(frame_contenido, text="Cantidad de números:", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.cantidad_entry = tk.Entry(frame_contenido)
        self.cantidad_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
        # Botón generar
        self.generar_btn = tk.Button(frame_contenido, text="Generar", command=self.generar_numeros)
        self.generar_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.resultado_text = tk.Text(frame_contenido, height=10, width=50)
        self.resultado_text.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Configurar expansión
        frame_contenido.grid_columnconfigure(1, weight=1)
        frame_contenido.grid_rowconfigure(3, weight=1)
    
    def generar_numeros(self):
        # Obtener valores de entrada
        semilla = self.semilla_entry.get()
        cantidad = self.cantidad_entry.get()
        
        # Validar entradas
        if not semilla or not cantidad:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            semilla = int(semilla)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
            return
        
        # Validar que la semilla tenga 4 dígitos
        if semilla < 1000 or semilla > 9999:
            messagebox.showerror("Error", "La semilla debe ser un número de 4 dígitos")
            return
        
        # Crear generador y generar números
        generador = CuadradosMedios(semilla)
        numeros = generador.generar(cantidad)
        
        # Mostrar resultados
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, "Números generados:\n\n")
        for i, num in enumerate(numeros):
            self.resultado_text.insert(tk.END, f"{i+1}. {num}\n")

class FrameProductosMedios(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        # Título
        tk.Label(self, text="Generador de Productos Medios", 
                font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        
        # Contenido específico del generador
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Campos de entrada
        tk.Label(frame_contenido, text="Semilla 1 (4 dígitos):", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.semilla1_entry = tk.Entry(frame_contenido)
        self.semilla1_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        tk.Label(frame_contenido, text="Semilla 2 (4 dígitos):", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.semilla2_entry = tk.Entry(frame_contenido)
        self.semilla2_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
        tk.Label(frame_contenido, text="Cantidad de números:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.cantidad_entry = tk.Entry(frame_contenido)
        self.cantidad_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        
        # Botón generar
        self.generar_btn = tk.Button(frame_contenido, text="Generar", command=self.generar_numeros)
        self.generar_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.resultado_text = tk.Text(frame_contenido, height=10, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Configurar expansión
        frame_contenido.grid_columnconfigure(1, weight=1)
        frame_contenido.grid_rowconfigure(4, weight=1)
    
    def generar_numeros(self):
        # Obtener valores de entrada
        semilla1 = self.semilla1_entry.get()
        semilla2 = self.semilla2_entry.get()
        cantidad = self.cantidad_entry.get()
        
        # Validar entradas
        if not semilla1 or not semilla2 or not cantidad:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            semilla1 = int(semilla1)
            semilla2 = int(semilla2)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
            return
        
        # Validar que las semillas tengan 4 dígitos
        if semilla1 < 1000 or semilla1 > 9999 or semilla2 < 1000 or semilla2 > 9999:
            messagebox.showerror("Error", "Las semillas deben ser números de 4 dígitos")
            return
        
        # Crear generador y generar números
        generador = ProductosMedios(semilla1, semilla2)
        numeros = generador.generar(cantidad)
        
        # Mostrar resultados
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, "Números generados:\n\n")
        for i, num in enumerate(numeros):
            self.resultado_text.insert(tk.END, f"{i+1}. {num}\n")

class FrameMultiplicadorConstante(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        # Título
        tk.Label(self, text="Generador de Multiplicador Constante", 
                font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        
        # Contenido específico del generador
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Campos de entrada
        tk.Label(frame_contenido, text="Semilla inicial (4 dígitos):", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.semilla_entry = tk.Entry(frame_contenido)
        self.semilla_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        tk.Label(frame_contenido, text="Constante multiplicadora (4 dígitos):", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.constante_entry = tk.Entry(frame_contenido)
        self.constante_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
        tk.Label(frame_contenido, text="Cantidad de números:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.cantidad_entry = tk.Entry(frame_contenido)
        self.cantidad_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        
        # Botón generar
        self.generar_btn = tk.Button(frame_contenido, text="Generar", command=self.generar_numeros)
        self.generar_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.resultado_text = tk.Text(frame_contenido, height=10, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Configurar expansión
        frame_contenido.grid_columnconfigure(1, weight=1)
        frame_contenido.grid_rowconfigure(4, weight=1)
    
    def generar_numeros(self):
        # Obtener valores de entrada
        semilla = self.semilla_entry.get()
        constante = self.constante_entry.get()
        cantidad = self.cantidad_entry.get()
        
        # Validar entradas
        if not semilla or not constante or not cantidad:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            semilla = int(semilla)
            constante = int(constante)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
            return
        
        # Validar que la semilla y la constante tengan 4 dígitos
        if semilla < 1000 or semilla > 9999 or constante < 1000 or constante > 9999:
            messagebox.showerror("Error", "La semilla y la constante deben ser números de 4 dígitos")
            return
        
        # Crear generador y generar números
        generador = MultiplicadorConstante(semilla, constante)
        numeros = generador.generar(cantidad)
        
        # Mostrar resultados
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, "Números generados:\n\n")
        for i, num in enumerate(numeros):
            self.resultado_text.insert(tk.END, f"{i+1}. {num}\n")

class FrameChiCuadrado(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        self.numeros = []  # guardamos los números ingresados
        self.intervalos = 10  # número de intervalos por defecto
        
        tk.Label(self, text="Prueba de Uniformidad Chi Cuadrado", 
                 font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Entrada de números
        tk.Label(frame_contenido, text="Números (0 a 1) separados por comas:", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.numeros_entry = tk.Text(frame_contenido, height=5, width=40)
        self.numeros_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Nivel de confianza
        tk.Label(frame_contenido, text="Nivel de confianza (ej: 0.95):", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.confianza_entry = tk.Entry(frame_contenido)
        self.confianza_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        
        # Botón ejecutar
        self.ejecutar_btn = tk.Button(frame_contenido, text="Ejecutar Prueba", command=self.ejecutar_prueba)
        self.ejecutar_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Botón mostrar gráfico
        self.grafico_btn = tk.Button(frame_contenido, text="Mostrar Gráfico", command=self.mostrar_ventana_grafico)
        self.grafico_btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.resultado_text = tk.Text(frame_contenido, height=15, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        
        frame_contenido.grid_columnconfigure(0, weight=1)
        frame_contenido.grid_rowconfigure(4, weight=1)
    
    def ejecutar_prueba(self):
        numeros_str = self.numeros_entry.get("1.0", tk.END).strip()
        confianza_str = self.confianza_entry.get()
        
        if not numeros_str or not confianza_str:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            confianza = float(confianza_str)
            if confianza <= 0 or confianza >= 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El nivel de confianza debe ser un número entre 0 y 1")
            return
        
        try:
            self.numeros = [float(num.strip()) for num in numeros_str.split(",")]
        except ValueError:
            messagebox.showerror("Error", "Los números deben ser valores numéricos separados por comas")
            return
        
        # Ejecutar prueba chi-cuadrado
        prueba = ChiCuadrado(self.numeros)
        resultado = prueba.ejecutar(confianza)
        self.intervalos = resultado['intervalos']
        
        # Mostrar resultados
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, f"Estadístico Chi-cuadrado: {resultado['estadistico']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Valor crítico: {resultado['valor_critico']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Resultado: {'Pasa la prueba' if resultado['pasa'] else 'No pasa la prueba'}\n\n")
        
        self.mostrar_histograma_textual()
    
    def mostrar_histograma_textual(self):
        frecuencias = [0] * self.intervalos
        for num in self.numeros:
            indice = min(int(num * self.intervalos), self.intervalos - 1)
            frecuencias[indice] += 1
        
        ancho_intervalo = 1.0 / self.intervalos
        max_frecuencia = max(frecuencias) if frecuencias else 1
        
        self.resultado_text.insert(tk.END, "Histograma de Frecuencias (Texto):\n\n")
        for i in range(self.intervalos):
            limite_inferior = i * ancho_intervalo
            limite_superior = (i + 1) * ancho_intervalo
            intervalo_str = f"[{limite_inferior:.2f}, {limite_superior:.2f})"
            longitud_barra = int(40 * frecuencias[i] / max_frecuencia) if max_frecuencia > 0 else 0
            barra = "█" * longitud_barra
            self.resultado_text.insert(tk.END, f"{intervalo_str}: {frecuencias[i]} {barra}\n")
        
        self.resultado_text.insert(tk.END, f"\nTotal de números: {len(self.numeros)}\n")
        self.resultado_text.insert(tk.END, f"Número de intervalos: {self.intervalos}\n")
        self.resultado_text.insert(tk.END, f"Frecuencia esperada por intervalo: {len(self.numeros)/self.intervalos:.2f}\n")
    
    def mostrar_ventana_grafico(self):
        if not self.numeros:
            messagebox.showwarning("Aviso", "Primero ejecuta la prueba para generar los datos")
            return
        
        # Crear ventana nueva
        ventana_grafico = tk.Toplevel(self)
        ventana_grafico.title("Histograma de Frecuencias")
        
        frecuencias = [0] * self.intervalos
        for num in self.numeros:
            indice = min(int(num * self.intervalos), self.intervalos - 1)
            frecuencias[indice] += 1
        
        ancho_intervalo = 1.0 / self.intervalos
        limites = [i * ancho_intervalo for i in range(self.intervalos+1)]
        
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar(range(self.intervalos), frecuencias, width=0.9, color='skyblue', edgecolor='black')
        ax.set_xticks(range(self.intervalos))
        ax.set_xticklabels([f"{limites[i]:.2f}-{limites[i+1]:.2f}" for i in range(self.intervalos)], rotation=45)
        ax.set_xlabel("Intervalos")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Histograma de Frecuencias")
        
        canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

class FramePruebaMedias(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        # Título
        tk.Label(self, text="Prueba de Medias", 
                 font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        
        # Contenido específico de la prueba
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Campo para ingresar los números (separados por comas)
        tk.Label(frame_contenido, text="Números (separados por comas):", 
                 bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.numeros_entry = tk.Text(frame_contenido, height=5, width=40)
        self.numeros_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Campo para el nivel de confianza
        tk.Label(frame_contenido, text="Nivel de confianza (ej: 0.95):", 
                 bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.confianza_entry = tk.Entry(frame_contenido)
        self.confianza_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        
        # Botón ejecutar prueba
        self.ejecutar_btn = tk.Button(frame_contenido, text="Ejecutar Prueba", 
                                      command=self.ejecutar_prueba)
        self.ejecutar_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.resultado_text = tk.Text(frame_contenido, height=10, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Botón para mostrar gráfico
        self.grafico_btn = tk.Button(frame_contenido, text="Mostrar Gráfico", 
                                     command=self.mostrar_grafico)
        self.grafico_btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Configurar expansión
        frame_contenido.grid_columnconfigure(0, weight=1)
        frame_contenido.grid_rowconfigure(4, weight=1)

        # Guardar resultado
        self.ultimo_resultado = None
    
    def ejecutar_prueba(self):
        # Obtener valores de entrada
        numeros_str = self.numeros_entry.get("1.0", tk.END).strip()
        confianza_str = self.confianza_entry.get()
        
        # Validar entradas
        if not numeros_str or not confianza_str:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            confianza = float(confianza_str)
            if confianza <= 0 or confianza >= 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El nivel de confianza debe ser un número entre 0 y 1")
            return
        
        # Convertir string de números a lista de floats
        try:
            numeros = [float(num.strip()) for num in numeros_str.split(",")]
        except ValueError:
            messagebox.showerror("Error", "Los números deben ser valores numéricos separados por comas")
            return
        
        # Crear prueba y ejecutar
        prueba = PruebaMedias(numeros)
        resultado = prueba.ejecutar(confianza)
        self.ultimo_resultado = resultado
        
        # Mostrar resultados
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, f"Media muestral: {resultado['media']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Estadístico Z: {resultado['estadistico']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Z crítico: ±{resultado['z_critico']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Límite inferior: {resultado['limite_inferior']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Límite superior: {resultado['limite_superior']:.4f}\n")
        self.resultado_text.insert(tk.END, f"Resultado: {'✅ Pasa la prueba' if resultado['pasa'] else '❌ No pasa la prueba'}\n")
    
    def mostrar_grafico(self):
        if not self.ultimo_resultado:
            messagebox.showerror("Error", "Primero ejecuta la prueba")
            return
        
        res = self.ultimo_resultado
        LI, LS, media = res['limite_inferior'], res['limite_superior'], res['media']
        
        # Gráfico simple
        plt.figure(figsize=(6,3))
        plt.axhline(0, color="black")
        plt.plot([LI, LS], [0,0], color="blue", linewidth=4, label="Intervalo de aceptación")
        plt.scatter(media, 0, color="red", zorder=5, label="Media muestral")
        plt.title("Prueba de Medias - Intervalo de Aceptación")
        plt.xlabel("Valores")
        plt.yticks([])
        plt.legend()
        plt.show()

class FramePruebaVarianza(tk.Frame):     
    def __init__(self, parent, controller=None):         
        super().__init__(parent)         
        self.controller = controller         
        self.config(bg="white")         

        self.numeros = []      # Guardar los números ingresados
        self.resultado = None  # Guardar el resultado de la prueba

        # Título         
        tk.Label(self, text="Prueba de Varianza",                 
                 font=("Arial", 16, "bold"), bg="white").pack(pady=20)         

        frame_contenido = tk.Frame(self, bg="white")         
        frame_contenido.pack(pady=10, padx=20, fill="both", expand=True)         

        # Entrada de números         
        tk.Label(frame_contenido, text="Números (separados por comas):", bg="white").grid(row=0, column=0, sticky="w", pady=5)         
        self.numeros_entry = tk.Text(frame_contenido, height=5, width=40)         
        self.numeros_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")         

        # Nivel de confianza         
        tk.Label(frame_contenido, text="Nivel de confianza (ej: 0.95):", bg="white").grid(row=2, column=0, sticky="w", pady=5)         
        self.confianza_entry = tk.Entry(frame_contenido)         
        self.confianza_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")         

        # Botón ejecutar prueba         
        self.ejecutar_btn = tk.Button(frame_contenido, text="Ejecutar Prueba", command=self.ejecutar_prueba)         
        self.ejecutar_btn.grid(row=3, column=0, columnspan=2, pady=10)         

        # Botón para mostrar gráfico en ventana aparte
        self.grafico_btn = tk.Button(frame_contenido, text="Mostrar Gráfico", command=self.mostrar_grafico_ventana)
        self.grafico_btn.grid(row=5, column=0, columnspan=2, pady=10)

        # Área de resultados         
        self.resultado_text = tk.Text(frame_contenido, height=10, width=50)         
        self.resultado_text.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")         

        # Configurar expansión         
        frame_contenido.grid_columnconfigure(0, weight=1)         
        frame_contenido.grid_rowconfigure(4, weight=1)     

    def ejecutar_prueba(self):         
        numeros_str = self.numeros_entry.get("1.0", tk.END).strip()         
        confianza_str = self.confianza_entry.get()         

        if not numeros_str or not confianza_str:             
            messagebox.showerror("Error", "Por favor completa todos los campos")             
            return         

        try:             
            confianza = float(confianza_str)             
            if confianza <= 0 or confianza >= 1:                 
                raise ValueError         
        except ValueError:             
            messagebox.showerror("Error", "El nivel de confianza debe ser un número entre 0 y 1")             
            return         

        try:             
            self.numeros = [float(num.strip()) for num in numeros_str.split(",")]         
        except ValueError:             
            messagebox.showerror("Error", "Los números deben ser valores numéricos separados por comas")             
            return         

        # Crear prueba y ejecutar         
        prueba = PruebaVarianza(self.numeros)         
        self.resultado = prueba.ejecutar(confianza)         

        # Mostrar resultados         
        self.resultado_text.delete(1.0, tk.END)         
        self.resultado_text.insert(tk.END, f"Varianza muestral: {self.resultado['varianza']:.6f}\n")         
        self.resultado_text.insert(tk.END, f"Límite inferior: {self.resultado['LI']:.6f}\n")         
        self.resultado_text.insert(tk.END, f"Límite superior: {self.resultado['LS']:.6f}\n")         
        self.resultado_text.insert(tk.END, f"Varianza teórica (1/12): {self.resultado['var_teorica']:.6f}\n")         
        self.resultado_text.insert(tk.END, f"Resultado: {'Pasa la prueba' if self.resultado['pasa'] else 'No pasa la prueba'}\n")         

    def mostrar_grafico_ventana(self):
        if not self.resultado:
            messagebox.showwarning("Aviso", "Primero ejecuta la prueba para generar los datos")
            return
        
        ventana_grafico = tk.Toplevel(self)
        ventana_grafico.title("Gráfico de Varianza")

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)

        # Dibujar líneas
        ax.axvline(self.resultado['LI'], color='red', linestyle='--', label="Límite Inferior")
        ax.axvline(self.resultado['LS'], color='red', linestyle='--', label="Límite Superior")
        ax.axvline(self.resultado['var_teorica'], color='green', linestyle=':', label="Varianza Teórica 1/12")
        ax.axvline(self.resultado['varianza'], color='blue', linewidth=2, label="Varianza Muestral")

        ax.set_title("Prueba de Varianza")
        ax.set_xlabel("Valores de varianza")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.6)

        # Embebido en ventana Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


