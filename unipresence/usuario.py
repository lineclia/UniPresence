from bd import ConexaoBanco
from mysql.connector import Error


class Usuario:
    def __init__(self, tipo):
        self.tipo = tipo
        self.id = None
        self.senha = None
        # chama o construtor de Pessoa passando "aluno" como parâmetro do tipo de pessoa

    def login(self):
        if self.tipo == "aluno":
            self.id = input("Digite seu RA: ").strip()
        else:
            self.id = input("Digite sua matrícula(RM): ").strip()

        self.senha = input("Digite sua senha: ")

        return self._verificar_credenciais()

    def _verificar_credenciais(self):
        conn = ConexaoBanco.get_connection()
        if not conn:
            print("Não foi possível conectar ao banco de dados.")
            return False
        try:
            cursor = conn.cursor(dictionary=True)
            if self.tipo == "aluno":
                query = "SELECT * FROM aluno WHERE ra = %s AND senha = %s"
            else:
                query = "SELECT * FROM professor WHERE matricula = %s AND senha = %s"

            cursor.execute(query, (self.id, self.senha))
            usuario = cursor.fetchone()

            if usuario:
                print("Login bem sucedido")
                return True
            else:
                print("Credenciais incorretas.")
                return False
        except Error as e:
            print(f"Erro ao verificar credenciais: {e}")
            return False
