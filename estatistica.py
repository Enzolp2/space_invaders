

class Estatistica:

    def __init__(self, num_onda: int, inimigos_derrotados: int, tempo_partida: int):
        self.__num_onda = num_onda
        self.__inimigos_derrotados = inimigos_derrotados
        self.__tempo_partida = tempo_partida

    @property
    def num_onda(self):
        return self.__num_onda

    @num_onda.setter
    def num_onda(self, num_onda):
        self.__num_onda = num_onda

    @property
    def inimigos_derrotados(self):
        return self.__inimigos_derrotados

    @inimigos_derrotados.setter
    def inimigos_derrotados(self, inimigos_derrotados):
        self.__inimigos_derrotados = inimigos_derrotados

    @property
    def tempo_partida(self):
        return self.__tempo_partida

    @tempo_partida.setter
    def tempo_partida(self, tempo_partida):
        self.__tempo_partida = tempo_partida

    def mostrar_estatistica(self):
        pass
