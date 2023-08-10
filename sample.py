"""posts = []
while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Puntos de evaluacion y comentarios')
    print('2: Comprueba los resultados obtenidos hasta ahora')
    print("3: Introduzca una puntuación utilizando un número del 1 al 5. Introduzca '6' para salir")
    num = input()
    point = input()
    if point.isdecimal():
        point = int(point)
        if point == 6:
            print("Terminacion")
            break
        elif 1 <= point <= 5:
            print("Introduzca sus comentarios")
            comment = input()
            post = f'punto: {point}. Comentario: {comment}'
            file = open("data.txt", 'a')
            file.write(f'{post} \n')
            file.close()
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
            ##posts.extend(post.items())
        else:
            print("introduzca un numero")
    else:
        print("Introduzca un numero")"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return "come"
    
    def move(self):
        return "Moverse libremente"
    
    def voice(self):
        return "hable"

class Dog(Animal):
    def voice(self):
        voice = super().voice()
        return "{}: bow bow".format(voice)
    
    def shake_tall(self):
        return "mover la cola"

class Cat(Animal):
    def voice(self):
        voice = super().voice()
        return "{}: miau".format(voice)
    
    def scratch(self):
        return "rayar"
    
pochi = Dog("pequeño caracol de concha espiral (especialmente un caracol de estanque)")
mike = Cat("concha de tortuga (patrón)")

"""for method in dir(mike):
    if callable(getattr(mike, str(method))):
        print(method)"""

print(pochi.voice())
print(mike.voice())






