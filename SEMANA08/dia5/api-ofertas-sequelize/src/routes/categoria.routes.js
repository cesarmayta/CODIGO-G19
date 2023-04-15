const express = require('express')
const CategoriaService = require('../services/categoria.service')

const boom = require('@hapi/boom')

//middlewares
const validatorHandler = require('../middlewares/validator.handler')
const {verifyToken} = require('../middlewares/auth.handler')


const {catalogSchema} = require('../schemas/catalog.schema')

function categoriaApi(app){
    const router = express.Router();
    app.use('/categoria',router)

    const objCategoria = new CategoriaService();

    router.get('/',verifyToken,async function(req,res){
        try{
            const data = await objCategoria.getAll()
            res.status(200).json({
                status:true,
                content:data
            })
        }catch(err){
            //console.log(err)
            res.status(500).json(boom.badData('ERROR DEL SERVIDOR'))
        }
    })

    router.post('/',verifyToken,
        validatorHandler(catalogSchema,'body')
        ,async function(req,res){
        const {body : data} = req;
        console.log(data);
        try{
            const newData = await objCategoria.create({data})
            res.status(201).json({
                status:true,
                content:newData[0]
            })
        }catch(err){
            res.status(500).json(boom.badData(err))
        }
    })

    router.get('/:id',async function(req,res){
        const {id} = req.params
        try{
            const data = await objCategoria.getById(id);
            if(data.length > 0){
                res.status(200).json({
                    status:true,
                    content:data[0]
                })
            }else{
                /*res.status(404).json({
                    status:false,
                    content:'no hay registros'
                })*/
                res.json(boom.notFound('no hay registros'))
            }
        }catch(err){
            res.status(500).json(boom.badData('error : ' + err))
        }
    })

    router.put('/:id',
        validatorHandler(catalogSchema,'body')
        ,async function(req,res){
        const {id} = req.params
        const {body:data} = req

        try{
            const updateData = await objCategoria.update({data,id})
            if(updateData.length > 0){
                res.status(200).json({
                    status:true,
                    content:updateData[0]
                })
            }else{
                res.json(boom.notFound('no hay registros'))
            }
        }catch(err){
            res.status(500).json(boom.badData(err))
        }
    })

    router.delete('/:id',async function(req,res){
        const {id} = req.params

        try{
            const dataDeleted = await objCategoria.delete(id)
            if(dataDeleted){
                res.status(201).json({
                    status:true,
                    content:'registro eliminado'
                })
            }else{
                res.json(boom.notFound('no hay registros'))
            }
        }catch(err){
            res.status(500).json(boom.badData(err))
        }
    })
}

module.exports = categoriaApi