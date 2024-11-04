import os
import mysql.connector
from mysql.connector import Error


class ConexaoBanco:
    _connection = None

    @classmethod
    def get_connection(cls):
        """Obtem a conexão com o bd, criando-a se necessário"""
        if cls._connection is None or not cls.connection.is_connected():
            try:
                cls._connection = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_DATABASE"),
                )
                if cls._connection.is_connected():
                    print("Conectado ao banco de dados")

            except Error as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                cls._connection = None
        return cls._connection

    @classmethod
    def close_connection(cls):
        """Fecha a conexão com o banco caso esteja aberta"""
        if cls._connection and cls._connection.is_connected():
            cls._connection.close()
            print("Conexão com o bando de dados encerrada")
            cls._connection = None


# class LoginAluno(ConexaoBanco):
#     def login(self, ra: str, senha: str):
#         # chamar o método da classe pai para conectar no banco
#         conn = self.conectar_banco()

#         try:
#             if conn is None:
#                 print("Não foi possível conectar ao banco de dados.")
#                 return None

#             cursor = conn.cursor(dictionary=True)

#             # consulta para verificar o RA e a senha

#             query_aluno = "SELECT * FROM universidade WHERE ra = %s AND senha = %s"
#             # TODO: atualizar as chamadas diretas na tabela por views
#             # forma SELECT * FROM nome_view WHERE condicao = valor;
#             cursor.execute(query_aluno, (ra, senha))
#             aluno = cursor.fetchone()

#             if aluno:
#                 print("Login realizado com sucesso!")
#                 return aluno
#             else:
#                 print("RA ou senha inválidos")

# except mysql.connector.Error as err:
#     print(f"Erro: {err}")
# finally:
#     if conn:
#         conn.close()


# class LoginProfessor(ConexaoBanco):
#     def login(self, matricula: str, senha: str):
#         conn = self.conectar_banco()
#         try:
#             if conn is None:
#                 print("Não foi possível conectar ao banco de dados.")
#                 return None

#             cursor = conn.cursor(dictionary=True)

#             # consulta para verificar a matricula e a senha
#             query_professor = (
#                 "SELECT * FROM professor WHERE matricula = %s AND senha = %s"
#             )
#             cursor.execute(query_professor, (matricula, senha))
#             professor = cursor.fetchone()

#             if professor:
#                 print("Login de professor realizado com sucesso!")
#                 return professor
#             else:
#                 print("Matrícula ou senha inválidos.")
#                 return None
#         except mysql.connector.Error as err:
#             print(f"Erro: {err}")
#         finally:
#             if conn:
#                 conn.close()
