#!/usr/bin/env python3


class Book:
    """A published title that can have one or more authors through contracts."""

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return the contracts that mention this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Use contracts as the middle table to find related authors."""
        return [contract.author for contract in self.contracts()]


class Author:
    """A writer who can sign contracts for many books."""

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return the contracts this author has signed."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Use contracts as the middle table to find related books."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a contract between this author and a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Add up royalties from every contract this author has signed."""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    """Connects one author to one book, plus the date and royalty terms."""

    all = []

    def __init__(self, author, book, date, royalties):
        # Properties check types first so we only keep valid contracts.
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return every contract that was signed on the given date."""
        return [contract for contract in cls.all if contract.date == date]
