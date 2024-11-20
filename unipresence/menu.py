from bd import ConexaoBanco
from tabulate import tabulate

# from aluno import Aluno
from validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
    # LocalizacaoCampus,
)


class Menu:
    def __init__(self, usuario):
        self.usuario = usuario
        self.conn = ConexaoBanco.get_connection()
        if self.conn:
            self.cursor = self.conn.cursor(dictionary = True)

    def exibe_grade_horaria(self):
        # print(f"RA fornecido: {self.usuario.id}")
        print(f"Tipo de usuario: {self.usuario.tipo}")
        query = None

        if self.usuario.tipo == "aluno":
            query = "SELECT * FROM grade_horaria_aluno_semana WHERE RA = %s"
            self.cursor.execute(query, (self.usuario.id,))  # Substituir pelo RA do aluno
        #resultados = self.cursor.fetchall()
        elif self.usuario.tipo == "professor":
            query = "SELECT * FROM grade_horaria_professor_semana WHERE Matrícula = %s"
            self.cursor.execute(query, (self.usuario.id,))  # Substituir pela matricula do professor


        resultados = self.cursor.fetchall()
       # print("Resultados da query:", resultados)

       # if self.usuario.tipo == "aluno":
        #    view_query = "SELECT * FROM grade_horaria_aluno_semana WHERE RA = %s"
         #   self.cursor.execute(view_query, (self.usuario.id,))
          #  resultados = self.cursor.fetchall()

        if not resultados:
            print("Nenhuma grade horária encontrada para o RA fornecido.")
            return

        table = []
            # Exibir os resultados
        if self.usuario.tipo == "aluno":
            for linha in resultados:
               # aluno = linha["Aluno"]
                #ra = linha["RA"]
                #curso = linha["Curso"]
                disciplina = linha["Disciplina"]
                dia_da_semana = linha.get("Dia da Semana", "N/A")
                inicio = linha["Início"]
                fim = linha["Fim"]
            #    modulo = linha["Módulo"]    
                table.append([disciplina, dia_da_semana, inicio, fim])
            print(
                tabulate(
                    table,  # A lista contendo os dados
                    headers=["Disciplina", "Dia da Semana", "Início", "Fim"],  # Cabeçalhos das colunas
                    tablefmt="grid",  # Formato da tabela (pode usar "plain", "grid", etc.)
                )
            )
        elif self.usuario.tipo == "professor":
            #view_query = (
             #   "SELECT * FROM grade_horaria_professor_semana WHERE Matrícula = %s"
            #)
            #self.cursor.execute(view_query, (self.usuario.id,))
            #resultados = self.cursor.fetchall()

            #table = []
            # Exibir os resultados
            for linha in resultados:
                
                #professor = linha["Professor"]
                #matricula = linha["Matrícula"]
                #curso = linha["Curso"]
                disciplina = linha.get("Disciplina", "N/A")  # Usando o valor padrão "N/A" se "Disciplina" for None"Disciplina"]
                dia_da_semana = linha.get("Dia da Semana", "N/A")
                inicio = linha.get("Início", "N/A")
                fim = linha.get("Fim", "N/A")
                #modulo = linha["Modulo"]
                #periodo = linha["Periodo"]
                
                table.append([dia_da_semana, disciplina, inicio, fim])
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
        query = "SELECT Disciplina, `Total Faltas` FROM historico_presenca_aluno WHERE RA = %s"
        self.cursor.execute(query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        if not resultados:
            print(f"Nenhuma falta registrada para o RA:{self.usuario.id}")
            return

        table = []
        # Exibir os resultados
        for linha in resultados:
            disciplina = linha.get("Disciplina", "N/A")
            total_faltas = linha.get("Total Faltas", "N/A")
            table.append([disciplina, total_faltas])
        print(tabulate(table, headers=["Disciplina", "Total de Faltas"]))

    def exibe_presencas_totais(self):
        view_query = "SELECT Disciplina, `Total Presencas` FROM historico_presenca_aluno WHERE RA = %s"
        self.cursor.execute(view_query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        table = []
        # Exibir os resultados
        for linha in resultados:
            disciplina = linha.get("Disciplina", "N/A")
            total_presencas = linha.get("Total Presencas", "N/A")
            table.append([disciplina, total_presencas])
            
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
        query = "SELECT `Dia da Semana`, Disciplina FROM grade_horaria_professor_semana WHERE Matrícula = %s"
        self.cursor.execute(query, (self.usuario.id,))
        resultados = self.cursor.fetchall()

        table = []
        # Exibir os resultados
        for linha in resultados:
            disciplina = linha.get("Disciplina", "N/A")
            dia_da_semana = linha.get("Dia da Semana", "N/A")
           
            table.append([dia_da_semana, disciplina])
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
            disciplina = linha.get("Disciplina", "N/A")
            total_presencas = linha.get("TotalPresencas", "N/A")
            total_faltas = linha.get("TotalFaltas", "N/A")
            table.append([disciplina, total_presencas, total_faltas])
        print(
            tabulate(
                table,
                headers=["Disciplina", "Total de Presenças", "Total de Faltas"],
            )
        )

    def liberar_qr_code(self):
        pass
