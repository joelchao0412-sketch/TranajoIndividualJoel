import tkinter as tk
from tkinter import ttk

class MenuLateral(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Estilo
        self.config(bg="#f0f0f0", width=200)
        self.pack_propagate(False)
        
        # Título
        tk.Label(self, text="Menú Principal", font=("Arial", 14, "bold"), 
                bg="#f0f0f0").pack(pady=10)
        
        # Botones para generadores
        tk.Label(self, text="Generadores", font=("Arial", 12, "bold"), 
                bg="#f0f0f0").pack(pady=(10, 5), anchor="w")
        
        btn_cuadrados = tk.Button(self, text="Cuadrados Medios", 
                                 command=lambda: controller.mostrar_frame("FrameCuadradosMedios"))
        btn_cuadrados.pack(fill="x", padx=10, pady=2)
        
        btn_productos = tk.Button(self, text="Productos Medios", 
                                 command=lambda: controller.mostrar_frame("FrameProductosMedios"))
        btn_productos.pack(fill="x", padx=10, pady=2)
        
        btn_multiplicador = tk.Button(self, text="Multiplicador Constante", 
                                     command=lambda: controller.mostrar_frame("FrameMultiplicadorConstante"))
        btn_multiplicador.pack(fill="x", padx=10, pady=2)
        
        # Botones para pruebas
        tk.Label(self, text="Pruebas", font=("Arial", 12, "bold"), 
                bg="#f0f0f0").pack(pady=(20, 5), anchor="w")
        
        btn_chi = tk.Button(self, text="Chi Cuadrado", 
                           command=lambda: controller.mostrar_frame("FrameChiCuadrado"))
        btn_chi.pack(fill="x", padx=10, pady=2)
        
        btn_medias = tk.Button(self, text="Prueba de Medias", 
                              command=lambda: controller.mostrar_frame("FramePruebaMedias"))
        btn_medias.pack(fill="x", padx=10, pady=2)
        
        btn_varianza = tk.Button(self, text="Prueba de Varianza", 
                                command=lambda: controller.mostrar_frame("FramePruebaVarianza"))
        btn_varianza.pack(fill="x", padx=10, pady=2)