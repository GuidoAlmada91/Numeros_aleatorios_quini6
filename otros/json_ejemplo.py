import json
data = {}
data["clientes"] = []

data["clientes"].append({"Nombre" : "Guido", "Apellido" : "Almada", "Edad" : "32"})
data["clientes"].append({"Nombre" : "Juan", "Apellido" : "Bausela", "Edad" : "26"})

with open("mi_archivojson.json", "w") as file:
    json.dump(data, file, indent=4)