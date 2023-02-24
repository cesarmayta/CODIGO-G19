from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

conn = sqlite3.connect('alumnos.db')

c = conn.cursor()
c.execute("""
          CREATE TABLE if not exists alumnos(  
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT
          );
          """)


def nuevo_alumno():
    def guardar():
        pass
    
    
    top = Toplevel()
    top.title('Nuevo Alumno')
    
    lblNombre = Label(top,text='Nombre')
    lblNombre.grid(row=0,column=0)
    txtNombre = Entry(top,width=30)
    txtNombre.grid(row=0,column=1)
    
    lblEmail = Label(top,text='Email')
    lblEmail.grid(row=1,column=0)
    txtEmail = Entry(top,width=30)
    txtEmail.grid(row=1,column=1)
    
    btnGuardar = Button(top,text='Guardar',command=guardar)
    btnGuardar.grid(row=3,column=1)
        
    top.mainloop()

def eliminar_alumno():
    pass

app = Tk()
app.title('Crud de Alumnos')

#botones del programa
btn = Button(app,text='Nuevo Alumno',command=nuevo_alumno)
btn.grid(column=0,row=0)
btn = Button(app,text='Eliminar Alumno',command=eliminar_alumno)
btn.grid(column=1,row=0)

#grilla del programa
tree = Treeview(app)
tree['columns'] = ('Nombre','Email')
tree.column('#0',width=0,stretch=NO)
tree.column('Nombre')
tree.column('Email')
tree.heading('Nombre',text='Nombre')
tree.heading('Email',text='Email')
tree.grid(column=0,row=1,columnspan=2)

app.mainloop()