# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self):
        super().__init__("professor")


class MenuProfessor:
    def __init__(self, professor: Professor, nome_professor):
        self.professor = professor
        self.nome_professor = nome_professor

    def menu_professor(self):
        print(f"Bem-vindo(a), {self.nome_professor}!")

        sair = False
        while not sair:
            print("\n--- Menu ---")
            print("1. Grade horária")
            print("2. Aula do dia")
            print("3. Relatório")
            print("4. Liberar QR Code ")
            print("5. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                pass

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            elif choice == "5":
                print("Saindo do app...")
                sair = True

            else:
                print("Opção inválida. Tente novamente.")
                return False
