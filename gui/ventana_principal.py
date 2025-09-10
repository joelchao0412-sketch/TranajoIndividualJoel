import tkinter as tk
from tkinter import ttk
from gui.menu_lateral import MenuLateral
from gui.frames import (FrameCuadradosMedios, FrameProductosMedios, 
                        FrameMultiplicadorConstante, FrameChiCuadrado,
                        FramePruebaMedias, FramePruebaVarianza)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Generadores y Pruebas de Aleatoriedad")
        self.geometry("900x600")
        self.resizable(True, True)
        
        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        
        # Diccionario para almacenar los frames
        self.frames = {}
        
        # Crear menú lateral
        self.menu_lateral = MenuLateral(self.container, self)
        self.menu_lateral.grid(row=0, column=0, sticky="nsew")
        
        # Crear frames para cada sección
        for F in (FrameCuadradosMedios, FrameProductosMedios, 
                 FrameMultiplicadorConstante, FrameChiCuadrado,
                 FramePruebaMedias, FramePruebaVarianza):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=1, sticky="nsew")
        
        # Mostrar frame inicial
        self.mostrar_frame("FrameCuadradosMedios")
    
    def mostrar_frame(self, nombre_frame):
        frame = self.frames[nombre_frame]
        frame.tkraise()