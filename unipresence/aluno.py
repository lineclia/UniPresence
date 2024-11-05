# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)
from unipresence.bd import ConexaoBanco
from mysql.connector import Error
from unipresence.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self):
        super().__init__("aluno")
        self.ra = None
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

    def login(self):
        latitude = float(input("Digite sua latitude: "))
        longitude = float(input("Digite sua longitude: "))
        localizacao_aluno = LocalizacaoAluno(latitude, longitude)
        # pede a localização do aluno para verificar se está em área permitida

        nome_campus = "mantiqueira"  # Ou qualquer campus que você deseja validar
        validacao = DistanciaAutorizada(localizacao_aluno, nome_campus)

        if validacao.local_autorizado():
            ra_digitado = int(input("RA: "))
            senha_digitada = input("Senha: ")
            aluno = self.get_dados_login(ra=ra_digitado, senha=senha_digitada)

            if aluno:
                menu_aluno = MenuAluno(self, aluno["nome_aluno"])
                menu_aluno.menu_aluno()

            # if isinstance(aluno, dict):  # verifica se aluno é um dicionário
            # from unipresence.aluno import MenuAluno
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
        # if not self.conn:
        #     print("Não foi possível conectar ao banco de dados.")
        #     self.conn = None

    def menu_aluno(self):
        if not self.conn:
            print("Não foi possível conectar ao banco de dados.")

        # cursor = self.conn.cursor()

        print("Bem-vindo(a)!")

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
            view_query = "SELECT * FROM grade_horaria_aluno_semana"
            cursor.execute(view_query, (self.Aluno))
            resultados = cursor.fetchall()

            # Exibir os resultados
            for linha in resultados:
                (
                    Aluno,
                    Curso,
                    Disciplina,
                    dia_semana,
                    horario_inicio,
                    horario_fim,
                    modulo,
                ) = linha
                print(
                    f"Aluno: {Aluno}, Curso: {Curso}, Modulo: {modulo}, Disciplina: {Disciplina}, Dia semana: {dia_semana}, "
                    f"Horário Início: {horario_inicio}, Horário Fim: {horario_fim}"
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

            # Exibir os resultados
            for linha in resultados:
                (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
                print(
                    f"Disciplina: {Disciplina}, Total de Faltas: {TotalFaltas} "
                    # Aluno: {NomeAluno},
                )
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

            # Exibir os resultados
            for linha in resultados:
                (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
                print(
                    f"Disciplina: {Disciplina}, Total de Presenças: {TotalPresencas} "
                    # Aluno: {NomeAluno},
                )
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()

    def escanear_qr_code():
        # Implementar lógica para escanear QR Code usando cursor
        pass
