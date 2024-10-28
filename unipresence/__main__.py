from unipresence.aluno import Aluno, ValidarLocal
from unipresence.professor import Professor
from unipresence.validacao_geografica import LocalizacaoAluno


def main():
    #  Exemplo de criação de aluno e verificação de localização antes do login
    aluno = Aluno(
        ra=123456,
        senha="minhasenha",
        nome="Lívia",
        curso="ADS",
        periodo="Noturno",
        semestre=2,
        modulo=1,
    )

    professor = Professor(rm=1111, nome="Marcelo", senha="senha")

    localizacao_aluno = LocalizacaoAluno(-21.96613986612555, -46.77416860602757)
    nome_campus = "mantiqueira"

    # Verificar se o aluno está em uma localização autorizada
    validador_local = ValidarLocal(localizacao_aluno, nome_campus)
    if validador_local.local_autorizado():
        aluno.login()  # Solicita RA e senha
    else:
        print("Acesso negado devido à localização.")

    professor.login()


if __name__ == "__main__":
    main()


# Observações a corrigir:
# apesar de perguntar se é aluno ou professor, e de ir pro login correto (RA p aluno e RM p prof)
# no primeiro momento, ele valida o aluno, principalmente pq eu pedi p validar o local
# e no segundo momento, em professor.login() ele faz o login com as credenciais do prof que criei
# mesmo perguntando antes de sou aluno ou professor
