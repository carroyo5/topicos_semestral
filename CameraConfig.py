import cv2
import tkinter as tk
from tkinter import messagebox

class CameraScreen(tk.Toplevel):
    def __init__(self, master= None):
        super().__init__(master)
        self.title('Cámara')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        self.iconbitmap(r'.\logo\cat_face_icon.ico')
        self.camara()

    def camara(self):
        capture = cv2.VideoCapture(0)
        if capture.isOpened() is False:
            messagebox.showerror('Mensaje de error', 'Error al abrir la cámara.')
            self.deiconify()
            self.destroy()
            return 

        while capture.isOpened():
            ret, frame = capture.read()
            if ret is True:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = tk.PhotoImage(data=frame.tobytes(), format='PPM')
                if hasattr(self, 'label'):
                    self.label.config(image=img)
                    self.label.image = img
                else:
                    self.label = tk.Label(self, image=img)
                    self.label.pack()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        capture.release()
        cv2.destroyAllWindows()

                

