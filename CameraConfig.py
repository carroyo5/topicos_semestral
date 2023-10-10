import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from styles import get_app_style
from recognitionLogic import CatRecognition

class CameraScreen(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Cámara')
        self.geometry('1280x720')
        styles = get_app_style()
        self.resizable(width=False, height=False)
        self.iconbitmap(r'.\logo\cat_face_icon.ico')
        self.capture = None
        self.label = tk.Label(self)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.cat_recognition = CatRecognition
        self.create_buttons()
        self.camara()

    def create_buttons(self):
        button_frame = tk.Frame(self)
        #Marco para los botones, se define un marco 
        # para poner los botones en un marco aparte del de la camara
        button_frame.pack(side=tk.TOP, fill=tk.X)
        # Se utiliza la literal X para que tkinter expanda horizontalmente los botones
        self.capture_icon = tk.PhotoImage(file=r'.\button_icon\capture.png')
        self.capture_button = ttk.Button(button_frame, 
                                         text='Capturar',
                                        style='EstiloBotones.TButton',
                                        compound='left',
                                        image= self.capture_icon,
                                        command=self.capture_information,
                                         )
        self.capture_button.pack(side=tk.LEFT, padx=15, pady=15)

        self.exit_icon = tk.PhotoImage(file=r'.\button_icon\exit.png')
        self.exit_button = ttk.Button(button_frame, 
                                      text='Salir', 
                                      style='EstiloBotones.TButton',
                                      image=self.exit_icon, 
                                      compound='left', 
                                      command=self.screen_callback)
        self.exit_button.pack(side=tk.RIGHT, padx=15,pady=15)

    def screen_callback(self):
        self.destroy()
        self.master.deiconify()

    def camara(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            messagebox.showerror('Mensaje de error', 'Error al abrir la cámara.')
            self.destroy()
            return
        self.update_camera()
    
    def draw_rectangle(self):
        #Funcion para dibujar un recuadro al rededor del gato 
        pass

    def draw_text(self):
        #Mostrar si se esta identificando el porcentaje correcto del gato
        # e informacion extra
        pass
    
    def capture_information(self):
        if self.cat_recognition.check():
            pass
        else:
            #Se procede a pasar los parametros de la cámara.
            x, y = self.frame.shape
            self.cat_recognition(x,y)

    def update_camera(self):
        ret, self.frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img
            self.after(10, self.update_camera)


                

