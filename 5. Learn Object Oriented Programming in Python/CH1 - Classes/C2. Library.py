class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        

    def remove_book(self, book):
        for book1 in self.books:
            if book.title == book1.title and book.author == book1.author:
                self.books.remove(book1)

    def search_books(self, search_string):
        search = []
        for book in self.books:
            if (search_string.lower() in book.title.lower()) or (search_string.lower() in book.author.lower()):
                search.append(book)
        return search
