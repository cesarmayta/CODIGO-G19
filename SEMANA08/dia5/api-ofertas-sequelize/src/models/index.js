const {Empresa,EmpresaSchema} = require('./empresa.models')
const {Oferta,OfertaSchema} = require('./oferta.models')

function setupModels(sequelize){
    Empresa.init(EmpresaSchema,Empresa.config(sequelize))
    Oferta.init(OfertaSchema,Oferta.config(sequelize))

    Oferta.associate(sequelize.models)

}

module.exports = setupModels;