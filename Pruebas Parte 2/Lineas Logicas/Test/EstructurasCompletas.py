# Código para evaluar estructuras completas

# Estructura `if`
x = 10
if x > 5:  # Cuenta como línea lógica
    print("x es mayor que 5")  # No cuenta como línea lógica

# Estructura `for`
numeros = [1, 2, 3]
for n in numeros:  # Cuenta como línea lógica
    print(n)  # No cuenta como línea lógica

# Estructura `while`
contador = 0
while contador < 5:  # Cuenta como línea lógica
    contador += 1  # No cuenta como línea lógica

# Estructura `def`
def suma(a, b):  # Cuenta como línea lógica
    return a + b  # No cuenta como línea lógica

# Estructura `class`
class Persona:  # Cuenta como línea lógica
    # Atributos de la clase, sin usar `def` para métodos
    nombre = ""  # No cuenta como línea lógica
    edad = 0  # No cuenta como línea lógica

    # Inicialización directa de atributos (sin `def`)
    nombre = "Juan"  # No cuenta como línea lógica
    edad = 30  # No cuenta como línea lógica

# Estructura `try`
try:  # Cuenta como línea lógica
    resultado = 10 / 2  # No cuenta como línea lógica
    print("Error: División por cero")  # No cuenta como línea lógica

# Estructura `with`
with open("archivo.txt", "r") as archivo:  # Cuenta como línea lógica
    contenido = archivo.read()  # No cuenta como línea lógica
