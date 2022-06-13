from personagem import Personagem


class Login:

    def __init__(self, username: str, password: str):
        self.__username = username
        self._password = password
        self.__personagem_atual = None
        self.__personagens = []
        self.__logins = {}
        self.__logins[self] = self.__personagens

    def alterar_personagem(self, novo_personagem: Personagem):
        self.__personagem_atual = novo_personagem

    def mostrar_logins(self):
        for chave in self.__logins.keys():
            print(f'Chave = {chave.__username, chave._password} e Valor = {self.__logins[chave]}')


log1 = Login('enzo', '123')
log1.mostrar_logins()