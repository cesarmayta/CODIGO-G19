const Sequelize = require('sequelize')

const sequelize = new Sequelize('db_sequelize','root','',{
    host:'localhost',
    dialect:'mysql'
})

sequelize.authenticate()
.then(()=>console.log("conectado a bd"))
.catch(err=>console.log("error : " + err))

const Tarea = sequelize.define(
    'tarea',
    {
        descripcion:Sequelize.STRING,
        estado:Sequelize.STRING
    }
)
//sequelize.sync()

module.exports = {sequelize,Tarea}



