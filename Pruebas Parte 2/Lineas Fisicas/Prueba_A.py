import Analizador_De_Codigo as LOC

class PruebaDeCodigo:

    def __init__(self):
        """
        Constructor de la clase. 
        Llama a los métodos de prueba relacionados con las líneas logicas.
        """

        self.test_2_metodos_con_comentarios()
        self.test_clase_3_metodos()
        self.test_clase_con_ciclos()
        self.test_clase_declaraciones()
        self.test_clase_metodos_codigo()
        self.test_condicionales_en_clase()
        self.test_con_manejo_errore()
        self.test_con_manejo_de_archivos()
        self.test_solo_clases()
        self.test_estructuas_completas()

    def test_2_metodos_con_comentarios(self):
        """
        test para comprobar el correcto conteo de LOC fisicas y lineas dentro de las clases
        con una clase con 2 comentarios
        """
        ruta = "./Test/test_2_metodos_con_comentarios.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["operaciones:"]["lineas"]
        print("test de clase con 2 metodos con comentarios")
        print(f'\nResultado esperado {5}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {4}, resultado obtenido: {lineas_clase}")

        if 5 == analizador.lineas_fisicas and lineas_clase == 4:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_3_metodos(self):
        """
        test para validar el correcto conteo de LOC fisicas de solo una clase
        con 3 metodos
        """
        ruta = "./Test/test_clase_3metodos.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["clase:"]["lineas"]
        print("test clase con solo 3 metodos")
        print(f'Resultado esperado {7}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {6}, resultado obtenido: {lineas_clase}")

        if 7 == analizador.lineas_fisicas and lineas_clase == 6:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
    
    def test_clase_con_ciclos(self):
        """
        test para validar el correcto conteo de Loc fisicas en  
         una clase que posee  ciclos
        """
        ruta = "./Test/test_clase_con_ciclos.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["CICLOS:"]["lineas"]

        print("test de clase con 2 metodos con comentarios")
        print(f'\nResultado esperado {7}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {6}, resultado obtenido: {lineas_clase}")

        if 7 == analizador.lineas_fisicas and lineas_clase == 6:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    
    def test_clase_declaraciones(self):
        """
        test para contar lineas fisicas dentro de una clase sin metodos.
        """
        ruta = "./Test/test_clase_declaraciones.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["declaraciones:"]["lineas"]

        print("Test de clase con declaraciones")
        print(f'Resultado esperado LOC fisicas {11}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {10}, resultado obtenido: {lineas_clase}")

        if 11 == analizador.lineas_fisicas and 10 == lineas_clase:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_clase_metodos_codigo(self):
        """
        test para validar el conteo correcto de loc fisicas de una clase
        con metodos y codigo dentro de la misma clase.
        """
        ruta = "./Test/test_clase_metodos_y_codigo.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["Operaciones:"]["lineas"]
        
        print("Test de clase con métodos y código")
        print(f'Resultado esperado LOC fisicas {13}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {12}, resultado obtenido: {lineas_clase}")

        if  analizador.lineas_fisicas == 13 and lineas_clase == 12:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_condicionales_en_clase(self):
        """
        verificar el correcto conteo de loc fisicas con condicionales if 
        en una clase
        """
        ruta = "./Test/test_con_If.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["condicionales:"]["lineas"]

        print("Test de clases con condicionales")
        print(f'Resultado esperado LOC fisicas {8}, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {7}, resultado obtenido: {lineas_clase}")

        if  analizador.lineas_fisicas == 8 and lineas_clase == 7:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
    
    def test_con_manejo_errore(self):
        """
        verifica que se maneje correctamente el conteo de lineas fisicas con codigo manejador de errores
        en una clase
        """
        ruta = "./Test/test_con_Try.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["TRY:"]["lineas"]

        print("Test con manejo de errores")
        print(f'Resultado esperado {5} lineas fisicas , resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {4}, resultado obtenido: {lineas_clase}")

        if analizador.lineas_fisicas == 5 and lineas_clase == 4 :
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_con_manejo_de_archivos(self):
        """
        test para verificar el conteo correcto de lineas fisicas en una clase 
        que contiene codigo de manejo de archivos
        """
        ruta = "./Test/test_con_with.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        lineas_clase = analizador.clases["With:"]["lineas"]

        print("Test con manejo de archivos")
        print(f'Resultado esperado {6} lineas fisicas en la clase, resultado obtenido {analizador.lineas_fisicas}')
        print(f"Resultado esperado lineas dentro de la clase : {5}, resultado obtenido: {lineas_clase}")
        if analizador.lineas_fisicas == 6 and lineas_clase == 5 :
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_solo_clases(self):
        """
        test para verificar que se cuentan las clases y las lineas fisicas totales.
        """
        ruta = "./Test/test_Solo_classes.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()

        print("Test de solo clases sin codigo extra")
        print(f'Resultado esperado {4} lineas fisicas en la clase, resultado obtenido {analizador.lineas_fisicas}')
        print(f'Resultado esperado 2 clases , resultado obtenido {len(analizador.clases)}')
        
        if  len(analizador.clases) == 2 and analizador.lineas_fisicas == 4:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_estructuas_completas(self):
        """ 
        test para validar todo lo probado anterior.
        """
        ruta = "./Test/test_Estructuras_Completas.py"
        analizador = LOC.AnalizadorDeCodigo(ruta)
        analizador.analizar_archivo()
        valores_esperados = {
            'IF:': {'lineas': 3, 'metodos': 0},
            'FOR:': {'lineas': 3, 'metodos': 0},
            'While:': {'lineas': 3, 'metodos': 0},
            'DEF:': {'lineas': 2, 'metodos': 1},
            'Persona:': {'lineas': 4, 'metodos': 0},
            'TRY:': {'lineas': 4, 'metodos': 0},
            'WITH:': {'lineas': 2, 'metodos': 0}
        }

        print("Test con todo lo anterior")
        print(f"loc fisicas esperadas: 28, resultado {analizador.lineas_fisicas}")
        print(f"loc logicas esperadas: 13, resultado {analizador.lineas_logicas}")
        print(f"clases esperadas: 7, resultado {len(analizador.clases)}\n")

        # Validar las clases
        for clase, detalles in analizador.clases.items():
            lineas_obtenidas = detalles['lineas']
            metodos_obtenidos = detalles['metodos']
            
            # Obtener valores esperados
            lineas_esperadas = valores_esperados.get(clase, {}).get('lineas', -1)
            metodos_esperados = valores_esperados.get(clase, {}).get('metodos', -1)
            
            # Validación
            if lineas_obtenidas == lineas_esperadas and metodos_obtenidos == metodos_esperados:
                print(f"Clase {clase}: Validación exitosa.")
            else:
                print(f"Clase {clase}: Error. Esperado {lineas_esperadas} líneas y {metodos_esperados} métodos, "
                    f"pero se obtuvo {lineas_obtenidas} líneas y {metodos_obtenidos} métodos.")
                







        





    

# Ejecutar las pruebas
PruebaDeCodigo()

