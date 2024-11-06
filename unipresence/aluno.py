from unipresence.validacao_geografica import (
    LocalizacaoAluno,
    DistanciaAutorizada,
)

from unipresence.usuario import Usuario


class Aluno(Usuario):
    def __init__(self):
        super().__init__(tipo="aluno")
        self.ra = None

    def obter_localizacao(self):
        return LocalizacaoAluno(-21.966449325239303, -46.77464406560066)
        # TODO: encontrar outra forma; possivelmente API do google
        # usando o geocoder para pegar a localização através no IP (para a simulação)
        # g = geocoder.ipinfo("187.183.58.57")
        # if g.ok:
        #     self.localizacao = LocalizacaoAluno(g.latlng[0], g.latlng[1])
        # else:
        #     print("Não foi possível obter a localizaçao.")

    def validar_localizacao(self, campus_nome):
        if not self.localizacao:
            self.obter_localizacao()
        validacao = DistanciaAutorizada(self.localizacao, campus_nome)
        if validacao.local_autorizado():
            print("Localização autorizada.")
            return True
        else:
            print("Localização fora do permitido")
            return False

    def login(self, ra: int, senha: str):
        return super().login(ra, senha)
