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
    },{
        freezeTableName: true,
        timestamps:false
    }
)

//migraciones
sequelize.sync()
.then(()=>{
    console.log("migración exitosa")
    Alumno.bulkCreate(
        [
            {nombre:'César Mayta',email:'cesarmayta@gmail.com'},
            {nombre:'Claudia Gonzales',email:'clau.gz@hotmail.com'}
        ]
    ).then(()=>{
        return Alumno.findAll()
    }).then((alumnos)=>console.log(alumnos))
})