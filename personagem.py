from missao import *

class Personagem:
    def __init__(self, nome:str):
        self.__nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__missaoList = []
    
    def add_missao(self, missao:Missao):
        for m in self.__missaoList:
            if(m == missao):
                raise Exception("Missão Duplicada")
        self.__missaoList.append(missao)

    def concluir_missao(self, missao:Missao, valor):
        for m in self.__missaoList:
            if(m == missao):
                m.concluir_missao(valor)
                return 
        
        raise Exception("Missão não pertence a esse jogador para ser concluida")
    
    def exibir_dados(self):
        print(f"Nome: {self.__nome}\nNível: {self.__nivel}\nVida: {self.__vida}\nXp: {self.__xp}Lista Missões: ")
        for m in self.__missaoList:
            print(m.exibir_dados())
            print("\n")

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
