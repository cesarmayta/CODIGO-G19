""" 
palindromos:
oso
ana
atar a la rata
anita lava la tina
"""

palabraInicial = input("escribe una palabra : ")
palabraInicial = palabraInicial.replace(' ','')
palabraInicial = palabraInicial.lower()
palabraReversa = palabraInicial[::-1]
if(palabraInicial == palabraReversa):
    print(" es un palindromo")
else:
    print("No es un palindromo")