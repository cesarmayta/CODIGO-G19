const os = require('os')
const tam = 1024

async function memoria(capacidad){
    capacidad_convertida = capacidad / tam;
    return capacidad_convertida.toFixed(2);
}

async function main(){
    console.log("======= MEMORIA RAM CON ASYNC AWAIT")
    kb = await memoria(os.totalmem())
    mb = await memoria(kb)
    gb = await memoria(mb)
    tb = await memoria(gb)
    console.table([
        {
            capacidad:'KB',tam:kb
        },
        {
            capacidad:'MB',tam:mb
        },
        {
            capacidad:'GB',tam:gb
        },
        {
            capacidad:'TB',tam:tb
        }
    ])
}

main()