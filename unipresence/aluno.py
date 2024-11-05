# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)
from unipresence.bd import ConexaoBanco
from mysql.connector import Error
import geocoder
from tabulate import tabulate
# biblioteca que ajuda na visualização em forma de tabelas


class Aluno:
    def __init__(self, tipo):
        self.tipo = tipo
        # super().__init__("aluno")
        self.ra = None
        self.localizacao = None
        # chama o construtor de Pessoa passando "aluno" como parâmetro do tipo de pessoa

    def get_dados_login(self, ra: int, senha: str):
        # parametros como metodos de instância
        conn = ConexaoBanco.get_connection()
        if not conn:
            print("Não foi possível conectar ao banco de dados.")
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM aluno WHERE ra = %s AND senha = %s"
            cursor.execute(query, (ra, senha))
            aluno = cursor.fetchone()
            if aluno:
                self.ra = aluno["ra"]
            return aluno
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def obtem_localizacao(self):
        # usando o geocoder para pegar a localização através no IP (para a simulação)
        g = geocoder.ip("me")
        if g.ok:
            self.localizacao = LocalizacaoAluno(g.latlng[0], g.latlng[1])
        else:
            print("Não foi possível obter a localizaçao.")

    def login(self):
        self.obtem_localizacao()
        nome_campus = "mantiqueira"  # Ou qualquer campus que você deseja validar
        validacao = DistanciaAutorizada(self.localizacao, nome_campus)
        if validacao:
            # .local_autorizado():
            ra_digitado = int(input("RA: "))
            senha_digitada = input("Senha: ")
            aluno = self.get_dados_login(ra=ra_digitado, senha=senha_digitada)

            if aluno:
                menu_aluno = MenuAluno(self, aluno["nome"])
                menu_aluno.menu_aluno()

            else:
                print("Credenciais incorretas.")
        else:
            print(
                "Não é possível seguir para a página de login, aluno está fora da área de cobertura."
            )


class MenuAluno:
    def __init__(self, aluno: Aluno, nome_aluno):
        self.aluno = aluno
        self.nome_aluno = nome_aluno
        self.conn = ConexaoBanco.get_connection()

    def menu_aluno(self):
        if not self.conn:
            print("Não foi possível conectar ao banco de dados.")

        print(f"Bem-vindo(a), {self.nome_aluno}")

        sair = False
        while not sair:
            print("\n--- Menu ---")
            print("1. Grade Horária")
            print("2. Faltas Totais")
            print("3. Presenças Totais")
            print("4. Escanear QR Code")
            print("5. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.exibir_grade_horaria()

            elif choice == "2":
                pass
                self.exibir_faltas_totais()

            elif choice == "3":
                self.exibir_presencas_totais()

            elif choice == "4":
                self.escanear_qr_code()

            elif choice == "5":
                print("Saindo do app...")
                sair = True

            else:
                print("Opção inválida. Tente novamente.")
                return False

        if self.conn:
            self.conn.close()

    # Métodos para as funções do Menu
    def exibir_grade_horaria(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            view_query = "SELECT * FROM grade_horaria_aluno_semana WHERE RA = %s"
            cursor.execute(view_query, (self.aluno.ra,))
            resultados = cursor.fetchall()

            table = []
            # Exibir os resultados
            for linha in resultados:
                (
                    Aluno,
                    RA,
                    Curso,
                    Disciplina,
                    Dia_da_Semana,
                    Inicio,
                    Fim,
                    Modulo,
                ) = linha
                table.append([Disciplina, Dia_da_Semana, Inicio, Fim])
            print(
                tabulate(
                    table, headers=["Disciplina", "Dia da Semana", "Início", "Fim"]
                )
            )

        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def exibir_faltas_totais(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            view_query = "SELECT * FROM historico_presenca_aluno WHERE RA = %s"
            cursor.execute(view_query, (self.aluno.ra,))
            resultados = cursor.fetchall()

            table = []
            # Exibir os resultados
            for linha in resultados:
                (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
                table.append([Disciplina, TotalFaltas])
            print(tabulate(table, headers=["Disciplina", "Total de Faltas"]))
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def exibir_presencas_totais(self):
        if not self.conn:
            print("Conexão com o banco de dados não disponível.")
            return

        cursor = self.conn.cursor()
        try:
            view_query = "SELECT * FROM historico_presenca_aluno WHERE RA = %s"
            cursor.execute(view_query, (self.aluno.ra,))
            resultados = cursor.fetchall()

            table = []
            # Exibir os resultados
            for linha in resultados:
                (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
                table.append([Disciplina, TotalPresencas])
            print(tabulate(table, headers=["Disciplina", "Total de Presenças"]))
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def escanear_qr_code():
        # Implementar lógica para escanear QR Code usando cursor
        pass
