from aluno import Usuario


class Professor(Usuario):
    def __init__(self):
        super().__init__(tipo="professor")
