# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self):
        super().__init__("professor")


class MenuProfessor:
    def __init__(self, professor: Professor):
        self.professor = professor
        self.menu_professor()

    def menu_professor(self):
        while True:
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
                break

            else:
                print("Opção inválida. Tente novamente.")
