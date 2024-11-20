from usuario import Usuario


class Aluno(Usuario):
    def __init__(self):
        super().__init__(tipo="aluno")
        self.ra = None
        self.localizacao = None
