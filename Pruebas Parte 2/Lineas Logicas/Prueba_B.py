import Analizador_De_Clases_Y_metodos as LOC

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
        test para comprobar el correcto conteo de LOC logicas con dos metodos con comentarios
        """
        ruta = "./Test/test_2_metodos_con_comentarios.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("test de 2 metodos con comentarios")
        print(f'\nResultado esperado {3}, resultado obtenido {analizador.lineas_logicas}')

        if 3 == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_3_metodos(self):
        """
        test para validar el correcto conteo de LOC logicas de solo una clase
        con 3 metodos
        """
        ruta = "./Test/test_clase_3metodos.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("test clase con solo 3 metodos")
        print(f'Resultado esperado {4}, resultado obtenido {analizador.lineas_logicas}')

        if 4 == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
    
    def test_clase_con_ciclos(self):
        """
        test para validar el correcto conteo de Loc logicas con ciclos

        """
        ruta = "./Test/test_clase_con_ciclos.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()

        print("test de clases con ciclos")
        print(f'Resultado esperado {3}, resultado obtenido {analizador.lineas_logicas}')

        if 3 == analizador.lineas_logicas:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
    
    def test_clase_declaraciones(self):
        """
        test para contar lineas dentro de una clase sin metodos.
        """
        ruta = "./Test/test_clase_declaraciones.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test de clase con declaraciones")
        print(f'Resultado esperado LOC logicas {1}, resultado obtenido {analizador.lineas_logicas}')

        if 1 == analizador.lineas_logicas :
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_clase_metodos_codigo(self):
        """
        test para validar el conteo correcto de loc logicas de una clase
        con metodos y codigo dentro de la misma clase.
        """
        ruta = "./Test/test_clase_metodos_y_codigo.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test de clase L")
        print(f'Resultado esperado LOC logicas {5}, resultado obtenido {analizador.lineas_logicas}')

        if  analizador.lineas_logicas == 5:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_condicionales_en_clase(self):
        """
        verificar el correcto conteo de loc logicas con condicionales if 
        """
        ruta = "./Test/test_con_If.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test de clases con condicionales")
        print(f'Resultado esperado LOC logicas {4}, resultado obtenido {analizador.lineas_logicas}')
      
        if  analizador.lineas_logicas == 4:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
    
    def test_con_manejo_errore(self):
        """
        verifica que se maneje correctamente el conteo con codigo manejador de errores
        de loc logicas

        """
        ruta = "./Test/test_con_Try.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test con manejo de errores")
        print(f'Resultado esperado {2} lineas en la clase, resultado obtenido {analizador.lineas_logicas}')

        if analizador.lineas_logicas == 2 :
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_con_manejo_de_archivos(self):
        """
        test para verificar el conteo correcto
        de loc logicas con codigo manejador de archivos
        """
        ruta = "./Test/test_con_with.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test con manejo de archivos")
        print(f'Resultado esperado {3} lineas en la clase, resultado obtenido {analizador.lineas_logicas}')

        if analizador.lineas_logicas == 3 :
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_solo_clases(self):
        """
        test para verificar que se cuentan las clases.
        """
        ruta = "./Test/test_Solo_classes.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        print("Test de solo clases sin codigo extra")
        print(f'Resultado esperado 2 clases MiClase , resultado obtenido {len(analizador.clases)}')

        if  len(analizador.clases) == 2:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')
        
    def test_estructuas_completas(self):
        """ 
        test para validar todo lo probado anterior.
        """
        ruta = "./Test/test_Estructuras_Completas.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
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
        print(f"loc logicas esperadas: 7, resultado {len(analizador.clases)}\n")

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

