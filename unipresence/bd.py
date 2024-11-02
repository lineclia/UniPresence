import mysql.connector


class ConectarBanco:
    def conectar_banco(self):
        try:
            connection = mysql.connector.connect(
                host="172.17.0.2",
                user="root",
                password="Litha003",
                database="feob",
            )
            if connection.is_connected():
                print("Conectado ao banco de dados")
                return connection
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None


class LoginAluno(ConectarBanco):
    def login(self, ra: str, senha: str):
        # chamar o método da classe pai para conectar no banco
        conn = self.conectar_banco()

        try:
            if conn is None:
                print("Não foi possível conectar ao banco de dados.")
                return None

            cursor = conn.cursor(dictionary=True)

            # consulta para verificar o RA e a senha
            query_aluno = "SELECT * FROM universidade WHERE ra = %s AND senha = %s"
            cursor.execute(query_aluno, (ra, senha))
            aluno = cursor.fetchone()

            if aluno:
                print("Login realizado com sucesso!")
                return aluno
            else:
                print("RA ou senha inválidos")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if conn:
                conn.close()


class LoginProfessor(ConectarBanco):
    def login(self, matricula: str, senha: str):
        conn = self.conectar_banco()
        try:
            if conn is None:
                print("Não foi possível conectar ao banco de dados.")
                return None

            cursor = conn.cursor(dictionary=True)

            # consulta para verificar a matricula e a senha
            query_professor = (
                "SELECT * FROM professor WHERE matricula = %s AND senha = %s"
            )
            cursor.execute(query_professor, (matricula, senha))
            professor = cursor.fetchone()

            if professor:
                print("Login de professor realizado com sucesso!")
                return professor
            else:
                print("Matrícula ou senha inválidos.")
                return None
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if conn:
                conn.close()
