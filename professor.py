#Classe professor, deve solicitar as credenciais (email institucional e senha) e fazer o login
# 
class Professor:
    def __init__(self, email, senha):
        self.email = email
        self._senha = senha #Senha como atributo privado

    def validar_email_e_senha(self, email_digitado, senha_digitado):
        return self.email == email_digitado and self._senha == senha_digitado

#Exemplo de uso, criando um objeto (no caso, um professor)
professor1 = Professor("professor1@email.com", "minha_senha")

#Validando acesso
email_inserido = input("Digite seu email institucional: ") 
senha_inserida = input("Digite sua senha: ")

if professor1.validar_email_e_senha(email_inserido,senha_inserida):
    print("Acesso concedido!")
else:
    print("Email ou Senha incorretos. Tente novamente.")