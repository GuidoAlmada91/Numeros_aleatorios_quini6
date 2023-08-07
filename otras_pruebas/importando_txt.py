f = open("prueba.txt", "w")

f.write("HOLAAA")
f.write("oTRA LINEA")

f.close()

f = open("atajos_teclado.txt", "r")

texto = f.read()
print(texto)


