const express = require('express')

const {sequelize,Tarea} = require('./database')

/*
sequelize.sync()
.then(()=>{
    console.log("migración exitosa")
    Tarea.bulkCreate(
        [
            {descripcion:'aprender sequelize',estado:'pendiente'}
        ]
    )
})*/

const app = express()

app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo'
    })
})

app.get('/tarea',(req,res)=>{
    Tarea.findAll()
    .then(function(resultado){
        //console.log(resultado)
        res.json(resultado)
    })
})

app.post('/tarea',(req,res)=>{
    Tarea.create(
        {
            descripcion: req.body.descripcion,
            estado:req.body.estado
        }
    ).then((data)=>{
        res.json(data)
    })
})

app.listen(5000,()=>console.log('http://localhost:5000'))