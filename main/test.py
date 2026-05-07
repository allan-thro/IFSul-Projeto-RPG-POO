from main.model.personagem.personagem import *
from main.model.missao.missao import *

buscaPeloJava = MissaoExploracao(
    "Em busca do java perdido",
    "Descubra pistas sobre onde foi parar o java da POO",
    15,
    "IFSul",
    3.5,
)

missaoCombate = MissaoCombate(
    "Derrote os goblins",
    "Derrota os globin aí",
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

detetive = Personagem(
    "sherlock Holmes"
)

detetive.add_missao(buscaPeloJava)
detetive.add_missao(missaoColeta)
detetive.add_missao(missaoCombate)

missaoColeta.iniciar_missao()
missaoCombate.iniciar_missao()

detetive.concluir_missao(missaoCombate, 6)
detetive.concluir_missao(missaoColeta, 50)

detetive.exibir_dados()


# teste push