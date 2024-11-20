from usuario import Usuario
from menu import MenuAluno, MenuProfessor
from aluno import Aluno
from professor import Professor


# # Uso no main
def main():
    tipo_usuario = (
        input("Você quer fazer login como Aluno ou Professor? ").strip().lower()
    )
    if tipo_usuario not in ["aluno", "professor"]:
        print("Tipo de usuário inválido. Por favor escolha 'aluno' ou 'professor'")
        return

    usuario = Usuario(tipo=tipo_usuario)

    if usuario.login():
        if tipo_usuario == "aluno":
            aluno = Aluno()
            aluno.id = usuario.id
            aluno.senha = usuario.senha
            menu = MenuAluno(usuario)
        elif tipo_usuario == "professor":
            professor = Professor()
            professor.id = usuario.id
            professor.senha = usuario.senha
            menu = MenuProfessor(usuario)

        while True:
            menu.menu_layout()
            opcao = input("escolha uma opção: ")
            menu.executar_opcao(opcao)
            if opcao == "5":
                break

    else:
        print(f"Falha no login como {tipo_usuario.capitalize()}")


if __name__ == "__main__":
    main()

# # -21.966903750276316, -46.77295740777025
# 24000001 -- aluno ra
# 19976457 -- aluno senha

# 123456 -- matricula prof
# 20683234 -- senha prof
