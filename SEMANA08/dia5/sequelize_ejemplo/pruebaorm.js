const Sequelize = require('sequelize')

const sequelize = new Sequelize({
    dialect : 'sqlite',
    storage : './database.sqlite'
})

sequelize.authenticate()
.then(()=>console.log("conexión exitosa a bd"))
.catch(err=>console.log("error : " +err))

//crear un modelo
const Alumno = sequelize.define(
    'tbl_alumno',
    {
        nombre:Sequelize.STRING,
        email:Sequelize.STRING
    }
)

//migraciones
sequelize.sync()
.then(()=>{
    console.log("migración exitosa")
})