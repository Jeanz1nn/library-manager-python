from styles import Styles
from library import Library

style = Styles()
lib = Library()

def display_menu():
    print(style.bold + "-" * 50)
    print(f"{style.magenta}Biblioteca de Livros{style.white}".center(50))
    print("-" * 50)
    print(style.reset, end='')

    while True:
        print(f"\n{style.bold}[1] -{style.reset} Adicionar livro à Biblioteca")
        print(f"{style.bold}[2] -{style.reset} Buscar livro na Biblioteca")
        print(f"{style.bold}[3] -{style.reset} Remover livro da Biblioteca")
        print(f"{style.bold}[4] -{style.reset} Listar todos os livros da Biblioteca")
        print(f"{style.bold}[5] -{style.reset} Salvar dados em um arquivo JSON")
        print(f"{style.bold}[6] -{style.reset} Carregar dados de um arquivo JSON")
        print(f"{style.bold}[7] -{style.reset} Limpar dados de um arquivo JSON")
        print(f"{style.bold}[0] -{style.reset} Encerrar aplicação\n")

        option = int(input(f"{style.blue}Qual opção você deseja realizar? {style.reset}"))
        print()

        match option:
            case 1:
                add_book()
            case 2: 
                search_book()
            case 3:
                del_book()
            case 4: 
                list_books()
            case 5:
                lib.save_to_json("data.json")
                print(f"{style.green}[+] Dados salvos com sucesso no arquivo [data.json]{style.reset}")
            case 6:
                result = lib.load_from_json("data.json")
                if result: 
                    print(f"{style.cyan}[*] Dados carregados com sucesso do arquivo [data.json]{style.reset}")
                else:
                    print(f"{style.red}[!] Erro ao carregar o arquivo!{style.reset}")
            case 7:
                lib.clear_json("data.json")
                print(f"{style.yellow}[-] Todos os dados foram apagados do arquivo JSON!{style.reset}")
            case 0:
                break 
            case _: 
                print("Opção Inválida! Tente novamente.")

def add_book():
    title = input("Título do Livro: ")
    author = input("Autor do Livro: ")
    category = input("Categoria do Livro: ")
    lib.add_book(title, author, category)
    print(f"\n{style.green}[+] Livro {lib.id-1} adicionado com sucesso à biblioteca!{style.reset}")

def search_book():
    id = int(input("Insira o ID do livro que deseja encontrar: "))

    result = lib.search_book(id)
    
    if result is not None:
        print(f"Informações do Livro {id}:\n")
        print(f"Título: {result['title']}")
        print(f"Autor: {result['author']}")
        print(f"Categoria: {result['category']}")
    else: 
        print(f"\n{style.red}[!] Livro {id} não foi encontrado!{style.reset}")

def del_book():
    id = int(input("Insira o ID do livro que deseja remover: "))

    result = lib.del_book(id)

    if result is not None: 
        print(f"\n{style.yellow}[-] Livro {id} removido com sucesso!{style.reset}")
    else: 
        print(f"\n{style.red}[!] Livro {id} não foi encontrado!{style.reset}")

def list_books():
    result = lib.list_books()

    if result is not None:
        print(f"\n{style.cyan}[*] Livros listados com sucesso!{style.reset}")
    else: 
        print(f"\n{style.red}[!] Não há livros na biblioteca!{style.reset}")

