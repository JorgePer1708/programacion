import tkinter as tk

def main() :
  #Crear la ventana principal
  ventana = tk.Tk()
  ventana.geometry("400x200")
  ventana.title("Ejemplo de etiqueta")
 

  # Crear la etiqueta
  etiqueta = tk.Label(ventana, text="Texto de la etiqueta", font=("Arial", 16))
  etiqueta.pack() # Coloca la etiqueta en la vetana

  #ejecutar la ventana
  ventana.mainloop()
if __name__=="__main__":
    main()
