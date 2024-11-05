import os
import mysql.connector
from mysql.connector import Error


class ConexaoBanco:
    _connection = None

    @classmethod
    def get_connection(cls):
        """Obtem a conexão com o bd, criando-a se necessário"""
        if cls._connection is None or not cls._connection.is_connected():
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
