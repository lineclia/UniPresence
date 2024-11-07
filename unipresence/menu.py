from unipresence.bd import ConexaoBanco
from tabulate import tabulate

# from unipresence.aluno import Aluno
from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
    # LocalizacaoCampus,
)


class Menu:
    def __init__(self, usuario):
        self.usuario = usuario
        self.conn = ConexaoBanco.get_connection()
        if self.conn:
            self.cursor = self.conn.cursor()

    def exibe_grade_horaria(self):
        if self.usuario.tipo == "aluno":
            view_query = "SELECT * FROM grade_horaria_aluno_semana WHERE RA = %s"
            self.cursor.execute(view_query, (self.usuario.id,))
            resultados = self.cursor.fetchall()

            table = []
            # Exibir os resultados
            for linha in resultados:
                (
                    Aluno,
                    RA,
                    Curso,
                    Disciplina,
                    Dia_da_Semana,
                    Inicio,
                    Fim,
                    Modulo,
                ) = linha
                table.append([Disciplina, Dia_da_Semana, Inicio, Fim])
            print(
                tabulate(
                    table, headers=["Disciplina", "Dia da Semana", "Início", "Fim"]
                )
            )

        elif self.usuario.tipo == "professor":
            view_query = (
                "SELECT * FROM grade_horaria_professor_semana WHERE Matrícula = %s"
            )
            self.cursor.execute(view_query, (self.usuario.id,))
            resultados = self.cursor.fetchall()

            table = []
            # Exibir os resultados
            for linha in resultados:
                (
                    Professor,
                    Matrícula,  # ALTERAR PARA O NOME CORRETO QUE ESTIVER NO BANCO, O MEU TA EM INGLES POR ISSO MATRCULA
                    Curso,
                    Disciplina,
                    Dia_da_Semana,
                    Inicio,
                    Fim,
                    Modulo,
                    Periodo,
                ) = linha
                table.append([Dia_da_Semana, Disciplina, Inicio, Fim])
            print(
                tabulate(
                    table, headers=["Dia da Semana", "Disciplina", "Início", "Fim"]
                )
            )

    def sair(self):
        print("Saindo do sistema...")


class MenuAluno(Menu):
    def __init__(self, usuario):
        super().__init__(usuario)

    def menu_layout(self):
        print("\n--- Menu Aluno ---")
        print("1. Grade Horária")
        print("2. Faltas Totais")
        print("3. Presenças Totais")
        print("4. Escanear QR Code")
        print("5. Sair")

    def executar_opcao(self, opcao):
        # escolha = input("Escolha uma opção: ")
        if opcao == "1":
            self.exibe_grade_horaria()
        elif opcao == "2":
            self.exibe_faltas_totais()
        elif opcao == "3":
            self.exibe_presencas_totais()
        elif opcao == "4":
            self.escanear_qr_code()
        elif opcao == "5":
            self.sair()
        else:
            print("Opção inválida.")

    def exibe_faltas_totais(self):
        view_query = "SELECT * FROM historico_presenca_aluno WHERE RA = %s"
        self.cursor.execute(view_query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        table = []
        # Exibir os resultados
        for linha in resultados:
            (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
            table.append([Disciplina, TotalFaltas])
        print(tabulate(table, headers=["Disciplina", "Total de Faltas"]))

    def exibe_presencas_totais(self):
        view_query = "SELECT * FROM historico_presenca_aluno WHERE RA = %s"
        self.cursor.execute(view_query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        table = []
        # Exibir os resultados
        for linha in resultados:
            (RA, NomeAluno, Disciplina, TotalPresencas, TotalFaltas) = linha
            table.append([Disciplina, TotalPresencas])
        print(tabulate(table, headers=["Disciplina", "Total de Presenças"]))

    def escanear_qr_code(self):
        campus_nome = input(
            "Digite o nome do campus que está tendo aulas (mantiqueira, fazenda, palmeiras): "
        )
        # Definindo coordenadas fictícias do aluno
        coordenadas_aluno = LocalizacaoAluno(-21.96614140503053, -46.77420297206084)
        validacao = DistanciaAutorizada(coordenadas_aluno, campus_nome)
        if validacao.local_autorizado():
            print("Localização válida para escanear o QR code!")
        else:
            print("Você não está dentro da área permitida. Não pode gerar o QR Code")


class MenuProfessor(Menu):
    def __init__(self, usuario):
        super().__init__(
            usuario,
        )

    def menu_layout(self):
        print("\n--- Menu ---")
        print("1. Grade horária")
        print("2. Aula do dia")
        print("3. Relatório")
        print("4. Liberar QR Code ")
        print("5. Sair")

        # choice = input("Escolha uma opção: ")

    def executar_opcao(self, opcao):
        if opcao == "1":
            self.exibe_grade_horaria()

        elif opcao == "2":
            self.exibir_aula_dia()

        elif opcao == "3":
            self.relatorio()

        elif opcao == "4":
            self.liberar_qr_code()

        elif opcao == "5":
            self.sair()

    def exibir_aula_dia(self):
        view_query = "SELECT * FROM grade_horaria_professor_semana WHERE Matrícula = %s"
        self.cursor.execute(view_query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        table = []
        # Exibir os resultados
        for linha in resultados:
            (
                Professor,
                Matrícula,  # ALTERAR PARA O NOME CORRETO QUE ESTIVER NO BANCO, O MEU TA EM INGLES POR ISSO MATRCULA
                Curso,
                Disciplina,
                Dia_da_Semana,
                Inicio,
                Fim,
                Modulo,
                Periodo,
            ) = linha
            table.append([Dia_da_Semana, Disciplina])
            print(tabulate(table, headers=["Dia da semana", "Disciplina"]))

    def relatorio(self):
        query = """SELECT Disciplina, SUM(`Total Presencas`) AS TotalPresencas, SUM(`Total Faltas`) AS TotalFaltas
                    FROM historico_presenca_aluno
                    GROUP BY Disciplina"""
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        print("Resumo por Disciplina:")
        table = []
        for linha in resultados:
            disciplina, total_presencas, total_faltas = linha
            table.append([disciplina, total_presencas, total_faltas])
        print(
            tabulate(
                table,
                headers=["Disciplina", "Total de Presenças", "Total de Faltas"],
            )
        )

    def liberar_qr_code(self):
        pass
