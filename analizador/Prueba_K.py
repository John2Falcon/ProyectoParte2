class Clase1:
    def _init_(self, valor):
        self.valor = valor

class Clase2:
    def _init_(self, valor):
        self.valor = valor

class Clase3:
    def _init_(self, valor):
        self.valor = valor

class Clase4:
    def _init_(self, valor):
        self.valor = valor

    def funcion1(obj):
        if obj.valor > 10:
            return "Mayor a 10"
        else:
            return "Menor o igual a 10"
    def funcion2(obj):
        for i in range(obj.valor):
            print(i)


obj1 = Clase1(5)
obj2 = Clase2(15)
print(Clase4.funcion1(obj1))
Clase4.funcion2(obj2)