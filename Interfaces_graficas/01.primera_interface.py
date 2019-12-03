# la libreria tk viene instalada por defecto con windows 
#en linux (ubuntu-debian) se instala con sudo apt install python3-tk

from tkinter import *

programa=Tk()

#tamaño por defecto px
# programa.geometry("1350x700")

#color de fond
programa.config(bg="white")

#poner titulo a la ventana
programa.title("Ventana de prueba")

#evita o permite que el progarama de redimensione (ancho,alto)
# programa.resizable(False,False)

#crear primera subvenatana
miFrame=Frame()
#asociar el frame al loop principal
miFrame.pack(fill="both",expand="True")
miFrame.config(bg="blue")
miFrame.config(width="1300", height="720")
miFrame.config(bd=4)
miFrame.config(relief="groove")

#este metodo debe estar al final siempre
programa.mainloop()