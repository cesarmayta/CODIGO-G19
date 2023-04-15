const Joi = require('joi');

const descripcion = Joi.string().min(3).max(200)

const catalogSchema = Joi.object({
    descripcion : descripcion.required()
})

module.exports = {catalogSchema}