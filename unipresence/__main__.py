from unipresence.aluno import Aluno
from unipresence.professor import Professor


# Uso no main
def main():
    tipo_usuario = (
        input("Você quer fazer login como Aluno ou Professor?").strip().lower()
    )

    if tipo_usuario == "aluno":
        aluno = Aluno()
        aluno.login(tipo="aluno")

    elif tipo_usuario == "professor":
        professor = Professor()
        professor.login(tipo="professor")

    else:
        print("tipo de usuário inválido. Por favor, escolha 'aluno' ou 'professor'.")


if __name__ == "__main__":
    main()
# -21.966903750276316, -46.77295740777025
