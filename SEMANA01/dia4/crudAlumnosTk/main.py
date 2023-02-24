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
    pass

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