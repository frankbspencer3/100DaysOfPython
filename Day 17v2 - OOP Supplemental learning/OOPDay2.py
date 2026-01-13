class Book:

    def __init__ (self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_summary(self):
        return (f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}")

Book1 = Book("stars", "Lay", "2026")
print(Book1.get_summary())