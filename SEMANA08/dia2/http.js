const http = require('http');

http.createServer(function(req,res){
    console.log("servidor activo...")
    console.log(req.url);
    switch(req.url){
        case '/':
            res.write('<h1><center>Bienvenido a mi servidor con nodejs</center></h1>')
            res.end()
            break;
        case '/login':
            res.write('<h1>Login de usuarios</h1>')
            res.end()
            break;
        default:
            res.write('<h1>Page Not Found</h1>')
            res.end()
        }
    
}).listen(5000);