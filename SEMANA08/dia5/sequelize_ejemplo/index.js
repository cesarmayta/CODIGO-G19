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

app.get('/tarea/:id',(req,res)=>{
    Tarea.findByPk(req.params.id)
    .then(function(data){
        res.json(data)
    })
})

app.put('/tarea/:id',(req,res)=>{
    Tarea.findByPk(req.params.id)
    .then(function(data){
        data.update({
            descripcion: req.body.descripcion,
            estado:req.body.estado
        }).then(function(dataAct){
            res.json(dataAct)
        })
    })
})

app.delete('/tarea/:id',(req,res)=>{
    Tarea.findByPk(req.params.id)
    .then((tareaDel)=>{
        tareaDel.destroy()
    }).then((data)=>{
        res.sendStatus(201)
    })
})

app.listen(5000,()=>console.log('http://localhost:5000'))