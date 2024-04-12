#importamos lo que vamos a necesitar

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.filedialog
from PIL import Image,ImageTk
import cv2


"""
https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
"""

#se crea la pantalla y el titlo de la app
ventana = tk.Tk()
ventana.geometry('1200x1200')
ventana.title('Procesamiento imagenes')


##al momento que se ingresa a la app nos pide escoger un archvi o y almacenar el path en esta variable global
archivo = tk.filedialog.askopenfilename(initialdir="/",
                                        title="Seleccione archivo",
                                        filetypes=(("png files", "*.png"), ("all files", "*.*")))



##se crean los componentes del primer tabulador
def crear_componentes_gris(tabulador):

    ##indicamos que se va a trabajar con la variable global definida antes
    global archivo

    ##leemos el archivo y lo pasamos a gris
    foto=cv2.imread(archivo)
    foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

    foto=Image.fromarray(foto)

    ##procesamos la imaen
    imagen = ImageTk.PhotoImage(foto)

##se encarga de mostar los detalles  de la imagen
    def mostrar_titulo():
        ##creamos un recuadro de dialogo con las caracteristicas de la imagen
        messagebox.showinfo('Informacion de la imagen', f""" ruta: {archivo}
                dimensiones {imagen.height()} x {imagen.width()}
        """)


    ##al hacer clic en la imagen nos mostrara la informacion
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)

    ## posicionamos la imagen
    boton_imagen.grid(row=0, column=0)







def crear_componentes_gauss(tabulador):
    ##indicamos que se va a trabajar con la variable global definida antes
    global archivo

    ##leemos el archivo y aplicamos un filtro gaussiano
    foto = cv2.imread(archivo)
    foto = cv2.GaussianBlur(foto, (5, 5), 0)

    foto = Image.fromarray(foto)

    ##procesamos la imaen
    imagen = ImageTk.PhotoImage(foto)

    ##se encarga de mostar los detalles  de la imagen
    def mostrar_titulo():
        ##creamos un recuadro de dialogo con las caracteristicas de la imagen
        messagebox.showinfo('Informacion de la imagen', f""" ruta: {archivo}
                    dimensiones {imagen.height()} x {imagen.width()}
            """)

    ##al hacer clic en la imagen nos mostrara la informacion
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)

    ## posicionamos la imagen
    boton_imagen.grid(row=0, column=0)


def crear_componentes_normal(tabulador):
    ##indicamos que se va a trabajar con la variable global definida antes
    global archivo

    ##leemos la imagen
    imagen = tk.PhotoImage(file=archivo)


    ##se encarga de mostar los detalles  de la imagen
    def mostrar_titulo():
        ##creamos un recuadro de dialogo con las caracteristicas de la imagen
        messagebox.showinfo('Informacion de la imagen', f""" ruta: {archivo}
                    dimensiones {imagen.height()} x {imagen.width()}
            """)

    ##al hacer clic en la imagen nos mostrara la informacion
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)

    ## posicionamos la imagen
    boton_imagen.grid(row=0, column=0)




#renderizamos las tabs para que se muestren en la app
def crear_tabs():
    control_tabulador = ttk.Notebook(ventana)
    control_tabulador.pack(fill='both')
    tabulador1 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador1, text='escala grises')
    crear_componentes_gris(tabulador1)
    tabulador2 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador2, text='filtro')
    crear_componentes_gauss(tabulador2)
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='imagen normal')
    crear_componentes_normal(tabulador3)



crear_tabs()

ventana.mainloop()