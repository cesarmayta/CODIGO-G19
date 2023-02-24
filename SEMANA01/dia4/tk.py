from tkinter import *
from tkinter import messagebox

#instanciamos un objeto de la clase Tk()
app = Tk()
app.geometry('300x100')
app.title('Mi primera App con Tk')

def saludar():
    messagebox.showinfo("mensaje","Hola " + txtNombre.get())

#agregamos frames
frame = LabelFrame(app,text='Nueva Ventana')
frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
#agregamos label
lbNombre = Label(frame,text='Nombre : ')
lbNombre.grid(row=1,column=0)
#agregamos caja de texto
txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1)
#agregamos un botón
btnSaludo = Button(frame,text='Saludar',command=saludar)
btnSaludo.grid(row=1,column=2)

app.mainloop()