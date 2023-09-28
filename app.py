import tkinter as tk
from tkinter import ttk
from styles import get_app_style
import os
from tkinter import filedialog

class InitialScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        #Cofiguracion de la pantalla
        self.title('Pantalla de Inicio')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        #Se inicializan los estilos
        styles = get_app_style()
        self.title_screen()
        self.camera_button()
        self.search_file()
        self.exit_button()
    
    def title_screen(self):
        self.logo = tk.PhotoImage(file=r'.\logo\cat_face.png')
        ttk.Label(self, 
                text='Identificador de gatos', 
                image=self.logo,
                compound='left',
                font=('Inter Bold',20)).pack()
    
    def camera_button(self):
        self.camera_icon = tk.PhotoImage(file=r'.\button_icon\camera_icon.png')
        self.camera = ttk.Button(self,
                                text= 'Cámara',
                                style='EstiloBotones.TButton',
                                image=self.camera_icon,
                                compound='left',
                                command=self.camera_cv2)
        self.camera.pack()
    
    def search_file(self):
        self.search_icon = tk.PhotoImage(file=r'.\button_icon\search.png')
        self.search = ttk.Button(self,
                                 text='Buscar un vídeo o imagen',
                                 style='EstiloBotones.TButton',
                                 image=self.search_icon,
                                 compound='left',
                                 command=self.search_function)
        self.search.pack()
        
    def search_function(self):
        self.archivo_seleccionado = filedialog.askopenfilename(
            filetypes=[('Imagenes', '*.png; *.jpg; *.jpeg'),
                       ('Archivos de Video', '*.mp4; *.avi')])
        

    def exit_button(self):
        self.exit_icon = tk.PhotoImage(file=r'.\button_icon\exit.png')
        self.exit = ttk.Button(text='Salir',
                                style= 'EstiloBotones.TButton',
                                image= self.exit_icon,
                                compound='left',
                                command= lambda: self.destroy())
        self.exit.pack()

    def camera_cv2(self):
        pass

if __name__ == '__main__':
    InitialScreen().mainloop()