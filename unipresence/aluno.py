# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from unipresence.pessoa import Pessoa
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)


class Aluno(Pessoa):
    def __init__(self):
        # self._ra = ra
        super().__init__("aluno")

    # @property
    # def ra(self):
    #     return self._ra

    # @property
    # def rm(self):
    #     raise ValueError("Aluno não possui RM")

    # @property
    # def senha_aluno(self):
    #     return self._senha_aluno


class ValidarLocal:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.distancia = DistanciaAutorizada(localizacao_aluno, nome_campus)

    def local_autorizado(self):
        return self.distancia.local_autorizado()


# criar as paginas do app do aluno e do professor
# do professor: escolher a materia, o dia, gerar código
# do aluno: inserir código, gerar QR Code, contabilizar presença
# quando contabiliza presença, isso vai pra uma tabela que contem o nome do aluno, RA, a materia, o dia, o horario
# que a presença foi contabilizada e se esteve presente ou não


class MenuAluno:
    def __init__(self, menu_aluno):
        self._menu_aluno = menu_aluno
        self.connection = self.connect_to_database()

    # def connect_to_database(self):
    #     try:
    #         connection = mysql.connector.connect(
    #             host="172.17.0.2:3306",
    #             user="root",
    #             password="Litha003",
    #             database="feob",
    #         )
    #         if connection.is_connected():
    #             print("Conectado ao banco de dados")
    #             return connection
    #     except mysql.connector.Error as err:
    #         print(f"Erro: {err}")
    #         return None

    def menu_aluno(self):
        while True:
            print("\n--- Menu ---")
            print("1. Faltas totais")
            print("2. Grade horária")
            print("3. Atividades Pendentes")
            print("4. Escanear QR Code")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.faltas_totais()
            elif choice == "2":
                self.grade_horaria()

            elif choice == "3":
                self.atividades_pendentes()

            elif choice == "4":
                self.escanear_qr_code

            elif choice == "5":
                break

            else:
                print("Opção inválida. Tente novamente.")
