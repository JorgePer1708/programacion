import tkinter as tk


def main() :
    #Crear la ventana principal
    ventana = tk.Tk()
    ventana.geometry("700x700")
    ventana.title("ejercicio 3")

    def accionSaludar():
        titulo = tk.Label (ventana, text=f"Hola, [nombre], te saluda Jorge")
        #Etiqueta de texto

    etiquetaNombre = tk.Label (ventana, text= "Ingrese el nombre ")
    entry(nombre)


    #Boton
    boton = tk.Button(ventana, text="Saludar", command=accionSaludar)
    #ejecutar la ventana
    ventana.mainloop()
    
if __name__=="__main__":
    main()
