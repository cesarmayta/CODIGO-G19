const MysqlLib = require('../lib/mysql')

class CategoriaService{

    constructor(){
        this.db = new MysqlLib()
        this.table_name = "categoria"
    }

    async getAll(){
        const sqlAll = `select ${this.table_name}_id as id,
                        ${this.table_name}_descripcion as descripcion
                        from tbl_${this.table_name}`
        const result = await this.db.querySql(sqlAll)
        return result
    }

    async create({data}){
        const sqlCreate = `insert into tbl_${this.table_name}
                           (${this.table_name}_descripcion) 
                           values('${data.descripcion}')`
        
        await this.db.querySql(sqlCreate);
        const sqlLast = `select ${this.table_name}_id as id,${this.table_name}_descripcion as descripcion
                        from tbl_${this.table_name} order by ${this.table_name}_id desc limit 1`
        const result = await this.db.querySql(sqlLast)
        return result
    }
}

module.exports = CategoriaService