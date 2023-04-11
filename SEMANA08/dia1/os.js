const os = require('os')

procesador = os.arch()
sistemaOperativo = os.platform()
cpu = os.cpus().length;
memoria = os.totalmem();

console.log('procesador : ' + procesador)
console.log('sistema operativo : ' + sistemaOperativo)
console.log('CPU ' +  cpu);
console.log('Memoria Ram : ' + memoria)
memoria = memoria / 1024;
console.log('Memoria en kb : ' + memoria)
memoria = memoria / 1024;
console.log('Memoria en mb : ' + memoria)
memoria = memoria / 1024;
console.log('Memoria en gb : ' + memoria)

//retornar la memoria rm en kb,mb,gb utilizando promesas
function calcularMemoria(capacidad,tipo){
    return new Promise((res,rej)=>{
        let memoria_convertida = capacidad / 1024
        console.log('MEMORIA EN ' + tipo + ' : ' + memoria_convertida)
        res(memoria_convertida)
    })
}
console.log("========== MEMORIA CON PROMESAS =========")
calcularMemoria(os.totalmem(),'KB')
    .then((kb)=>calcularMemoria(kb,'MB'))
    .then((mb)=>calcularMemoria(mb,'GB'))
    .then((gb)=>calcularMemoria(gb,'TB'))