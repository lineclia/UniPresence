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
                menu_aluno = MenuAluno(self, aluno["nome"])
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

    def menu_aluno(self):
        print(f"Bem-vindo(a), {self.nome_aluno}!")

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
                pass
            elif choice == "2":
                pass
                # puxar da tabela aula e mostrar

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
