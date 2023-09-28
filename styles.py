# Estilos comunes para los componentes como los botones, etc.

from tkinter import ttk

# Esta función define cada uno de los estilos de cada componente en la aplicación
def get_app_style():
  app_style = ttk.Style()
  app_style.configure('EstiloBotones.TButton', relief='flat', 
                 foreground='#000000', 
                 background='#D9D9D9',
                 height= 25,
                 width=20,
                 borderwidth=4, font=('Inter Bold', 20))

  app_style.configure('BotonPersonalizado.TButton', 
                 relief='flat', 
                 foreground='#555454', 
                 background='#B3D5EE', 
                 borderwidth=4, font=('Inter Bold', 12))

  app_style.configure('BotonBuscarImagen.TButton', 
                 relief='flat', 
                 foreground='#555454', 
                 background='#B3D5EE',
                 width=20, 
                 height=20, 
                 borderwidth=20, font=('Inter Bold', 12))

  app_style.configure('BotonGuardarCambios.TButton', 
                 relief='flat', 
                 foreground='#000000', 
                 background='#8EFF9A',
                 width=20, 
                 height=20, 
                 borderwidth=20, font=('Inter Bold', 12))
  app_style.configure('')
  return app_style
