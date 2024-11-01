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
