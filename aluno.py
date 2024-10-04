# Classe Aluno, deve solicitar o RA e Senha caso esteja na localização permitida
from validacao_geografica import ValidacaoGeografica


class Aluno:
    def __init__(self, ra, senha):
        self.ra = ra
        self._senha = senha  # Senha como atributo privado

    def validar_ra_e_senha(self, ra_digitado, senha_digitada):
        return self.ra == ra_digitado and self._senha == senha_digitada


class LocalAluno(ValidacaoGeografica):
    def __init__(self, latitude, longitude, ra, senha):
        super().__init__(latitude, longitude)  # inicializa a classe ValidacaoGeografica
        self.aluno = Aluno(ra, senha)

    def verificar_acesso(self, latitude_permitida, longitute_permitida, raio_permitido):
        # Verifica se está na localização permitida
        if self.esta_dentro_do_raio(
            latitude_permitida, longitute_permitida, raio_permitido
        ):
            # se estivwer na área permitida, solicita RA e senha
            ra_inserido = input("Digite seu RA:")
            senha_inserida = input("Digite sua senha: ")
            if self.aluno.validar_ra_e_senha(ra_inserido, senha_inserida):
                print("Acesso concedido!")
            else:
                print("RA ou Senha incorretos. Tente novamente.")
        else:
            print("Você não está localizado na área permitida.")


# Exemplo de uso, criando o objeto (no caso, um aluno e seu local)
local_aluno = LocalAluno(-21.9700, -46.7700, "123456", "minha_senha")

# Coordenadas permitidas são as coordenadas do polo mantiqueira da UNIFEOB, e raio permitido de 1km
latitude_permitida = -21.966469960170866
longitute_permitida = -46.77255352511558
raio_permitido_km = 1

# Verificando se o aluno pode acessar o sistema
local_aluno.verificar_acesso(latitude_permitida, longitute_permitida, raio_permitido_km)
