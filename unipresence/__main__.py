# from unipresence.professor import Professor
# from unipresence.validacao_geografica import LocalizacaoAluno, DistanciaAutorizada
from unipresence.aluno import Aluno
from unipresence.professor import Professor
# from unipresence.aluno import MenuAluno
# from unipresence.professor import MenuProfessor
# from unipresence.interfaces import PessoaInterface


# Uso no main
def main():
    tipo_usuario = (
        input("Você quer fazer login como Aluno ou Professor?").strip().lower()
    )

    if tipo_usuario == "aluno":
        aluno = Aluno()
        aluno.login()

    elif tipo_usuario == "professor":
        professor = Professor()
        professor.login()

    else:
        print("tipo de usuário inválido. Por favor, escolha 'aluno' ou 'professor'.")


if __name__ == "__main__":
    main()
# -21.966903750276316, -46.77295740777025
