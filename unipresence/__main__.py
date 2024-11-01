# from unipresence.professor import Professor
# from unipresence.validacao_geografica import LocalizacaoAluno, DistanciaAutorizada
from unipresence.aluno import Aluno
from unipresence.professor import Professor
from unipresence.interfaces import PessoaInterface


# Uso no main
def main():
    def processar_login(pessoa: PessoaInterface):
        pessoa.login()

    aluno1 = Aluno(123456, "minhasenha", "Lívia")
    professor1 = Professor(1111, "senha", "Marcelo")

    processar_login(aluno1)  # Chama login do aluno
    processar_login(professor1)  # Chama login do professor

    # #  Exemplo de criação de aluno e verificação de localização antes do login
    # aluno1 = Aluno(123456, "minhasenha", "Lívia")

    # professor1 = Professor(1111, "senha", "Marcelo")

    # localizacao_aluno = LocalizacaoAluno(-21.96613986612555, -46.77416860602757)
    # nome_campus = "mantiqueira"

    # # Verificar se o aluno está em uma localização autorizada
    # validador_local = DistanciaAutorizada(localizacao_aluno, nome_campus)
    # if validador_local.local_autorizado():
    #     aluno1.login()  # Solicita RA e senha
    # else:
    #     print("Acesso negado devido à localização.")

    # professor1.login()  # Solicita RM e senha do professor


if __name__ == "__main__":
    main()


# Observações a corrigir:
# apesar de perguntar se é aluno ou professor, e de ir pro login correto (RA p aluno e RM p prof)
# no primeiro momento, ele valida o aluno, principalmente pq eu pedi p validar o local
# e no segundo momento, em professor.login() ele faz o login com as credenciais do prof que criei
# mesmo perguntando antes de sou aluno ou professor
