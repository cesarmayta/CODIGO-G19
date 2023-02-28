import requests
from bs4 import BeautifulSoup

class TipoCambioSbs:
    
    def __init__(self):
        self.url = requests.get('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')
        
    def obtenerTipoCambio(self):
        if(self.url.status_code == 200):
            listaMonedas = []
            html = BeautifulSoup(self.url.text,'html.parser')
            for i in range(7):
                fila  = html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)})
                moneda = fila.find('td',{'class':'APLI_fila3'})
                compra = fila.find('td',{'class':'APLI_fila2'})
                venta = fila.find('td',{'class':'APLI_fila2'}).findNext('td')
                dicMoneda = {
                    'moneda':moneda.get_text(),
                    'compra':compra.get_text(),
                    'venta':venta.get_text()
                }
                listaMonedas.append(dicMoneda)
        else:
            print('error : '+ str(self.url.status_code))
            
        return listaMonedas
    
sbs = TipoCambioSbs()
print(sbs.obtenerTipoCambio())
        