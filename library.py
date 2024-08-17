import json

class Library:
    def __init__(self):
        self.books = {}
        self.id = 0

    def add_book(self, title, author, category):
        self.books[f"book_{self.id}"] = {"title": title, "author": author, "category": category}
        self.id += 1

    def del_book(self, id):
        book_index = f"book_{id}"
        if book_index in self.books:
            removed_book = self.books[book_index]
            del self.books[book_index]  
            return removed_book
        else:
            return None

    def search_book(self, id):
        book_index = f"book_{id}"
        if book_index in self.books: 
            return self.books[book_index]
        else:
            return None

    def list_books(self):
        if not self.books:
            return None
        else:
            book_list = []
            for key, value in self.books.items():
                book_info = f"ID: {key.split('_')[1]}, Título: {value['title']}, Autor: {value['author']}, Categoria: {value['category']}"
                book_list.append(book_info)
            print("\n".join(book_list))
            return 0

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                self.books = json.load(file)
            self.id = len(self.books)
            return True
        except FileNotFoundError:
            return False


    def clear_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({}, file, indent=4)
        self.books = {} 
        self.id = 0 

