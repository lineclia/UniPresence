# TODO: acesso professor, acesso aluno, redefinicao de senha
# usar isso pra depois chamar o acesso aluno em aluno.py e  o acesso professor em professor.py


class Pessoa:
    def __init__(self, ra: int, rm: int, senha: str, tipo: str):
        self._ra = ra
        # registro aluno
        self._rm = rm
        # registro matricula (professor)
        self._senha = senha
        self.tipo = tipo

        # tipo: professor ou aluno

    def validacao_dados_login(self, ra=None, rm=None, senha=None):
        if self.tipo == "aluno" and ra == self._ra and senha == self._senha:
            return True
        elif self.tipo == "professor" and rm == self._rm and senha == self._senha:
            return True
        return False

    def login(self):
        tipo_digitado = str(input("Você é um Aluno ou Professor? ")).lower()

        if tipo_digitado == "aluno":
            from validacao_geografica import LocalizacaoAluno
            from aluno import ValidarLocal

            LocalizacaoAluno = LocalizacaoAluno(-21.96613986612555, -46.77416860602757)
            # Coordenada aleatória para exemplo
            validacao = ValidarLocal(LocalizacaoAluno, "mantiqueira")

            if validacao.local_autorizado():
                ra_digitado = int(input("RA: "))
                senha_digitada = input("Senha: ")
                if self.validacao_dados_login(ra=ra_digitado, senha=senha_digitada):
                    print("Acesso concedido.")
                else:
                    print("Credenciais incorretas.")
            else:
                print(
                    "Não é possível seguir para a página de login, aluno está fora da área de cobertura."
                )
        elif tipo_digitado == "professor":
            rm_digitado = int(input("RM: "))
            senha_digitada = input("Senha: ")
            if self.validacao_dados_login(rm=rm_digitado, senha=senha_digitada):
                print("Acesso concedido.")
            else:
                print("Credenciais incorretas.")
        else:
            print("Tipo inválido. Por favor insira 'Aluno' ou 'Professor'")
