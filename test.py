from missao import *

missaoExploracao = MissaoExploracao(
    "Em busca do java perdido",
    "Descubra pistas sobre onde foi parar o java da POO",
    15,
    "IFSul",
    3.5,
)

missaoCombate = MissaoCombate(
    "Derrote os goblins",
    "Derrota os globin ai",
    10,
    "Goblin",
    5,
)

missaoColeta = MissaoColeta(
    "Coleta de cristais magicos",
    "Colete os cristais magicos mais comuns do reino",
    2,
    "Normaluns Cristal",
    100
)

missaoExploracao.iniciar_missao()
missaoExploracao.concluir_missao()
missaoExploracao.exibir_dados()