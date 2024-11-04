# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa
from unipresence.bd import ConexaoBanco
from mysql.connector import Error


class Professor(Pessoa):
    def __init__(self):
        super().__init__("professor")

    def get_dados_login(self, matricula: int, senha: str):
        conn = ConexaoBanco.get_connection()
        if not conn:
            print("Não foi possível conectar ao banco de dados.")
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM professor WHERE matricula = %s AND senha = %s"
            cursor.execute(query, (matricula, senha))
            professor = cursor.fetchone()
            return professor
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def login(self):
        matricula_digitada = int(input("Matrícula(RM): "))
        senha_digitada = input("Senha: ")
        professor = self.get_dados_login(
            matricula=matricula_digitada, senha=senha_digitada
        )
        if professor:
            menu_professor = MenuProfessor(self, professor["nome"])
            menu_professor.menu_professor()


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
