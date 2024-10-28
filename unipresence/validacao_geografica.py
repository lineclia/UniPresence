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


class DistanciaAutorizada:
    def __init__(self, localizacao_aluno: LocalizacaoAluno, nome_campus: str):
        self.localizacao_aluno = localizacao_aluno
        self.campus = LocalizacaoCampus().get_campus(nome_campus)

    def local_autorizado(self):
        raio_permitido = 0.5  # 50 metros em quilômetros
        coordenadas_aluno = self.localizacao_aluno.get_coordenadas()
        distancia = geodesic(coordenadas_aluno, self.campus).km
        return distancia <= raio_permitido
