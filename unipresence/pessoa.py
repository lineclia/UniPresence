# TODO: acesso professor, acesso aluno, redefinicao de senha
# usar isso pra depois chamar o acesso aluno em aluno.py e  o acesso professor em professor.py

from unipresence.bd import ConexaoBanco


class Pessoa(ConexaoBanco):
    def __init__(self, tipo: str):
        super().__init__()
        self._tipo = tipo
