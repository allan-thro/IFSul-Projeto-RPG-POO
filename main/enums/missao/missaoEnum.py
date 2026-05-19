from enum import Enum

class Status(Enum):
    PENDENTE = ("Pendente")
    EM_ANDAMENTO = ("Em Andamento")
    CONCLUIDA = ("Concluida")
    FRACASSADA = ("Fracassada")

class TipoMissao(Enum):
    COLETA = ("Coleta")
    COMBATE = ("Combate")
    EXPLORACAO = ("Exploração")