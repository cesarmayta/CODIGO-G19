const MysqlLib = require('../lib/mysql')

class CategoriaService{

    constructor(){
        this.db = new MysqlLib()
    }

    async getAll(){
        const sqlAll = `select categoria_id as id,
                        categoria_descripcion as descripcion
                        from tbl_categoria`
        const result = await this.db.querySql(sqlAll)
        return result
    }
}

module.exports = CategoriaService