const express = require('express')
const ExperienciaService = require('../services/experiencia.service')

function experienciaApi(app){
    const router = express.Router();
    app.use('/experiencia',router)

    const objExperiencia = new ExperienciaService();

    router.get('/',async function(req,res){
        try{
            const data = await objExperiencia.getAll()
            res.status(200).json({
                status:true,
                content:data
            })
        }catch(err){
            console.log(err)
        }
    })
}

module.exports = experienciaApi