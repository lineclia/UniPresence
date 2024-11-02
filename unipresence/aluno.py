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


class ValidarLocal:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.distancia = DistanciaAutorizada(localizacao_aluno, nome_campus)

    def local_autorizado(self):
        return self.distancia.local_autorizado()


class MenuAluno:
    def __init__(self, aluno: Aluno):
        self.aluno = aluno
        self.menu_aluno()

    def menu_aluno(self):
        while True:
            print("\n--- Menu ---")
            print("1. Faltas totais")
            print("2. Grade horária")
            print("3. Atividades Pendentes")
            print("4. Escanear QR Code")
            print("5. Sair")

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
                print("Saindo do app")
                break

            else:
                print("Opção inválida. Tente novamente.")
