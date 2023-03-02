import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

print("conexión exitosa")

from firebase_admin import firestore

db = firestore.client()

colProyectos = db.collection('proyectos')
listProyectos = colProyectos.get()

for docProyecto in listProyectos:
    print(docProyecto.to_dict())
