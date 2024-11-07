from geopy.distance import geodesic


class LocalizacaoCampus:
    def __init__(self):
        self.__campus_mantiqueira_coords = (-21.966571251651015, -46.77271231380196)
        self.__campus_fazenda_coords = (-21.959124918142102, -46.75541626064883)
        self.__palmeiras_coords = (-21.973273070543343, -46.79749880108253)

    def get_campus(self, nome):
        if nome == "mantiqueira":
            return self.__campus_mantiqueira_coords
        elif nome == "fazenda":
            return self.__campus_fazenda_coords
        elif nome == "palmeiras":
            return self.__palmeiras_coords
        else:
            raise ValueError("Campus não encontrado")


class LocalizacaoAluno:
    def __init__(self, latitude: float, longitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_coordenadas(self):
        return (self.__latitude, self.__longitude)


class DistanciaAutorizada(LocalizacaoAluno):
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.localizacao_aluno = localizacao_aluno
        self.campus = LocalizacaoCampus().get_campus(nome_campus)

    def local_autorizado(self):
        raio_permitido = 0.3  # 50 metros
        coordenadas_aluno = self.localizacao_aluno.get_coordenadas()
        distancia = geodesic(coordenadas_aluno, self.campus).km
        return distancia <= raio_permitido

    def validar_localizacao(self, campus_nome):
        if not self.localizacao:
            self.localizacao = self.obter_localizacao()
        coordenadas_campus = LocalizacaoCampus().get_campus(campus_nome)
        validacao = DistanciaAutorizada(self.localizacao, coordenadas_campus)
        if validacao.local_autorizado():
            return True
        else:
            return False


def validar_localizacao(self, campus_nome):
    if not self.localizacao:
        self.localizacao = self.obter_localizacao()
    coordenadas_campus = LocalizacaoCampus().get_campus(campus_nome)
    validacao = DistanciaAutorizada(self.localizacao, coordenadas_campus)
    if validacao.local_autorizado():
        print("Localização autorizada.")
        return True
    else:
        print("Localização fora do permitido")
        return False
