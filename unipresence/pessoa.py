# TODO: acesso professor, acesso aluno, redefinicao de senha
# usar isso pra depois chamar o acesso aluno em aluno.py e  o acesso professor em professor.py

from unipresence.validacao_geografica import LocalizacaoAluno, DistanciaAutorizada
from unipresence.interfaces import PessoaInterface


class Pessoa(PessoaInterface):
    def __init__(
        self, ra: int, rm: int, senha_aluno: str, senha_prof: str, tipo: str, nome: str
    ):
        self._ra = ra
        # registro aluno
        self._rm = rm
        # registro matricula (professor)
        self._senha_aluno = senha_aluno
        self._senha_prof = senha_prof
        self._tipo = tipo
        self._nome = nome

        # tipo: professor ou aluno

    @property
    def rm(self):
        raise NotImplementedError()

    @property
    def ra(self):
        raise ValueError("Professor não possui RA")

    def validacao_dados_login(
        self, ra=None, rm=None, senha_aluno=None, senha_prof=None
    ):
        if (
            self._tipo == "aluno"
            and ra == self._ra
            and senha_aluno == self._senha_aluno
        ):
            return True
        elif (
            self._tipo == "professor"
            and rm == self._rm
            and senha_prof == self._senha_prof
        ):
            return True
        return False

    def login(self):
        tipo_digitado = str(input("Você é um Aluno ou Professor? ")).lower()

        if tipo_digitado == "aluno":
            # Solicitar coordenadas do aluno
            latitude = float(input("Digite sua latitude: "))
            longitude = float(input("Digite sua longitude: "))
            localizacao_aluno = LocalizacaoAluno(latitude, longitude)

            # Verificar se a localização é autorizada
            nome_campus = "mantiqueira"  # Ou qualquer campus que você deseja validar
            validacao = DistanciaAutorizada(localizacao_aluno, nome_campus)

            if validacao.local_autorizado():
                ra_digitado = int(input("RA: "))
                senha_digitada = input("Senha: ")
                if self.validacao_dados_login(
                    ra=ra_digitado, senha_aluno=senha_digitada
                ):
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
            if self.validacao_dados_login(rm=rm_digitado, senha_prof=senha_digitada):
                print("Acesso concedido.")
            else:
                print("Credenciais incorretas.")
        else:
            print("Tipo inválido. Por favor insira 'Aluno' ou 'Professor'")
