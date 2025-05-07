import tkinter as tk

def main() :
  #Crear la ventana principal
  ventana = tk.Tk()
  ventana.geometry("700x700")
  ventana.title("ejercicio 2")
  ventana.configure(bg="red")
 

  # Crear la etiqueta
  etiqueta = tk.Label(ventana, text="Ejercicio 2", font=("Arial", 16))
  etiqueta = tk.Label(ventana, text="Jorge", font=("Arial", 16))
  etiqueta.pack() # Coloca la etiqueta en la ventana

  #ejecutar la ventana
  ventana.mainloop()
if __name__=="__main__":
    main()

