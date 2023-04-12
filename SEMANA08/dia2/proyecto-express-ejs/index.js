const express = require('express');
const app = express();

app.set('view engine','ejs')

app.get('/',(req,res)=>{
    let titulo = 'MIS PELICULAS FAVORITAS'
    let peliculas = [
        {
            titulo:'Super Mario Bross',
            imagen:'https://i.blogs.es/b7859f/super-mario-bros-la-pelicula/450_1000.jpeg'
        },
        {
            titulo:'John wick 4',
            imagen:'https://i.ytimg.com/vi/56s7ltckzoA/maxresdefault.jpg'
        },
        {
            titulo:'Misterio a bordo 2',
            imagen:'https://revistaronda.net/wp-content/uploads/2022/02/Adam-Cortesia-scaled.jpg'
        },

    ]

    context = {
        titulo:titulo,
        peliculas:peliculas
    }

    res.render('pages/index',context)
})

app.listen(5000)
console.log('http://localhost:5000')