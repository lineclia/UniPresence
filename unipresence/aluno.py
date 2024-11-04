# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from unipresence.pessoa import Pessoa
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)


class Aluno(Pessoa):
    def __init__(self):
        super().__init__("aluno")
        # chama o construtor de Pessoa passando "aluno" como parâmetro do tipo de pessoa


class ValidarLocal:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.distancia = DistanciaAutorizada(localizacao_aluno, nome_campus)

    def local_autorizado(self):
        return self.distancia.local_autorizado()


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
