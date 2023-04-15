const { Model,DataTypes,Sequelize} = require('sequelize')

const {EMPRESA_TABLE} = require('./empresa.models')

const TABLE_NAME = 'tbl_oferta'

const OfertaSchema = {
    id:{
        field:'oferta_id',
        allowNull:false,
        primaryKey:true,
        autoIncrement:true,
        type:DataTypes.INTEGER
    },
    nombre:{
        allowNull:false,
        type:DataTypes.STRING,
        field:'oferta_titulo'
    },
    empresaId:{
        field:'empresa_id',
        allowNull:false,
        type:DataTypes.INTEGER,
        references:{
            model:EMPRESA_TABLE,
            key:'empresa_id'
        },
        onUpdate:'CASCADE',
        onDelete:'SET NULL'
    }
}

class Oferta extends Model {
    static associate(models){
        this.belongsTo(models.Empresa,{as :'empresa'})
    }

    static config(sequelize){
        return {
            sequelize,
            tableName: TABLE_NAME,
            modelName:'Oferta',
            timestamps : false
        }
    }
}

module.exports = {Oferta,OfertaSchema,TABLE_NAME}

