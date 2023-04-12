const mysql = require('mysql')

const mysqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'db_tareas_node_g19'
})

mysqlConnection.connect(function(err){
    if(err){
        console.error(err);
        return;
    }
    else{
        console.log('conectado a la bd')
    }
})

module.exports = mysqlConnection