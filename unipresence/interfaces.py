# unipresence/interfaces.py

from abc import ABC, abstractmethod


class PessoaInterface(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def validacao_dados_login(
        self, ra=None, rm=None, senha_aluno=None, senha_prof=None
    ):
        pass
