from datetime import datetime

class Author:
    all = []

    def __init__(self, name=""):
        self.name = name
        self._book = []
        Author.all.append(self)

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("Please insert the author's book")
        self._book = book

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)   
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    all = []

    def __init__(self, title=""):
        self.title = title
        self._author = None
        Book.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Please insert the book's author")
        self._author = author

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
   
         


class Contract:
    all = []

    def __init__(self, author, book, date="", royalties=type(int)):
        if not isinstance(author, Author):
            raise Exception("Please insert the book's author")
        self.author = author
        if not isinstance(book, Book):
            raise Exception("Please insert the author's book")
        self.book = book
        if not isinstance(date, str):
            raise Exception("Please make the date a string")
        self.date = date
        if not isinstance(royalties, int):
            raise Exception("Author's royalties is a number")
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]