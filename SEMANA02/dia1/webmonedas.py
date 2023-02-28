from flask import Flask,request,render_template,redirect
from TipoCambioSbs import TipoCambioSbs
from tabulate import tabulate

app =  Flask(__name__)

tipoCambio = TipoCambioSbs()
listaMonedas = tipoCambio.obtenerTipoCambio()

@app.route('/')
def index():
    """httpResponse = "<center><h1>TIPOS DE CAMBIO DEL DÍA</h1></center>"
    
    columnas = ['moneda','compra','venta']
    tablaMonedas = [moneda.values() for moneda in listaMonedas]
    htmlTablaMonedas = tabulate(tablaMonedas,headers=columnas,tablefmt='html')
    print(htmlTablaMonedas)
    httpResponse += htmlTablaMonedas
    
    return httpResponse"""
    
    strTitulo = "TIPO DE CAMBIO DE LA SBS"
    montoResultado = request.args.get('monto','nn')
    return render_template('index.html',titulo=strTitulo,monedas=listaMonedas,monto=montoResultado)
    
@app.route('/convertir',methods=['POST'])
def convertir():
    if request.method == "POST":
        montoSoles = request.form['soles']
        tipoMoneda = request.form['tipomoneda']
        dicMoneda = tipoCambio.buscarTipoCambio(listaMonedas,tipoMoneda)
        print(dicMoneda)
        resultado = round(float(montoSoles) / float(dicMoneda['compra']),2)
        
        
    #return '<h1>El monto es : {}</h1>'.format(round(resultado,2))
    return redirect('/?monto='+str(resultado))

app.run(debug=True)