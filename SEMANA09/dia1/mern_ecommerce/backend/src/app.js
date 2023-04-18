const express = require('express')
const {config} = require('./config')
const cors = require('cors')

const app = express()

//middlewares
app.use(cors())
app.use(express.json())

//configuración de puerto
app.set('port',config.port)

app.get('/',(req,res)=>{
    res.json({
        "success":true,
        "message":"api rest de ecommerce con stack MERN"
    })
})

//routes
app.use('/categories',require('./routes/category.route'))

module.exports = app