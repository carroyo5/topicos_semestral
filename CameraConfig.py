import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class CameraScreen(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Cámara')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        self.iconbitmap(r'.\logo\cat_face_icon.ico')
        self.capture = None
        self.label = tk.Label(self)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.camara()

    def camara(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            messagebox.showerror('Mensaje de error', 'Error al abrir la cámara.')
            self.destroy()
            return
        self.update_camera()
    
    def update_camera(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img
            self.after(10, self.update_camera)
    
    def __del__(self):
        if self.capture is not None:
            self.capture.release()
            cv2.destroyAllWindows()

                

