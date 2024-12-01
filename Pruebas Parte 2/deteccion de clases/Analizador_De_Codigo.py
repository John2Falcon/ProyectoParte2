import sys
class AnalizadorDeCodigo:
    def __init__(self, ruta_del_archivo):
        """
        Inicializa el analizador con la ruta del archivo.
        """
        self.ruta_del_archivo = ruta_del_archivo
        self.lineas_fisicas = 0
        self.lineas_logicas = 0
        self.clases = {}
        self.metodos_fuera_clases = []
        self.codigo_fuera_clases = []  # Almacena líneas de código fuera de clases
        self.palabras_clave_logicas = ['if', 'for', 'while', 
                                       'def', 'class', 'try', 'with']

    def analizar_archivo(self):
        """
        Analiza un archivo fuente para contar líneas físicas, clases y métodos.
        Verifica si el script sigue estrictamente el paradigma POO.
        """
        comentario_bloque = False
        clase_actual = None  # Almacena la clase en la que estamos actualmente
        indentacion_clase = None  # Almacena la indentación de la clase actual

        try:
            with open(self.ruta_del_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea_sin_espacios = linea.strip()

                    # Manejo de comentarios en bloque
                    if '"""' in linea_sin_espacios or "'''" in linea_sin_espacios:
                        if linea_sin_espacios.count('"""') == 2 \
                            or linea_sin_espacios.count("'''") == 2:
                            continue
                        comentario_bloque = not comentario_bloque
                        continue

                    if comentario_bloque or not linea_sin_espacios \
                        or linea_sin_espacios.startswith('#'):
                        continue

                    self.lineas_fisicas += 1
                    primera_palabra = linea_sin_espacios.split()[0]
                    if primera_palabra.rstrip(':') in self.palabras_clave_logicas:
                        self.lineas_logicas += 1

                    # Detección de clases
                    if primera_palabra == 'class':
                        clase_actual = linea_sin_espacios.split()[1].split('(')[0]
                        self.clases[clase_actual] = {'lineas': 0, 'metodos': 0}
                        indentacion_clase = len(linea) - len(linea.lstrip())
                        continue

                    # Detección de métodos
                    if primera_palabra == 'def':
                        metodo = linea_sin_espacios.split()[1].split('(')[0]
                        indentacion_metodo = len(linea) - len(linea.lstrip())

                        if clase_actual and indentacion_metodo > indentacion_clase:
                            self.clases[clase_actual]['metodos'] += 1
                        else:
                            self.metodos_fuera_clases.append(metodo)

                    # Detección de código fuera de clases
                    if not clase_actual:
                        if primera_palabra not in ['import', 'from', 'class', 'def']:
                            self.codigo_fuera_clases.append(linea_sin_espacios)

                    # Sumar líneas a la clase actual si existe
                    if clase_actual:
                        indentacion_actual = len(linea) - len(linea.lstrip())
                        if indentacion_actual > indentacion_clase:
                            self.clases[clase_actual]['lineas'] += 1
                        else:
                            clase_actual = None  # Salimos del contexto de la clase

        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
            sys.exit(1)
        except IOError as e:
            print(f"Error de E/S: {e}")
            sys.exit(1)
        except UnicodeDecodeError as e:
            print(f"Error de codificación: {e}")
            sys.exit(1)

    def verificar_poo(self):
        """
        Verifica si el script sigue estrictamente el paradigma POO.
        Si no lo cumple, muestra un mensaje y sale del programa.
        """
        if self.metodos_fuera_clases or self.codigo_fuera_clases:
            print("\nERROR: El archivo **NO** sigue estrictamente el paradigma POO.")
            print("Causas detectadas:")
            if self.metodos_fuera_clases:
                print(f"  - Métodos fuera de clases: {', '.join(self.metodos_fuera_clases)}")
            if self.codigo_fuera_clases:
                print("  - Código ejecutable fuera de clases:")
                for linea in self.codigo_fuera_clases:
                    print(f"    {linea}")
            sys.exit(1)

    def informe(self):
        """
        Muestra un informe del análisis y verifica si es POO.
        """
        print("-" * 60)
        print(f"{'Programa:':<10} {self.ruta_del_archivo}\n")
        print(f"{'LOC Físicas:':<20} {self.lineas_fisicas}")
        print(f"{'LOC Lógicas:':<20} {self.lineas_logicas}\n")

        print("Estadísticas por clase:")
        for clase, datos in self.clases.items():
            print(f"  Clase '{clase}': {datos['lineas']} líneas, {datos['metodos']} métodos")
        print("-" * 60)

if __name__ == "__main__":
    ruta_del_archivo = './Test/test_archivo_integral.py'
    analizador = AnalizadorDeCodigo(ruta_del_archivo)
    analizador.analizar_archivo()
    analizador.verificar_poo()  # Verifica POO
    analizador.informe()        # Muestra el informe si cumple con POO
