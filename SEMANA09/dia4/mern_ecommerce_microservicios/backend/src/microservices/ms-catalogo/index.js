const express = require('express')
const {config} = require('../../config')
const cors = require('cors')
require('../../libs/mongoose.lib')

const app = express()

app.use(cors())
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'microservicio de catalogo'
    })
})

app.use('/products',require('../../routes/product.route'))

app.listen(config.mscatalogo.port,function(){
    console.log(`ms catalogo : http://localhost:${config.mscatalogo.port}`)
})