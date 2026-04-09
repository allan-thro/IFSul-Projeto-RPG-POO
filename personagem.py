class Personagem:
    def __init__(self, nome:str):
        self.__nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def xp(self):
        return self.__xp
    
    @property
    def vida(self):
        return self.__vida
