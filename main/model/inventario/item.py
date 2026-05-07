from dataclasses import dataclass

from main.enums.inventario.inventarioEnum import TipoItem

@dataclass
class Item():
    nome : str
    descricao : str
    valorEfeito : float
    tipo : TipoItem
