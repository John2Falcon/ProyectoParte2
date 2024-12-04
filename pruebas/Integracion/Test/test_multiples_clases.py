""""
Prueba de comentarios para probar 
el analizador estructural y contar correctamente
las clases y metodos, lineas logicas y fisicas y lineas dentro
de las clases.
"""
class IF:
    # Estructura `if`
    def operacion():
        x = 10
        if x > 5:  # Cuenta como línea lógica
            print("x es mayor que 5")  # No cuenta como línea lógica
class FOR:
    # Estructura `for`
    numeros = [1, 2, 3]
    for n in numeros:  # Cuenta como línea lógica
        print(n)  # No cuenta como línea lógica

class While:
    # Estructura `while`
    contador = 0
    while contador < 5:  # Cuenta como línea lógica
        contador += 1  # No cuenta como línea lógica
        
class DEF:
    # Estructura `def`
    def suma(a, b):  # Cuenta como línea lógica
        return a + b  # No cuenta como línea lógica


class Persona:  # Cuenta como línea lógica
    # Atributos de la clase, sin usar `def` para métodos
    nombre = ""  # No cuenta como línea lógica
    edad = 0  # No cuenta como línea lógica

    def personas():# Inicialización directa de atributos (sin `def`)
        nombre = "Juan"  # No cuenta como línea lógica
        edad = 30  # No cuenta como línea lógica
        return None

class TRY:
    # Estructura `try`
    def metodotry():
        try:
            resultado = 10 / 0  # Esta línea ejecuta el código dentro de try
        except ZeroDivisionError:  # Esta línea ejecuta el código dentro de except
            print("Error: División por cero")  # Esta línea es dentro del except, pero no cuenta como lógica
        
        
class WITH:
    # Estructura `with`
    with open("archivo.txt", "r") as archivo:  # Cuenta como línea lógica
        contenido = archivo.read()  # No cuenta como línea lógica
    
    def metodo_uno(self):
        return self.x

    def metodo_dos(self):
        return self.x * 2

  
