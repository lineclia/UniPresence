# Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
#
from unipresence.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, rm: int, senha_prof: str, nome: str):
        super().__init__(None, rm, None, senha_prof, "professor", nome)

    @property
    def rm(self):
        return self._rm

    @property
    def ra(self):
        raise ValueError("Professor não possui RA")

    @property
    def senha_prof(self):
        return self._senha_prof
