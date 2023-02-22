dias = ("lunes","martes","miercoles")

print(dias)
dias = list(dias)
dias.append("jueves")
dias = tuple(dias)
print(dias)

for dia in dias:
    print(dia)
