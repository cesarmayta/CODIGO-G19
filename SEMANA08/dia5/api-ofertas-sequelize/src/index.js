const express = require('express')
const {config} = require('./config');
const cors = require('cors')

const categoriaApi = require('./routes/categoria.routes')
const experienciaApi = require('./routes/experiencia.routes')
const usuarioApi = require('./routes/usuario.routes')
const authApi = require('./routes/auth.routes')
const empresaApi = require('./routes/empresa.routes')

const {errorHandler,boomErrorHandler} = require('./middlewares/error.handler')

const app = express()

app.use(cors())

app.use(express.json())

app.get('/',(req,res)=>{
    //console.log(a + 3)
    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

categoriaApi(app)
experienciaApi(app)
usuarioApi(app)
authApi(app)
empresaApi(app)

//manejador de errores
app.use(boomErrorHandler)
app.use(errorHandler)


app.listen(config.port,()=>console.log("http://localhost:"+config.port))