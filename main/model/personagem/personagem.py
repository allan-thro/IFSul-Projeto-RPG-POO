from typing import Optional

from main.model.inventario.item import Item
from main.model.missao.missao import *

from dataclasses import dataclass, field


@dataclass
class Personagem:
    nome : str
    vida : int = 100
    ataqueBase : float = 2.0
    nivel : int = 1
    xp : int = 0
    armaEquipada : Optional[Item] = None
    vestimentaEquipada : Optional[Item] = None
    utilitarioEquipado : Optional[Item] = None
    missaoList : list = field(default_factory=list)
    inventario : list = field(default_factory=list)

    def add_missao(self, missao:Missao):
        for m in self.missaoList:
            if(m == missao):
                raise Exception("Missão Duplicada")
        self.missaoList.append(missao)

    def concluir_missao(self, missao:Missao, valor):
        for m in self.missaoList:
            if(m == missao):
                m.concluir_missao(valor)
                return 
        
        raise Exception("Missão não pertence a esse jogador para ser concluida")
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nNível: {self.nivel}\nVida: {self.vida}\nXp: {self.xp}Lista Missões: ")
        for m in self.missaoList:
            print(m.exibir_dados())
            print("\n")