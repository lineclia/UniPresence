# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, rm: int, senha_prof: str, nome: str):
        super().__init__(None, rm, None, senha_prof, "professor", nome)

    @property
    def rm(self):
        return self._rm

    @property
    def ra(self):
        raise ValueError("Professor não possui RA")

    @property
    def senha_prof(self):
        return self._senha_prof


class MenuProfessor:
    def __init__(self, menu_professor):
        self._menu_professor = menu_professor

        def menu_professor(database):
            while True:
                print("\n--- Menu ---")
                print("1. Grade horária")
                print("2. Aula do dia")
                print("3. Relatório")
                print("4. Liberar QR Code ")
                print("5. Sair")

                choice = input("Escolha uma opção: ")

                if choice == "1":
                    title = input("Título: ")
                    author = input("Autor: ")
                    publication_year = int(input("Ano de publicação: "))
                    database.insert_book(title, author, publication_year)
                elif choice == "2":
                    name = input("Nome: ")
                    address = input("Endereço: ")
                    phone = input("Telefone: ")
                    database.insert_client(name, address, phone)

                else:
                    print("Opção inválida. Tente novamente.")
