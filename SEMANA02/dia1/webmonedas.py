from flask import Flask,request,render_template
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
    
    return render_template('index.html')
    
    

app.run(debug=True)