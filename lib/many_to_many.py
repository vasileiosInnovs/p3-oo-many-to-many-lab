class Author:
    all = []

    def __init__(self, name=""):
        self.name = name
        Author.all.append(self)


class Book:
    all = []

    def __init__(self, title=""):
        self.title = title
        Book.all.append(self)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self. author = author
        self.book = book
        self.date = date
        self.royalties = royalties        
        Contract.all.append(self)