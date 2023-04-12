const express = require('express')
const bp = require('body-parser')

const app = express()


app.use(bp.json())
app.use(bp.urlencoded({extended : true}))


app.use(express.static('public'))


app.get('/',function(req,res){
    res.send('<h1><center>Bienvenido a mi web con express</center><h1><hr/>')
})

app.get('/api',(req,res)=>{
    res.json({
        'status':true,
        'content':'api rest activo'
    })
})

app.get('/saludo',(req,res)=>{
    let nombre = req.query.nom
    res.send('hola ' + nombre)
})

app.get('/suma/:n1/:n2',(req,res)=>{
    const {n1,n2} = req.params

    let suma = parseInt(n1) + parseInt(n2);
    res.send('la suma es ' +  suma)
})

app.post('/calculadora',(req,res)=>{
    let operacion = req.query.ope;
    resultado = 0
    //if(operacion === "suma"){
        n1 = req.body.n1;
        n2 = req.body.n2;
        console.log(n1)
        resultado = parseInt(n1) + parseInt(n2);
    //}
    res.send('resultado : ' + resultado)
})



app.listen(5000,()=>console.log('sevidor activo en http://localhost:5000'))