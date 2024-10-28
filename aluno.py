# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from pessoa import Pessoa
from validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)

# classe Pessoa, com infos comuns entre o prof e aluno
# usar ra para aluno e rm para professor, e senha


class Aluno(Pessoa):
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
        super().__init__(ra=ra, rm=None, senha=senha, tipo="aluno")
        self.nome = nome
        self.curso = curso
        self.periodo = periodo
        self.semestre = semestre
        self.modulo = modulo

    # TODO: Fazer API que vai ter os dados dos alunos (conferir se ta correto o pensamento)

    @property
    def ra(self):
        return self._ra

    @property
    def senha(self):
        return self._senha


class ValidarLocal:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.distancia = DistanciaAutorizada(localizacao_aluno, nome_campus)

    def local_autorizado(self):
        return self.distancia.local_autorizado()
