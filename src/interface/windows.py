import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as messagebox
from models import book, library

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

library = library.Lib()

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteca de Livros")
        self.geometry("350x300")

        self.text_frame = ctk.CTkFrame(self)
        self.text_frame.pack(padx=20, pady=20)

        self.basic_text = ctk.CTkLabel(self.text_frame, text="Gerencie sua coleção de livros facilmente.")
        self.basic_text.grid(row=0, column=1, padx=20, pady=10)

        self.text_frame.pack(anchor="center")

        self.add_button = ctk.CTkButton(self, text="Adicionar Livro", border_width=1, command=self.open_addwindow)
        self.add_button.pack(padx=10, pady=10)

        self.search_button = ctk.CTkButton(self, text="Buscar Livro", border_width=1, command=self.open_searchwindow)
        self.search_button.pack(padx=10, pady=10)

        self.del_button = ctk.CTkButton(self, text="Remover Livro", border_width=1, command=self.open_delwindow)
        self.del_button.pack(padx=10, pady=10)

        self.space2 = ctk.CTkLabel(self, text="")
        self.space2.pack(padx=10, pady=10)

    def open_addwindow(self):
        AddWindow(self)

    def open_searchwindow(self):
        SearchWindow(self)

    def open_delwindow(self):
        DelWindow(self)

class AddWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Adicionar Livro")
        self.geometry("300x300")

        self.space1 = ctk.CTkLabel(self, text="")
        self.space1.pack(padx=10, pady=10)

        self.title = ctk.CTkEntry(self, placeholder_text="Título do Livro")
        self.title.pack(padx=10, pady=5)

        self.author = ctk.CTkEntry(self, placeholder_text="Autor do Livro")
        self.author.pack(padx=10, pady=5)

        self.category = ctk.CTkEntry(self, placeholder_text="Categoria do Livro")
        self.category.pack(padx=10, pady=5)

        self.confirm = ctk.CTkButton(self, text="Adicionar", command=self.add_command)
        self.confirm.pack(padx=10, pady=20)

    def add_command(self):
        title_input = self.title.get()
        author_input = self.author.get()
        category_input = self.category.get()

        new_book = book.Bk(title_input, author_input, category_input)
        library.add_book(new_book)

        messagebox(title="Livro Adicionado!", message=f"Livro ID:{new_book.id} foi adicionado com sucesso à biblioteca!", icon="info")

class SearchWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Buscar Livro")
        self.geometry("300x200")

        self.space1 = ctk.CTkLabel(self, text="")
        self.space1.pack(padx=10, pady=10)

        self.id = ctk.CTkEntry(self, placeholder_text="ID do Livro")
        self.id.pack(padx=10, pady=5)

        self.confirm = ctk.CTkButton(self, text="Buscar", command=self.search_command)
        self.confirm.pack(padx=10, pady=5)

        self.space2 = ctk.CTkLabel(self, text="")
        self.space2.pack(padx=10, pady=10)

    def search_command(self):
        id_input = self.id.get()

        book_found = library.search_book(int(id_input))

        if book_found != None: 
            messagebox(title="Livro Encontrado!", message=f"""
O Livro ID:{id_input} foi encontrado com sucesso!

Título: {book_found.title}
Autor: {book_found.author}
Categoria: {book_found.category}
""", icon="info")
        else: 
            messagebox(title="Livro não Encontrado!", message=f"O livro ID:{id_input} não foi encontrado!", icon="warning")

class DelWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Remover Livro")
        self.geometry("300x200")

        self.space1 = ctk.CTkLabel(self, text="")
        self.space1.pack(padx=10, pady=10)

        self.id = ctk.CTkEntry(self, placeholder_text="ID do Livro")
        self.id.pack(padx=10, pady=5)

        self.confirm = ctk.CTkButton(self, text="Remover", command=self.del_command)
        self.confirm.pack(padx=10, pady=5)

        self.space2 = ctk.CTkLabel(self, text="")
        self.space2.pack(padx=10, pady=10)

    def del_command(self):
        id_input = self.id.get()

        book_removed = library.del_book(int(id))

        if book_removed:
            messagebox(title="Livro removido com Sucesso!", message=f"O Livro ID:{id_input} foi removido com sucesso!", icon="info")
        else: 
            messagebox(title="Livro não Encontrado!", message=f"O livro ID:{id_input} não foi encontrado!", icon="warning")