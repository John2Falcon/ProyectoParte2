# Este archivo contiene un bloque `try` con `except`
# Esta línea es un comentario y no se debe contar
class TRY:
    try:
        resultado = 10 / 0  # Esta línea ejecuta el código dentro de try
    except ZeroDivisionError:  # Esta línea ejecuta el código dentro de except
        print("Error: División por cero")  # Esta línea es dentro del except, pero no cuenta como lógica
