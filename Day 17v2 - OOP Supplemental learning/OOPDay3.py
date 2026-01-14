class Book:

    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return (f"Title: {self.title}, Author: {self.author}, Year Published: {self.year}")
    
class EBook(Book):

    def __init__(self,title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def get_summary(self):
        return f"{super().get_summary()}, File Size: {self.file_size}"

Book1 = Book("stars", "Lay", "2026")

EBook1 = EBook("stars", "Spencer", "2026", "51255")

print(Book1.get_summary())
print(EBook1.get_summary())