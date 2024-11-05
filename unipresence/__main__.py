from unipresence.aluno import Aluno
from unipresence.professor import Professor


# # Uso no main
def main():
    tipo_usuario = (
        input("Você quer fazer login como Aluno ou Professor?").strip().lower()
    )
    if tipo_usuario not in ["aluno", "professor"]:
        print("Tipo de usuário inválido. Por favor escolha 'aluno' ou 'professor'")
        return

    if tipo_usuario == "aluno":
        usuario = Aluno()

    elif tipo_usuario == "professor":
        usuario = Professor()

    usuario.login()


if __name__ == "__main__":
    main()

# # -21.966903750276316, -46.77295740777025
# 24000001
# 19976457
