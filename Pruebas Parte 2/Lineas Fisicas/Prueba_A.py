import Analizador_De_Codigo as LOC

class PruebaDeCodigo:
    
    def __init__(self):
        """
        Constructor que ejecuta todos los tests.
        """
        self.testComentarios()
        self.testDeclaraciones()
        self.testImportaciones()
        self.testLogicas()
        self.testCompleto()

    def testComentarios(self):
        """
        Este test contiene únicamente comentarios (una sola línea y múltiples) 
        y líneas vacías, se espera que el analizador no detecte ninguna de estas líneas.
        
        Salida esperada: 
        Líneas físicas = 0
        """
        print('Test de Comentarios')
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
        Este test contiene declaraciones de una sola línea y múltiples.
        
        Salida esperada:
        Líneas físicas = 14
        """
        print('Test de Declaraciones')
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
        Este test contiene únicamente importaciones de librerías.
        
        Salida esperada:
        Líneas físicas = 4
        """
        print('Test de Importaciones')
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
        Este test contiene un conjunto de operaciones lógicas
        y declaraciones.

        Salida esperada:
        Líneas físicas = 12
        """
        print('Test de Lógicas')
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
        Este test contiene el contenido de todos los tests anteriores.
        La salida debe ser la suma de todas las líneas físicas de los tests anteriores.
        
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

# Ejecutamos las pruebas
PruebaDeCodigo()
