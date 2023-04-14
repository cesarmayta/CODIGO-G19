const express = require('express')

const app = express()

//middlewares de aplicación
app.use(function(req,res,next){
    console.log('esto es un middleware')
    next()
})
app.use((req,res,next)=>{
    const timeElapsed = Date.now()
    const today = new Date(timeElapsed)
    console.log('ejecutado a las',today.toISOString())
    next()

})



app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'ejemplo de middlewares'
    })
})

app.listen(5000,()=>console.log('http://localhost:5000'))