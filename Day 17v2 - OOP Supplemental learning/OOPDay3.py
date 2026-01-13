class Book:

    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return (f"Title: {self.title}, Author: {self.author}, Year Published: {self.year}")
    
class EBook(Book):

    def __init__(self, file_size):
        Book.__init__(self)
        self.file_size = file_size

    def get_summary(self):
        return super().get_summary()

Book1 = Book("stars", "Lay", "2026")

EBook1 = EBook.Book1("10256")
print(EBook)