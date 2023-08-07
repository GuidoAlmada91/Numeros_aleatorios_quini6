import json
with open("mi_archivojson.json") as file:
    data_lectura = json.load(file)

for clientes in data_lectura["clientes"]:
    print("Nombre: ", clientes["Nombre"])
    print("Apellido: ", clientes["Apellido"])
    print("Edad: ", clientes["Edad"])
    print(" ")