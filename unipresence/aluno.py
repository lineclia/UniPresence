# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from unipresence.pessoa import Pessoa
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)

# classe Pessoa, com infos comuns entre o prof e aluno
# usar ra para aluno e rm para professor, e senha


class Aluno(Pessoa):
    def __init__(self, ra: int, senha_aluno: str, nome: str):
        super().__init__(ra, None, senha_aluno, None, "aluno", nome)

    @property
    def ra(self):
        return self._ra

    @property
    def rm(self):
        raise ValueError("Aluno não possui RM")

    @property
    def senha_aluno(self):
        return self._senha_aluno


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

        def menu_aluno(database):
            while True:
                print("\n--- Menu ---")
                print("1. Faltas totais")
                print("2. Grade horária")
                print("3. Atividades Pendentes")
                print("4. Escanear QR ")

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
