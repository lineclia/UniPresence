# Classe professor, deve solicitar as credenciais (registro de matrícula e senha) e fazer o login
# nome, matricula, curso, turma, modulo
from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, rm: int, nome: str, senha: str):
        super().__init__(ra=None, rm=rm, senha=senha, tipo="professor")
        self.nome = nome

    @property
    def rm(self):
        return self._rm

    @property
    def senha(self):
        return self._senha
