const mongoose = require('mongoose')

async function main(){
    await mongoose.connect('mongodb://localhost:27017/db_codigo_g19')

    //creamos un schema
    const AlumnoSchema = new mongoose.Schema({
        nombre:String,
        email:String,
        nota:Number
    })

    const Alumno = mongoose.model('alumnos',AlumnoSchema)

    //listado de alumnos
    const listadoAlumnos = await Alumno.find()
    console.log(listadoAlumnos)

}

main()