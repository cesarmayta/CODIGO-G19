const {MongoClient} = require('mongodb')

const url = 'mongodb://localhost:27017'
const client = new MongoClient(url)


async function main(){
    await client.connect()
    console.log("estas conectado a mongodb")

    const db = client.db('db_codigo_g19')
    const collection = db.collection('alumnos')

    const insertar = await collection.insertOne({nombre:'Laura Zuñiga',email:'laura@gmail.com',nota:20})
    console.log('nueva tarea : ',insertar)

    const result = await collection.find().toArray()
    console.log('listado de alumnos',result)
    return 0
}

main()