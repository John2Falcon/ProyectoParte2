"""
Analizador de líneas de código en Python.

Cuenta:
- Líneas físicas totales.
- Líneas de cada clase.
- Métodos por clase.
- Métodos fuera de clases.
"""

class AnalizadorDeCodigo:
    def __init__(self, ruta_del_archivo):
        """
        Inicializa el analizador con la ruta del archivo.

        Args:
            ruta_del_archivo (str): Ruta del archivo a analizar.
        """
        self.ruta_del_archivo = ruta_del_archivo
        self.lineas_fisicas = 0
        self.lineas_logicas = 0
        self.clases = {}
        self.metodos_fuera_clases = []
        self.palabras_clave_logicas = ['if', 'for', 'while', 
                                       'def', 'class', 'try', 'with']

    def analizar_archivo(self):
        """
        Analiza un archivo fuente para contar líneas físicas, clases y métodos.
        """
        comentario_bloque = False
        clase_actual = None  # Almacena la clase en la que estamos actualmente
        indentacion_clase = None  # Almacena la indentación de la clase actual
        self.error = False  # Indicador de error
        self.error_mensaje = ""  # Mensaje de error


        try:
            with open(self.ruta_del_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea_sin_espacios = linea.strip()

                    # Manejo de comentarios en bloque
                    if '"""' in linea_sin_espacios or "'''" in linea_sin_espacios:
                        if linea_sin_espacios.count('"""') == 2 or linea_sin_espacios.count("'''") == 2:
                            continue
                        comentario_bloque = not comentario_bloque
                        continue
                    if comentario_bloque or not linea_sin_espacios or linea_sin_espacios.startswith('#'):
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

                    # Sumar líneas a la clase actual si existe
                    if clase_actual:
                        indentacion_actual = len(linea) - len(linea.lstrip())
                        if indentacion_actual > indentacion_clase:
                            self.clases[clase_actual]['lineas'] += 1
                        else:
                            clase_actual = None  # Salimos del contexto de la clase

        except FileNotFoundError as e:
            self.error = True
            self.error_mensaje = f"Archivo no encontrado: {e}"
        except IOError as e:
            self.error = True
            self.error_mensaje = f"Error de E/S: {e}"
        except UnicodeDecodeError as e:
            self.error = True
            self.error_mensaje = f"Error de codificación: {e}"

    def informe(self):
        """
        Retorna un resumen tabular del análisis del archivo.

        Retorna:
            Estadísticas generales, por clase y métodos fuera de clases.
        """
        print("-" * 60)
        print(f"{'Programa:':<10} {self.ruta_del_archivo}\n")
        print(f"{'LOC Físicas:':<20} {self.lineas_fisicas}")
        print(f"{'LOC Lógicas:':<20} {self.lineas_logicas}\n")

        print("Estadísticas por clase:")
        for clase, datos in self.clases.items():
            print(f"  Clase '{clase}': {datos['lineas']} líneas, {datos['metodos']} métodos")

        print("\nMétodos fuera de clases:")
        if self.metodos_fuera_clases:
            for metodo in self.metodos_fuera_clases:
                print(f"  - {metodo}")
        else:
            print("  Ningún método fuera de clases.")
        print("-" * 60)


if __name__ == "__main__":
    ruta_del_archivo = 'Lineas Fisicas\Test\Comentarios.py'
    analizador = AnalizadorDeCodigo(ruta_del_archivo)
    analizador.analizar_archivo()
    analizador.informe()
