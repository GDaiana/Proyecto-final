from PIL import Image, ImageTk 
import tkinter
from tkinter import filedialog, PhotoImage


def buscar_nueva():
    global m
    archivo = filedialog.askopenfilename(filetypes=[("Image",("*.jpg","*.png"))])
    m = Image.open(archivo)
    m.thumbnail((500,500))
    m = ImageTk.PhotoImage(m)
    global imagen
   
    imagen.destroy()
    imagen = tkinter.Label(ventana, image=m)
    imagen.image = m
    imagen.pack()
    
def guardar_nueva():
    
    archivo =filedialog.asksaveasfile()
    m.save("image/nuevasimagenes")
    
    imagen = tkinter.Label(ventana)
    imagen.pack()
    



ventana = tkinter.Tk()
ventana.geometry("800x600") 
img_boton=Image.open("carpeta.png")

img_boton = PhotoImage(file="carpeta.png")

img_boton2=Image.open("disco-flexible.png")
img_boton2 = PhotoImage(file="disco-flexible.png")




btn = tkinter.Button(ventana,image=img_boton,height=100,width=100,command=buscar_nueva)

btn.pack(side="left")
btn.place(x=200,y=30)



btn_2= tkinter.Button(ventana,image=img_boton2,height=100,width=100,command=guardar_nueva)

btn_2.pack(side="right")
btn_2.place(x=600,y=30)

imagen = tkinter.Label(ventana)
imagen.pack()





ventana.mainloop()
