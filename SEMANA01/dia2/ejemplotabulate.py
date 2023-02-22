from tabulate import tabulate

tabla = [
    ["cesar mayta","cesarmayt@gmail.com","89898998"],
    ["cesar mayta","cesarmayt@gmail.com","89898998"]
]

cabeceras = ["nombre","email","celular"]

print(tabulate(tabla,headers=cabeceras,tablefmt="grid"))