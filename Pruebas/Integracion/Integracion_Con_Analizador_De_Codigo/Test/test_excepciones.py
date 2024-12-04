class ManejoExcepciones:
    def metodo(self):
        try:
            with open("archivo.txt", "r") as f:
                contenido = f.read()
        except FileNotFoundError:
            print("Archivo no encontrado")
