import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseAdmin:
    
    def __init__(self):
        cred = credentials.Certificate("token.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        
    def getCollection(self,collectionName):
        listCollection = []
        collectionValues = self.db.collection(collectionName)
        docValues = collectionValues.get()
        for doc in docValues:
            dicCollection = doc.to_dict()
            listCollection.append(dicCollection)
            
        return listCollection
    
#fs = FirebaseAdmin()
#lista = fs.getCollection('proyectos')
#print(lista)