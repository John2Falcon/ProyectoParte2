import Analizador_De_Clases_Y_metodos as LOC

class PruebaDeCodigo:

    def __init__(self):
        """
        Constructor de la clase.
        Llama a los métodos de prueba relacionados con las líneas físicas dentro de clases.
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
        Test para comprobar el correcto conteo de líneas físicas dentro de una clase con 2 métodos y comentarios.
        """
        ruta = "./Test/test_2_metodos_con_comentarios.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["operaciones:"]["lineas"]

        print("\nTest de clase con 2 métodos con comentarios")
        print(f"Resultado esperado líneas dentro de la clase: 4, resultado obtenido: {lineas_clase}")

        if lineas_clase == 4:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_3_metodos(self):
        """
        Test para validar el correcto conteo de líneas físicas dentro de una clase con 3 métodos.
        """
        ruta = "./Test/test_clase_3metodos.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["clase:"]["lineas"]

        print("\nTest clase con 3 métodos")
        print(f"Resultado esperado líneas dentro de la clase: 6, resultado obtenido: {lineas_clase}")

        if lineas_clase == 6:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_con_ciclos(self):
        """
        Test para validar el correcto conteo de líneas físicas dentro de una clase que posee ciclos.
        """
        ruta = "./Test/test_clase_con_ciclos.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["CICLOS:"]["lineas"]

        print("\nTest de clase con ciclos")
        print(f"Resultado esperado líneas dentro de la clase: 6, resultado obtenido: {lineas_clase}")

        if lineas_clase == 6:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_declaraciones(self):
        """
        Test para contar líneas físicas dentro de una clase sin métodos.
        """
        ruta = "./Test/test_clase_declaraciones.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["declaraciones:"]["lineas"]

        print("\nTest de clase con declaraciones")
        print(f"Resultado esperado líneas dentro de la clase: 10, resultado obtenido: {lineas_clase}")

        if lineas_clase == 10:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_clase_metodos_codigo(self):
        """
        Test para validar el conteo correcto de líneas físicas dentro de una clase con métodos y código.
        """
        ruta = "./Test/test_clase_metodos_y_codigo.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["Operaciones:"]["lineas"]

        print("\nTest de clase con métodos y código")
        print(f"Resultado esperado líneas dentro de la clase: 12, resultado obtenido: {lineas_clase}")

        if lineas_clase == 12:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_condicionales_en_clase(self):
        """
        Verificar el correcto conteo de líneas físicas dentro de una clase con condicionales.
        """
        ruta = "./Test/test_con_If.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["condicionales:"]["lineas"]

        print("\nTest de clase con condicionales")
        print(f"Resultado esperado líneas dentro de la clase: 7, resultado obtenido: {lineas_clase}")

        if lineas_clase == 7:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_con_manejo_errore(self):
        """
        Verifica el conteo correcto de líneas físicas dentro de una clase que maneja errores.
        """
        ruta = "./Test/test_con_Try.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["TRY:"]["lineas"]

        print("\nTest con manejo de errores")
        print(f"Resultado esperado líneas dentro de la clase: 4, resultado obtenido: {lineas_clase}")

        if lineas_clase == 4:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_con_manejo_de_archivos(self):
        """
        Test para verificar el conteo correcto de líneas físicas dentro de una clase que maneja archivos.
        """
        ruta = "./Test/test_con_with.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        lineas_clase = analizador.clases["With:"]["lineas"]

        print("\nTest con manejo de archivos")
        print(f"Resultado esperado líneas dentro de la clase: 5, resultado obtenido: {lineas_clase}")

        if lineas_clase == 5:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_solo_clases(self):
        """
        Test para verificar el conteo de líneas físicas dentro de clases sin código adicional.
        """
        ruta = "./Test/test_Solo_classes.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()

        print("\nTest de solo clases sin código extra")
        print(f"Resultado esperado: 2 clases, resultado obtenido: {len(analizador.clases)}")

        if len(analizador.clases) == 2:
            print('--Aprobado--\n')
        else:
            print('--Rechazado--\n')

    def test_estructuas_completas(self):
        """
        Test para validar todo lo probado anteriormente.
        """
        ruta = "./Test/test_Estructuras_Completas.py"
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()
        valores_esperados = {
            'IF:': {'lineas': 3},
            'FOR:': {'lineas': 3},
            'While:': {'lineas': 3},
            'DEF:': {'lineas': 2},
            'Persona:': {'lineas': 4},
            'TRY:': {'lineas': 4},
            'WITH:': {'lineas': 2}
        }

        print("\nTest con todo lo anterior")

        for clase, detalles in analizador.clases.items():
            lineas_obtenidas = detalles['lineas']
            lineas_esperadas = valores_esperados.get(clase, {}).get('lineas', -1)

            if lineas_obtenidas == lineas_esperadas:
                print(f"Clase {clase}: Validación exitosa.")
            else:
                print(f"Clase {clase}: Error. Esperado {lineas_esperadas} líneas, pero se obtuvo {lineas_obtenidas}.")

# Ejecutar las pruebas
PruebaDeCodigo()
