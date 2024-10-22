# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)


class Aluno:
    def __init__(
        self,
        ra: int,
        senha: str,
        nome: str,
        curso: str,
        periodo: str,
        semestre: int,
        modulo: int,
    ):
        self.__ra = ra
        self.__senha = senha
        self.nome = nome
        self.curso = curso
        self.periodo = periodo
        self.semestre = semestre
        self.modulo = modulo

    @property
    def ra(self):
        return self.__ra

    @property
    def senha(self):
        return self.__senha

    # Isso seria viável? a senha deveria vir encriptografada, certo? como?
    # a lógica de colocar isso foi para conseguir verificar com a senha digitada depois
    # e permitir, assim, o acesso


class ValidarLocal:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        distancia = DistanciaAutorizada(localizacao_aluno, nome_campus)
        if distancia.local_autorizado():
            print(
                "Você se encontra próximo a sua sala de aula! Pode ir para o login do aplicativo."
            )
        else:
            print(
                "Você não se encontra próximo a sua sala de sua aula. Acesso ao aplicativo negado!"
            )
