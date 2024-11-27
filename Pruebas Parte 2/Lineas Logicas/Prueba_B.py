import Analizador_De_Codigo as LOC

class PruebaDeCodigo:

    def __init__(self):
        """
        Constructor de la clase. Llama a los métodos de prueba relacionados con las líneas físicas.
        """
        self.testComentarios()
        self.testDeclaraciones()
        self.testImportaciones()
        self.testLogicas()
        self.testCompleto()

    def testComentarios(self):
        """
        Este test evalúa un archivo con comentarios y líneas vacías.

        Salida esperada:
        Líneas físicas = 0
        """
        print('Test Comentarios')
        ruta = 'Test/Comentarios.py'
        lineas_fisicas_esperadas = 0

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testDeclaraciones(self):
        """
        Este test evalúa un archivo con declaraciones de una sola línea y múltiples.

        Salida esperada:
        Líneas físicas = 14
        """
        print('Test Declaraciones')
        ruta = 'Test/Declaraciones.py'
        lineas_fisicas_esperadas = 14

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testImportaciones(self):
        """
        Este test evalúa un archivo con importaciones de librerías.

        Salida esperada:
        Líneas físicas = 4
        """
        print('Test Importaciones')
        ruta = 'Test/Imports.py'
        lineas_fisicas_esperadas = 4

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testLogicas(self):
        """
        Este test evalúa un archivo con estructuras lógicas y declaraciones.

        Salida esperada:
        Líneas físicas = 12
        """
        print('Test Logicas')
        ruta = 'Test/Logicas.py'
        lineas_fisicas_esperadas = 12

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def testCompleto(self):
        """
        Este test evalúa un archivo que contiene todos los casos anteriores, sumando todas las líneas físicas.

        Salida esperada:
        Líneas físicas = 30
        """
        print('Test Completo')
        ruta = 'Test/Completo.py'
        lineas_fisicas_esperadas = 30

        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print(f'Resultado esperado {lineas_fisicas_esperadas}, resultado obtenido {analizador.lineas_fisicas}')

        if lineas_fisicas_esperadas == analizador.lineas_fisicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

# Ejecutar las pruebas
PruebaDeCodigo()
