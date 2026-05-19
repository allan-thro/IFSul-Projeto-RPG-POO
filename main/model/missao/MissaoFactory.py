from missao import *
from main.enums.missao.missaoEnum import TipoMissao
class MissaoFactory:

    @staticmethod
    def criarMissao(tipoMissao:TipoMissao, nome, descricao, recompensa, **args):
        match tipoMissao:
            case TipoMissao.COMBATE:
                return MissaoCombate(nome, descricao, recompensa, Status.PENDENTE, args.get("tipoInimigo"), args.get("qtdInimigos"))
            case TipoMissao.COLETA:
                return MissaoColeta(nome, descricao, recompensa, Status.PENDENTE, args.get("itemNecessario"), args.get("quantidadeItens"))
            case TipoMissao.EXPLORACAO:
                return MissaoExploracao(nome, descricao, recompensa, Status.PENDENTE, args.get("regiaoDestino"), args.get("distanciaEmKm"))
            case _:
                raise Exception("Tipo missão inválido")