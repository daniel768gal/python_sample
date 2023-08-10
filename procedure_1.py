#aplicacion de compras - orientado a objetos

class Grocery:  #Clase de producto
    def __init__(self, name, price):
        self.name = name
        self.price = price

#Configuracion de la clase de usuario
class User:
    def __init__(self, arg1, arg2=None, arg3=None):
        self.name = arg1
        self.address = arg2

#Configuracion de la clase de vendedor
class Seller(User):
    from shopping1 import ordenling_list
    def __init__(self, name, shop, address=None):
        super().__init__(name, address)
        self.shop = shop
        self.orders = []

    def ordered(self, order):
        self.orders.append(order)

    """def ordenling_list(self):
        #Mostrar lista de pedidos del comprador y en funcion de las compras del Comprador
        total = 0
        print("======== Listas de pedidos por cliente({}, {})=====".format(self.name, self.shop))
        for order in self.orders:
            print(f"Nombre del cliente: {order[0]}, cantidad de dinero: {order[1]}, fecha y hora: {order[2]}")
            total += order[1]

        print(f"----------importe total: {total}")
        print("=================================")"""

#Crear una clase de comprador
class Customer(User):
    total = 0
    from shopping1 import grocery_list, shopping_list

    def __init__(self, name, address):
        super().__init__(name, address)
        self.basket = []

    def shopping(self, groceries):
        import datetime
        #Empezar a comprar
        self.grocery_list(groceries)
        shopping_end = None
        while shopping_end != "yes":
            #Seleccion de productos
            print('Seleccion el numero de articulo')
            number = int(input())
            #Entrada de cantidad de producto
            print('Entrada de cantidad de producto')
            quantity = int(input())
            self.__entry(groceries[number], quantity)
            print('Quieres terminar de comprar? yes/no')
            shopping_end = input()

        self.shopping_list(self.basket)
        #Total pero calculado en shopping_list
        order = [self.name, self.total, datetime.datetime.now().strftime("%Y-%m-%d")]
        return order

    #Metodos privados a continuacion
    """def __grocery_list(self, groceries):
        print("------Lista de la Compra-------")
        for i, grocery in enumerate(groceries):
            print(f'{i}, {grocery.name}, {grocery.price}')"""

    def __entry(self, grocery, quantity):
        self.basket.append([grocery, quantity])

    """def __shopping_list(self, basket):
        print(f'===== lista de compra({self.name}/{self.address})')
        for grocery in basket:
            name = grocery[0].name
            price = grocery[0].price
            quantity = grocery[1]
            money = price * quantity
            print(f'nombre comercial (marca): {name}, volumen: {quantity}, cantidad de dinero: {money}')
            self.total += money
        print("---------importe total: {}".format(self.total))
        print('================================')"""


#Creacion de listas de productos
groceries = []
#Instanciar cada producto y almacenarlo en la matriz de productos
groceries = Grocery('platana', 300),\
            Grocery('pan', 500),\
            Grocery('leche de vaca', 230),\
            Grocery('huevo', 280),\
            Grocery('carne', 800),\
            Grocery('pescado', 500)

#Instanciacion de vendedor(Ichiro Takhashi, Tienda A)
ichiro = Seller("Ichiro Takahashi", "Tienda A")

#Instanciacion de comprador (Taro Yamada, Tokyo)
taro = Customer("Taro Yamada", "Tokyo")

#Lista de compra
order = taro.shopping(groceries)
ichiro.ordered(order)
ichiro.ordenling_list()


