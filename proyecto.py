from PIL import Image, ImageTk 
import tkinter
from tkinter import filedialog, PhotoImage


def buscar_nueva():
    global m
    archivo = filedialog.askopenfilename(filetypes=[("Image",("*.jpg","*.png"))])
    m = Image.open(archivo)
    m_tk = m
    m_tk.thumbnail((500,500))
    m_tk = ImageTk.PhotoImage(m_tk)
    global imagen
    imagen.configure(image=m_tk)
    imagen.image = m_tk
    imagen.pack()
    
def guardar_nueva():
    global m
    archivo = filedialog.asksaveasfilename(filetypes=[("JPEG","*.jpg")])
    m.save(archivo)




ventana = tkinter.Tk()
ventana.geometry("800x600") 
img_boton=Image.open("carpeta.png")

img_boton = PhotoImage(file="carpeta.png")

img_boton2=Image.open("disco-flexible.png")
img_boton2 = PhotoImage(file="disco-flexible.png")

frame_btn = tkinter.Frame(ventana)
frame_btn.pack(pady=20)


btn = tkinter.Button(frame_btn,image=img_boton,height=100,width=100,command=buscar_nueva)

btn.pack(side="left",padx=60)




btn_2= tkinter.Button(frame_btn,image=img_boton2,height=100,width=100,command=guardar_nueva)

btn_2.pack(side="right",padx=60)


imagen = tkinter.Label(ventana)
imagen.pack()





ventana.mainloop()
