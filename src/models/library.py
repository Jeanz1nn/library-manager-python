class Lib:
    def __init__(self): 
        self.books = []
        self.id = 0

    def add_book(self, book): 
        self.books.append(book)
        self.books[self.id].id = self.id
        self.id += 1

    def search_book(self, id):
        if 0 <= id < len(self.books) and self.books[id] is not None:
            book = self.books[id]
            return book
        return None

    def del_book(self, id):
        if 0 <= id < len(self.books) and self.books[id] is not None:
            self.books[id] = None  
            return True
        return False