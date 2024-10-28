# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, rm: int, senha: str, nome: str):
        super().__init__(None, rm, senha, "professor", nome)

    @property
    def rm(self):
        return self._rm

    @property
    def ra(self):
        raise ValueError("Professor não possui RA")

    @property
    def senha(self):
        return self._senha
