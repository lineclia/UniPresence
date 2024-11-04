# TODO: acesso professor, acesso aluno, redefinicao de senha
# usar isso pra depois chamar o acesso aluno em aluno.py e  o acesso professor em professor.py

import mysql.connector
from unipresence.validacao_geografica import LocalizacaoAluno, DistanciaAutorizada

# from unipresence.interfaces import PessoaInterface
from unipresence.bd import ConectarBanco


class Pessoa(ConectarBanco):
    def __init__(self, tipo: str):
        super().__init__()
        self._tipo = tipo

    def validacao_dados_login(self, ra=None, matricula=None, senha=None):
        conn = self.conectar_banco()
        try:
            cursor = conn.cursor(dictionary=True)

            if self._tipo == "aluno":
                # verifica na tabela aluno com o RA e senha
                query_aluno = "SELECT * FROM aluno WHERE ra = %s AND senha = %s"
                cursor.execute(query_aluno, (ra, senha))
                aluno = cursor.fetchone()
                return aluno
                # retorna True se o aluno existir

            elif self._tipo == "professor":
                # verifica na tabela professor com matricula e senha
                query_professor = (
                    "SELECT * FROM professor WHERE matricula = %s AND senha = %s"
                )
                cursor.execute(query_professor, (matricula, senha))
                professor = cursor.fetchone()
                return professor

            return None
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None
        finally:
            if conn:
                conn.close()

    def login(self, tipo):
        # tipo_digitado = str(input("Você é um Aluno ou Professor? ")).lower()
        self._tipo = tipo

        if tipo == "aluno":
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
                aluno = self.validacao_dados_login(ra=ra_digitado, senha=senha_digitada)

                if isinstance(aluno, dict):  # verifica se aluno é um dicionário
                    # print("Acesso concedido.Bem vindo(a), {aluno['aluno']}")
                    from unipresence.aluno import MenuAluno

                    menu_aluno = MenuAluno(self, aluno["nome"])
                    menu_aluno.menu_aluno()
                else:
                    print("Credenciais incorretas.")
            else:
                print(
                    "Não é possível seguir para a página de login, aluno está fora da área de cobertura."
                )

        elif tipo == "professor":
            matricula_digitada = int(input("Matrícula: "))
            senha_digitada = input("Senha: ")
            professor = self.validacao_dados_login(
                matricula=matricula_digitada, senha=senha_digitada
            )
            if isinstance(professor, dict):
                from unipresence.professor import MenuProfessor

                menu_professor = MenuProfessor(self, professor["nome"])
                menu_professor.menu_professor()
            else:
                print("Credenciais incorretas.")
        else:
            print("Tipo inválido. Por favor insira 'Aluno' ou 'Professor'")
