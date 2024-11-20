class AnalizadorDeCodigoDetallado:
    """
    Extiende el analizador anterior para contar LOC por clase y método.
    """

    def __init__(self, ruta_del_archivo):
        self.ruta_del_archivo = ruta_del_archivo
        self.lineas_totales = 0
        self.clases = {}

    def analizar_archivo(self):
        comentario_bloque = False
        clase_actual = None

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

                    # Línea válida (física)
                    self.lineas_totales += 1

                    # Detección de clases
                    if linea_sin_espacios.startswith("class "):
                        clase_actual = linea_sin_espacios.split()[1].split('(')[0]
                        self.clases[clase_actual] = {'metodos': 0, 'lineas': 0}
                    elif clase_actual and linea_sin_espacios.startswith("def "):
                        # Detección de métodos dentro de una clase
                        self.clases[clase_actual]['metodos'] += 1

                    # Incremento de líneas en la clase actual (si aplica)
                    if clase_actual:
                        self.clases[clase_actual]['lineas'] += 1

        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_del_archivo} no existe.")
        except IOError as e:
            print(f"Error al leer el archivo {self.ruta_del_archivo}: {e}")

    def informe(self):
        print("-" * 60)
        print("Clase          | Total Métodos | LOC Físicas por Clase")
        print("-" * 60)
        for clase, datos in self.clases.items():
            print(f"{clase:<14} | {datos['metodos']:<14} | {datos['lineas']:<22}")
        print("-" * 60)
        print(f"Total LOC físicas del programa: {self.lineas_totales}")
        print("-" * 60)


if __name__ == "__main__":
    ruta_del_archivo = './pruebas/Prueba_E.py'
    analizador = AnalizadorDeCodigoDetallado(ruta_del_archivo)
    analizador.analizar_archivo()
    analizador.informe()
