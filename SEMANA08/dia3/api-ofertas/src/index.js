const express = require('express')
const app = express()

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

app.listen(5000,()=>console.log("http://localhost:5000"))