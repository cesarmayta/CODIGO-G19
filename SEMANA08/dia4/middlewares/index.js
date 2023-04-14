const express = require('express')
const morgan = require('morgan')

const app = express()
app.use(morgan('combined'))


//middlewares de aplicación
app.use(function(req,res,next){
    console.log('esto es un middleware')
    console.log('Request Type:', req.method);
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

//middleware a nivel de ruta
app.use('/usuario',(req,res,next)=>{
    console.log('Request URL:', req.originalUrl);
    next()
})

app.get('/usuario',(req,res)=>{
    console.log(a + 3)
    res.json({
        nombre:'admin',
        email:'admin@gmail.com'
    })
})

//middlewares a nivel de router
const router = express.Router();
router.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next();
  });

app.use('/router', router);


router.get('/user/:id', function (req, res, next) {
    // if the user ID is 0, skip to the next router
    if (req.params.id == 0) next('route');
    // otherwise pass control to the next middleware function in this stack
    else next(); //
  }, function (req, res, next) {
    // render a regular page
    res.render('regular');
  });


//middlewares para manejo de errores
app.use(function(err,req,res,next){
    console.error(err.stack)
    res.status(500).json({
        status:false,
        content:err.stack
    })
})

app.listen(5000,()=>console.log('http://localhost:5000'))