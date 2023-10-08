import tkinter as tk
from tkinter import ttk
from styles import get_app_style
from tkinter import filedialog
from CameraConfig import CameraScreen
import _tkinter

class InitialScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        #Cofiguracion de la pantalla
        self.title('Pantalla de Inicio')
        self.geometry('520x520')
        self.resizable(width=False, height=False)
        self.iconbitmap(r'.\logo\cat_face_icon.ico')
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
                font=('Inter Bold',20)).place(x=45, y=50)
    
    def camera_button(self):
        self.camera_icon = tk.PhotoImage(file=r'.\button_icon\camera_icon.png')
        self.camera = ttk.Button(self,
                                text= 'Cámara',
                                style='EstiloBotones.TButton',
                                image=self.camera_icon,
                                compound='left',
                                command=self.camera_cv2)
        self.camera.place(x=45, y=200)
    
    def search_file(self):
        self.search_icon = tk.PhotoImage(file=r'.\button_icon\search.png')
        self.search = ttk.Button(self,
                                 text='Buscar un vídeo o imagen',
                                 style='EstiloBotones.TButton',
                                 image=self.search_icon,
                                 compound='left',
                                 command=self.search_function)
        self.search.place(x=42, y=270)
        
    def search_function(self):
        self.selected_file = filedialog.askopenfilename(
            filetypes=[('Imagenes', '*.png; *.jpg; *.jpeg'),
                       ('Archivos de Video', '*.mp4; *.avi')])
        self.path = tk.Label(self, text='', wraplength=500)
        self.path.place(x=35, y = 420)
        if self.selected_file:
            self.path.config(text=f'Archivo: {self.selected_file}', 
                        font=('Inter Bold', 10), 
                        foreground='#75AD3C')
        else:
            self.path.config(text='')
        
    def exit_button(self):
        self.exit_icon = tk.PhotoImage(file=r'.\button_icon\exit.png')
        self.exit = ttk.Button(text='Salir',
                                style= 'EstiloBotones.TButton',
                                image= self.exit_icon,
                                compound='left',
                                command= lambda: self.destroy())
        self.exit.place(x=42, y=350)

    def camera_cv2(self):
        try:
            self.withdraw()
            camera_screen = CameraScreen(self)
            camera_screen.mainloop()
            self.deiconify()
        except _tkinter.TclError as wm_command:
            print(wm_command)

if __name__ == '__main__':
    InitialScreen().mainloop()