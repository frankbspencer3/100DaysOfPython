class Book:

    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

Book1 = Book("stars", "Lay", "2026")

print(Book1)
print(Book1.title)
print(Book1.author)
print(Book1.year_published)
