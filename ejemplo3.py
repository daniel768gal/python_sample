class Book:
    __slots__ = ['title', 'author'] #limita los atributos que se agregan
    def __init__(self, title, author):
        self.title = title
        self. author = author

book = Book(title="PythonBook", author="Guido")
book.price = 3000
print(book.price)