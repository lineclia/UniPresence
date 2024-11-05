# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa
from unipresence.bd import ConexaoBanco
from mysql.connector import Error


class Professor(Pessoa):
    def __init__(self):
        super().__init__("professor")
        self.matricula = None

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
            if professor:
                self.matricula = professor["matricula"]
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
        self.conn = ConexaoBanco.get_connection()

    def menu_professor(self):
        if not self.conn:
            print("Não foi possível conectar ao banco de dados.")

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
                self.exibir_grade_horaria()

            elif choice == "2":
                self.exibir_aula_dia()

            elif choice == "3":
                self.relatorio()

            elif choice == "4":
                self.liberar_qr_code()

            elif choice == "5":
                print("Saindo do app...")
                sair = True

            else:
                print("Opção inválida. Tente novamente.")
                return False

    def exibir_grade_horaria(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            view_query = (
                "SELECT * FROM grade_horaria_professor_semana WHERE Matrcula = %s"
            )
            cursor.execute(view_query, (self.professor.matricula,))
            resultados = cursor.fetchall()

            # Exibir os resultados
            for linha in resultados:
                (
                    Professor,
                    Matrcula,  # ALTERAR PARA O NOME CORRETO QUE ESTIVER NO BANCO, O MEU TA EM INGLES POR ISSO MATRCULA
                    Curso,
                    Disciplina,
                    Dia_da_Semana,
                    Inicio,
                    Fim,
                    Modulo,
                    Periodo,
                ) = linha
                print(
                    f"Dia da semana: {Dia_da_Semana}, Disciplina: {Disciplina}, Horário de início: {Inicio}, Horário Fim: {Fim}"
                )

        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def exibir_aula_dia(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            view_query = (
                "SELECT * FROM grade_horaria_professor_semana WHERE Matrcula = %s"
            )
            cursor.execute(view_query, (self.professor.matricula,))
            resultados = cursor.fetchall()

            # Exibir os resultados
            for linha in resultados:
                (
                    Professor,
                    Matrcula,  # ALTERAR PARA O NOME CORRETO QUE ESTIVER NO BANCO, O MEU TA EM INGLES POR ISSO MATRCULA
                    Curso,
                    Disciplina,
                    Dia_da_Semana,
                    Inicio,
                    Fim,
                    Modulo,
                    Periodo,
                ) = linha
                print(f"Dia da semana: {Dia_da_Semana}, Disciplina: {Disciplina}")
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def relatorio(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            query = """SELECT Disciplina, SUM(`Total Presencas`) AS TotalPresencas, SUM(`Total Faltas`) AS TotalFaltas
                    FROM historico_presenca_aluno
                    GROUP BY Disciplina"""
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Resumo por Disciplina:")
            for linha in resultados:
                disciplina, total_presencas, total_faltas = linha
                print(
                    f"Disciplina: {disciplina}, Total de Presenças: {total_presencas}, Total de Faltas: {total_faltas}"
                )
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()
