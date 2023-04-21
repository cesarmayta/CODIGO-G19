const express = require('express')
const app = express()

const port = 5000

const path = require('path')
app.use(express.static(path.join(__dirname,'public')))

const server = app.listen(port,()=>console.log('http://localhost:5000'))

/************* web socket ***************/
const SocketIO = require('socket.io')

const io = SocketIO(server)

io.on('connection',(socket)=>{
    console.log('nueva conexión con id',socket.id)
})