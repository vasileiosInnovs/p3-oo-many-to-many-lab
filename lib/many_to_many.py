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
    pass