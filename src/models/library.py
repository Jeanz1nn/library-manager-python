class Lib:
    def __init__(self): 
        self.books = []
        self.id = 0

    def add_book(self, book): 
        self.books.append(book)
        self.books[self.id].id = self.id
        print(f"\nLivro adicionado com sucesso! ID:{self.id}") # logtoremove
        print(f"Título do Livro: {self.books[self.id].title}") # logtoremove
        print(f"Autor do Livro: {self.books[self.id].author}") # logtoremove
        print(f"Categoria do Livro: {self.books[self.id].category}") # logtoremove
        self.id += 1

    def search_book(self, id):
        if 0 <= id < len(self.books) and self.books[id] is not None:
            book = self.books[id]
            print(f"\nLivro ID:{id} foi encontrado!") # logtoremove
            print(f"Título: {book.title}") # logtoremove
            print(f"Autor: {book.author}") # logtoremove
            print(f"Título: {book.category}") # logtoremove   
            return book
        print(f"\nLivro ID:{id} não foi encontrado!") # logtoremove
        return None

    def del_book(self, id):
        if 0 <= id < len(self.books) and self.books[id] is not None:
            self.books[id] = None  
            print(f"\nLivro ID:{id} foi removido com sucesso!")  # logtoremove
            return True
        print(f"\nLivro ID:{id} não foi encontrado!")  # logtoremove
        return False