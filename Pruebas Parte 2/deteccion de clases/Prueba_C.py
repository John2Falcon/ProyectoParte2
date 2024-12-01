import Analizador_De_Codigo as LOC

class PruebaDeCodigo:

    def __init__(self):
        """
        Constructor que ejecuta todos los tests.
        """
        self.test_detectar_clases_y_metodos()
        self.test_codigo_fuera_de_clases()
        self.test_verificar_poo()
        self.test_archivo_inexistente()
        self.test_analisis_integral()

    def test_detectar_clases_y_metodos(self):
        ruta = "./Test/test_archivo_clases.py"
        with open(ruta, "w") as f:
            f.write("class MiClase:\n")  # Detecta 1 clase
            f.write("\tdef metodo1(self):\n")  # Detecta 1 método
            f.write("\t\tpass\n")  # No cuenta como método

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        assert "MiClase:" in analizador.clases
        assert analizador.clases["MiClase:"]["metodos"] == 1  # Verifica 1 método

    def test_codigo_fuera_de_clases(self):
        ruta = "./Test/test_archivo_fuera.py"
        with open(ruta, "w") as f:
            f.write("print('Hola mundo')\n")  # Código fuera de clase
            f.write("class MiClase:\n")
            f.write("    def metodo1(self):\n")
            f.write("        pass\n")

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        assert len(analizador.codigo_fuera_clases) == 1
        assert analizador.codigo_fuera_clases[0] == "print('Hola mundo')"
    
    def test_verificar_poo(self):
        ruta = "./Test/test_archivo_poo.py"
        with open(ruta, "w") as f:
            f.write("def funcion():\n")  # Método fuera de clase
            f.write("    pass\n")

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        try:
            analizador.verificar_poo()
            assert False  # Si no falla, hay un error
        except SystemExit as e:
            assert e.code == 1  # Salida con código de error
    
    def test_archivo_inexistente(self):
        ruta = "./Test/archivo_no_existente.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        try:
            analizador.analizar_archivo()
            assert False  # Si no lanza excepción, hay error
        except SystemExit as e:
            assert e.code == 1  # Código de error esperado
    
    def test_analisis_integral(self):
        ruta = "./Test/test_archivo_integral.py"
        with open(ruta, "w") as f:
            f.write("class MiClase:\n")
            f.write("    def metodo1(self):\n")
            f.write("        pass\n")
            f.write("print('Hola mundo')\n")  # Código fuera de clase
            f.write("print('Hola mundo')\n")  # Código fuera de clase

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        assert analizador.lineas_fisicas == 5
        assert analizador.lineas_logicas == 2
        assert len(analizador.codigo_fuera_clases) == 1
        assert analizador.codigo_fuera_clases[0] == "print('Hola mundo')"

# Ejecutamos las pruebas
if __name__ == "__main__":
    PruebaDeCodigo()
