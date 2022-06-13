from estatistica import Estatistica


class Personagem:
    def __init__(self, nome: str, vida: int, vel_movimento: int,
                 dano: int, vel_tiro: int):
        self.__nome = nome
        self.__vida = vida
        self.__vel_movimento = vel_movimento
        self.__dano = dano
        self.__vel_tiro = vel_tiro
        self.__estatistica = Estatistica(0, 0, 0)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self, dano):
        self.__dano = dano

    @property
    def vel_tiro(self):
        return self.__vel_tiro

    @vel_tiro.setter
    def vel_tiro(self, vel_tiro):
        self.__vel_tiro = vel_tiro

    # iniciar um novo jogo (chama a instância da classe Jogo)
    def novo_jogo(self):
        pass

    # mostra as estatisticas do personagem
    def estatistica(self):
        pass

