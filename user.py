class HashTable:
    def __init__(self, size=10007):
        self.size = size
        self.table = [None] * size
        self.deleted_marker = "DELETED"

    def _hash(self, key, attempt=0):
        return (hash(key) + attempt ** 2) % self.size

    def insert(self, key, value):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None or self.table[index] == self.deleted_marker or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            attempt += 1

    def search(self, key):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None:
                return None
            if self.table[index] != self.deleted_marker and self.table[index][0] == key:
                return self.table[index][1]
            attempt += 1
        return None

    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None:
                return
            if self.table[index] != self.deleted_marker and self.table[index][0] == key:
                self.table[index] = self.deleted_marker
                return
            attempt += 1

library = HashTable()

def init():
    global library
    library = HashTable()

def addBook(author, title):
    books = library.search(author)
    if books is None:
        books = set()
    books.add(title)
    library.insert(author, books)

def find(author, title):
    books = library.search(author)
    return books is not None and title in books

def delete(author, title):
    books = library.search(author)
    if books is None or title not in books:
        return
    books.remove(title)
    if books:
        library.insert(author, books)
    else:
        library.delete(author)

def findByAuthor(author):
    books = library.search(author)
    return sorted(books) if books else []