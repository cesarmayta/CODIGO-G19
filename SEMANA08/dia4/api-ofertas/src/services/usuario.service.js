const MysqlLib = require('../lib/mysql')
const bcrypt = require('bcryptjs')

class UsuarioService{

    constructor(){
        this.db = new MysqlLib()
    }

    async create({usuario}){
        const passwordEncriptado = await bcrypt.hash(usuario.password,10)

        const sqlCreate = `insert into tbl_usuario(usuario_nombre,
                           usuario_password)
                           values('${usuario.usuario}',
                           '${passwordEncriptado}')`
        
        await this.db.querySql(sqlCreate)

        const sqlLastInsert = `select usuario_id as id,
                               usuario_nombre as usuario
                               from tbl_usuario order by usuario_id
                               desc limit 1`
        const result = await this.db.querySql(sqlLastInsert)

        return result
    }
}

module.exports = UsuarioService