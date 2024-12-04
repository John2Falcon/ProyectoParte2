import os
from unittest.mock import patch
from app import app

def prueba_integracion_app():
    # Configuración
    carpeta_prueba = './Test'
    archivo_prueba = 'test_Estructuras_Completas.py'
    ruta_archivo = os.path.join(carpeta_prueba, archivo_prueba)

    # Crear una carpeta y un archivo de prueba
    os.makedirs(carpeta_prueba, exist_ok=True)
    with open(ruta_archivo, 'w') as f:
        f.write("""
class MiClase:
    def metodo_1(self):
        pass

    def metodo_2(self):
        pass
""")

    # Simulación de las entradas del usuario
    entradas_mock = iter(["no"])  # Responder "no" directamente cuando se pregunte si desea continuar

    def mock_obtener_archivos():
        # Simular la entrada del usuario para elegir los archivos
        return [archivo_prueba]

    try:
        print("Ejecutando prueba de integración con app.py...")
        with patch('builtins.input', lambda _: next(entradas_mock)):  # Simula las respuestas del usuario
            aplicacion = app(carpeta=carpeta_prueba)
            aplicacion.obtener_archivos = mock_obtener_archivos  # Evita preguntar los nombres de archivos
            aplicacion.ejecutar()  # Ejecuta el flujo principal
        print("Prueba de integración: PASÓ")
    except Exception as e:
        print("Prueba de integración: FALLÓ")
        print(f"Error: {e}")

if __name__ == "__main__":
    prueba_integracion_app()
