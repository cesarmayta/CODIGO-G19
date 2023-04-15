const {models}  = require('../lib/sequelize')
const boom = require('@hapi/boom')

class EmpresaService{

    constructor(){

    }

    async getAll(){
        const result = await models.Empresa.findAll()
        return result
    }

    async create(data){
        const newData = await models.Empresa.create(data)
        return newData
    }

    async findOne(id){
        const data = await models.Empresa.findByPk(id)
        if(!data){
            throw boom.notFound('no existe el registro')
        }
        return data
    }

    async update(id,data){
        const dataUpdate = await this.findOne(id)
        const result = await dataUpdate.update(data)
        return result
    }

    async delete(id){
        const dataDelete = await this.findOne(id)
        await dataDelete.destroy()
        return true
    }

}

module.exports = EmpresaService