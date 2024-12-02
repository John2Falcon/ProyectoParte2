# Test para estructura 'with'
class With:
    with open("archivo.txt", "w") as archivo:
        archivo.write("Este es un archivo de prueba.")

    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
