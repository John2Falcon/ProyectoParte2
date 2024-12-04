import Analizador_De_Clases_Y_metodos as LOC

class PruebaDeIntegracion:
    """
    Clase para probar la integración de los módulos de análisis de clases y métodos.
    Objetivo: Validar las funcionalidades de ambos módulos en conjunto.
    """
    def __init__(self):
        """
        Constructor de la clase.
        Llama a los métodos de prueba relacionados.
        """
        self.ejecutar_pruebas()

    def ejecutar_pruebas(self):
        """
        Ejecuta todas las pruebas de integración.
        """
        self.test_integracion_1()
        self.test_integracion_2()
        self.test_integracion_3()

    def test_integracion_1(self):
        """
        Prueba de integración que valida las salidas del analizador estructural en un archivo de prueba.
        """
        ruta = "./Test/test_clases_varios_metodos.py"

        print("\nIniciando prueba de integración 1...")
        print(f"Archivo a analizar: {ruta}")

        # Crear instancia del analizador
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()

        # Resultados esperados
        lineas_fisicas_esperadas = 7
        lineas_logicas_esperadas = 4
        total_de_clases_esperadas = 1
        valores_esperados = {
            'MiClaseCompleja:': {'lineas': 6, 'metodos': 3},
        }

        # Validar resultados
        print(f"Validando líneas físicas...")
        assert analizador.lineas_fisicas == lineas_fisicas_esperadas, \
            f"Error: Se esperaban {lineas_fisicas_esperadas} líneas físicas, pero se obtuvieron {analizador.lineas_fisicas}."

        print(f"Validando líneas lógicas...")
        assert analizador.lineas_logicas == lineas_logicas_esperadas, \
            f"Error: Se esperaban {lineas_logicas_esperadas} líneas lógicas, pero se obtuvieron {analizador.lineas_logicas}."

        print(f"Validando cantidad de clases...")
        assert len(analizador.clases) == total_de_clases_esperadas, \
            f"Error: Se esperaban {total_de_clases_esperadas} clases, pero se encontraron {len(analizador.clases)}."

        # Validar cada clase y sus detalles
        print(f"Validando detalles de clases y métodos...")
        for clase, detalles in analizador.clases.items():
            lineas_obtenidas = detalles['lineas']
            metodos_obtenidos = detalles['metodos']

            lineas_esperadas = valores_esperados.get(clase, {}).get('lineas', -1)
            metodos_esperados = valores_esperados.get(clase, {}).get('metodos', -1)

            assert lineas_obtenidas == lineas_esperadas, \
                f"Error en la clase {clase}. Se esperaban {lineas_esperadas} líneas, pero se obtuvieron {lineas_obtenidas}."

            assert metodos_obtenidos == metodos_esperados, \
                f"Error en la clase {clase}. Se esperaban {metodos_esperados} métodos, pero se obtuvieron {metodos_obtenidos}."

            print(f"Clase {clase}: Validación exitosa de líneas y métodos.")

        print("Prueba de integración 1 completada con éxito.\n")
    
    def test_integracion_2(self):
        """
        Prueba de integración que valida las salidas del analizador estructural en un archivo de prueba.
        """
        ruta = "./Test/test_excepciones.py"

        print("\nIniciando prueba de integración 2...")
        print(f"Archivo a analizar: {ruta}")

        # Crear instancia del analizador
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()

        # Resultados esperados
        lineas_fisicas_esperadas = 7
        lineas_logicas_esperadas = 4
        total_de_clases_esperadas = 1
        valores_esperados = {
            'ManejoExcepciones:': {'lineas': 6, 'metodos': 1},
        }

        # Validar resultados
        print(f"Validando líneas físicas...")
        assert analizador.lineas_fisicas == lineas_fisicas_esperadas, \
            f"Error: Se esperaban {lineas_fisicas_esperadas} líneas físicas, pero se obtuvieron {analizador.lineas_fisicas}."

        print(f"Validando líneas lógicas...")
        assert analizador.lineas_logicas == lineas_logicas_esperadas, \
            f"Error: Se esperaban {lineas_logicas_esperadas} líneas lógicas, pero se obtuvieron {analizador.lineas_logicas}."

        print(f"Validando cantidad de clases...")
        assert len(analizador.clases) == total_de_clases_esperadas, \
            f"Error: Se esperaban {total_de_clases_esperadas} clases, pero se encontraron {len(analizador.clases)}."

        # Validar cada clase y sus detalles
        print(f"Validando detalles de clases y métodos...")
        for clase, detalles in analizador.clases.items():
            lineas_obtenidas = detalles['lineas']
            metodos_obtenidos = detalles['metodos']

            lineas_esperadas = valores_esperados.get(clase, {}).get('lineas', -1)
            metodos_esperados = valores_esperados.get(clase, {}).get('metodos', -1)

            assert lineas_obtenidas == lineas_esperadas, \
                f"Error en la clase {clase}. Se esperaban {lineas_esperadas} líneas, pero se obtuvieron {lineas_obtenidas}."

            assert metodos_obtenidos == metodos_esperados, \
                f"Error en la clase {clase}. Se esperaban {metodos_esperados} métodos, pero se obtuvieron {metodos_obtenidos}."

            print(f"Clase {clase}: Validación exitosa de líneas y métodos.")

        print("Prueba de integración 2 completada con éxito.\n")

    def test_integracion_3(self):
        """
        Prueba de integración que valida las salidas del analizador estructural en un archivo de prueba.
        """
        ruta = "./Test/test_multiples_clases.py"

        print("\nIniciando prueba de integración 3...")
        print(f"Archivo a analizar: {ruta}")

        # Crear instancia del analizador
        analizador = LOC.AnalizadorEstructural(ruta)
        analizador.obtener_resultados()

        # Resultados esperados
        lineas_fisicas_esperadas = 36
        lineas_logicas_esperadas = 18
        total_de_clases_esperadas = 7
        valores_esperados = {
            'IF:': {'lineas': 4, 'metodos': 1},
            'FOR:': {'lineas': 3, 'metodos': 0},
            'While:': {'lineas': 3, 'metodos': 0},
            'DEF:': {'lineas': 2, 'metodos': 1},
            'Persona:': {'lineas': 6, 'metodos': 1},
            'TRY:': {'lineas': 5, 'metodos': 1},
            'WITH:': {'lineas': 6, 'metodos': 2}
        }

        # Validar resultados
        print(f"Validando líneas físicas...")
        assert analizador.lineas_fisicas == lineas_fisicas_esperadas, \
            f"Error: Se esperaban {lineas_fisicas_esperadas} líneas físicas, pero se obtuvieron {analizador.lineas_fisicas}."

        print(f"Validando líneas lógicas...")
        assert analizador.lineas_logicas == lineas_logicas_esperadas, \
            f"Error: Se esperaban {lineas_logicas_esperadas} líneas lógicas, pero se obtuvieron {analizador.lineas_logicas}."

        print(f"Validando cantidad de clases...")
        assert len(analizador.clases) == total_de_clases_esperadas, \
            f"Error: Se esperaban {total_de_clases_esperadas} clases, pero se encontraron {len(analizador.clases)}."

        # Validar cada clase y sus detalles
        print(f"Validando detalles de clases y métodos...")
        for clase, detalles in analizador.clases.items():
            lineas_obtenidas = detalles['lineas']
            metodos_obtenidos = detalles['metodos']

            lineas_esperadas = valores_esperados.get(clase, {}).get('lineas', -1)
            metodos_esperados = valores_esperados.get(clase, {}).get('metodos', -1)

            assert lineas_obtenidas == lineas_esperadas, \
                f"Error en la clase {clase}. Se esperaban {lineas_esperadas} líneas, pero se obtuvieron {lineas_obtenidas}."

            assert metodos_obtenidos == metodos_esperados, \
                f"Error en la clase {clase}. Se esperaban {metodos_esperados} métodos, pero se obtuvieron {metodos_obtenidos}."

            print(f"Clase {clase}: Validación exitosa de líneas y métodos.")

        print("Prueba de integración 3 completada con éxito.")


# Ejecutar las pruebas
if __name__ == "__main__":
    PruebaDeIntegracion()
