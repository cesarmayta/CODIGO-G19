const express = require('express')
const app = express()

const port = 5000

const path = require('path')
app.use(express.static(path.join(__dirname,'public')))

const server = app.listen(port,()=>console.log('http://localhost:5000'))