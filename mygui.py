import tkinter as tk 
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Saludo","!Bienvenido!")
    messagebox.configure(bg="blue")

ventana = tk.Tk()
ventana.title("Mi Primera ")
ventana.geometry("200x100")
ventana.configure(bg="red")

boton = tk.Button(ventana, text="Haz clic aqui", command=saludar)
boton.pack(pady=20)

ventana.mainloop()