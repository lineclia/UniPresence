import math

#Nesse primeiro momento o código irá verificar apenas a localização do Campus Mantiqueira
#Coordenadas do polo: -21.966469960170866, -46.77255352511558

class ValidacaoGeografica:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # Método para validar se a localização atual está dentro do raio permitido
    def esta_dentro_do_raio(self, latitude_permitida, longitude_permitida, raio_km):
        # Cálculo da distância usando Haversine
        distancia = self.calcular_distancia(latitude_permitida, longitude_permitida)
        return distancia <= raio_km

    # Método para calcular a distância entre dois pontos geográficos
    def calcular_distancia(self, outra_latitude, outra_longitude):
        # Conversão de graus para radianos
        lat1, lon1 = math.radians(self.latitude), math.radians(self.longitude)
        lat2, lon2 = math.radians(outra_latitude), math.radians(outra_longitude)

        # Fórmula de Haversine
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Raio da Terra em km
        raio_terra_km = 6371
        distancia = raio_terra_km * c
        return distancia

# Exemplo de uso
# Coordenadas da localização do usuário (exemplo)
localizacao_usuario = ValidacaoGeografica(-21.9700, -46.7700) 
# Exemplo de coordenadas do usuário
#esse dado teria de vir da utilização do GPS pelo dispositivo do aluno/professor

# Coordenadas permitidas do polo mantiqueira
coordenadas_permitidas = [
    (-21.966469960170866, -46.77255352511558)  
]

# Raio permitido de 1 km
raio_permitido_km = 1

# Verificar se o usuário está dentro da coordenada permitida
acesso_liberado = False
for coord in coordenadas_permitidas:
    if localizacao_usuario.esta_dentro_do_raio(coord[0], coord[1], raio_permitido_km):
        acesso_liberado = True
        break

if acesso_liberado:
    print("Acesso permitido.")
else:
    print("Acesso negado.")