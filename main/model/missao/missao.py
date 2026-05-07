from dataclasses import dataclass

from main.enums.missao.missaoEnum import Status

@dataclass
class Missao:
    _nome: str
    _descricao: str
    _recompensa: int
    _status: Status = Status.PENDENTE

    def __post_init__(self):
        self.nome = self._nome
        self.descricao = self._descricao
        self.recompensa = self._recompensa
        self.status = self._status

    def exibir_dados(self):
        print(f"Missão: {self.nome}\nRecompensa: {self.recompensa}\nStatus: {self.status.value}\nDescrição: {self.descricao}")

    def iniciar_missao(self):
        if self.status == Status.PENDENTE:
            print(f"A missão {self.nome} começou! Objetivo central da missão: {self.descricao}")
            self.status = Status.EM_ANDAMENTO
        else:
            print(f"Missão com status indevido: {self.status}")

    def concluir_missao(self, parametro):
        pass 

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def recompensa(self):
        return self._recompensa
    
    @property
    def status(self):
        return self._status
    
    @nome.setter
    def nome(self, nome: str):
        if nome is None:
            raise Exception("Nome nao pode ser nulo")

        palavras = nome.split(" ")
        validas = [] 
        
        for s in palavras:
            if len(s.strip()) != 0:
                validas.append(s.strip())

        self._nome = " ".join(validas)

    @descricao.setter
    def descricao(self, descricao: str):
        if descricao is None:
            raise Exception("Descricao nao pode ser nulo")
        self._descricao = descricao

    @recompensa.setter
    def recompensa(self, recompensa: int):
        if recompensa is None:
            raise Exception("Recompensa nao pode ser nulo")
        if recompensa > 50 or recompensa < 1:
            raise Exception("Valores fora do intervalo permitido [1, 50]")
        self._recompensa = recompensa

    @status.setter
    def status(self, novo_status: Status):
        if novo_status is None:
            raise Exception("Status nao pode ser nulo")

        if (
            (self._status == Status.PENDENTE and novo_status != Status.EM_ANDAMENTO) or
            (self._status == Status.EM_ANDAMENTO and novo_status != Status.CONCLUIDA) or
            (self._status == Status.CONCLUIDA)
        ):
            raise Exception("Ordem de alteração incorreta: PENDENTE -> EM ANDAMENTO -> CONCLUIDA")

        self._status = novo_status
        
    
# ---------//--------- #


@dataclass
class MissaoCombate(Missao):
    _tipo_inimigo: str
    _inimigos_a_derrotar: int

    def __post_init__(self):
        super().__post_init__()

        self.tipo_inimigo = self._tipo_inimigo
        self.inimigos_a_derrotar = self._inimigos_a_derrotar

    def concluir_missao(self, parametro):
        if not isinstance(parametro, int):
            raise Exception("Inimigos derrotados deve ser numérico")

        if parametro >= self._inimigos_a_derrotar and self.status == Status.EM_ANDAMENTO:
            print("Missão concluída com sucesso! Todos os inimigos foram derrotados")
            self.status = Status.CONCLUIDA

        elif parametro >= self._inimigos_a_derrotar:
            print(f"Status da missão incorreto: {self.status}")

        else:
            print(f"Inimigos insuficientes. Derrotados: {parametro}, Esperado: {self._inimigos_a_derrotar}")

    @property
    def tipo_inimigo(self):
        return self._tipo_inimigo

    @tipo_inimigo.setter
    def tipo_inimigo(self, tipo_inimigo: str):
        if tipo_inimigo is None:
            raise Exception("Tipo de inimigo não pode ser nulo")
        self._tipo_inimigo = tipo_inimigo

    @property
    def inimigos_a_derrotar(self):
        return self._inimigos_a_derrotar

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, inimigos_a_derrotar: int):
        if inimigos_a_derrotar is None or inimigos_a_derrotar <= 0:
            raise Exception("Quantidade inválida de inimigos")
        self._inimigos_a_derrotar = inimigos_a_derrotar
    

# ---------//--------- #


@dataclass
class MissaoColeta(Missao):
    _item_necessario: str
    _quantidade_item: int

    def __post_init__(self):
        super().__post_init__()

        self.item_necessario = self._item_necessario
        self.quantidade_item = self._quantidade_item

    def concluir_missao(self, parametro):
        if not isinstance(parametro, int):
            raise Exception("Quantidade coletada deve ser numérico")

        if parametro >= self._quantidade_item and self.status == Status.EM_ANDAMENTO:
            print("Missão concluída com sucesso! Todos os itens foram coletados!")
            self.status = Status.CONCLUIDA

        elif parametro >= self._quantidade_item:
            print(f"Status da missão incorreto: {self.status}")

        else:
            print(f"Objetos insuficientes. Coletado: {parametro}, Esperado: {self._quantidade_item}")

    @property
    def item_necessario(self):
        return self._item_necessario

    @item_necessario.setter
    def item_necessario(self, item_necessario: str):
        if item_necessario is None:
            raise Exception("Item necessário não pode ser nulo")
        self._item_necessario = item_necessario

    @property
    def quantidade_item(self):
        return self._quantidade_item

    @quantidade_item.setter
    def quantidade_item(self, quantidade_item: int):
        if quantidade_item is None or quantidade_item <= 0:
            raise Exception("Quantidade deve ser maior que zero")
        self._quantidade_item = quantidade_item


# ---------//--------- #


@dataclass
class MissaoExploracao(Missao):
    _regiao_destino: str
    _distancia_em_km: float

    def __post_init__(self):
        super().__post_init__()

        self.regiao_destino = self._regiao_destino
        self.distancia_em_km = self._distancia_em_km

    @property
    def regiao_destino(self):
        return self._regiao_destino

    @regiao_destino.setter
    def regiao_destino(self, regiao_destino: str):
        if regiao_destino is None:
            raise Exception("Região de destino não pode ser nula")
        self._regiao_destino = regiao_destino

    @property
    def distancia_em_km(self):
        return self._distancia_em_km

    @distancia_em_km.setter
    def distancia_em_km(self, distancia_em_km: float):
        if distancia_em_km is None or distancia_em_km < 0:
            raise Exception("Distância não pode ser negativa")
        self._distancia_em_km = distancia_em_km


    """def concluir_missao(self, parametro): <- concluir missão não definido
        if not isinstance(parametro, float): raise Exception("Quantidade coletada deve ser numérico")

        if(parametro >= self.__item_necessario and self.__status == Status.EM_ANDAMENTO):
            print(f"Missão concluida com sucesso! Todos os itens forma coletados!")
            self.status = Status.CONCLUIDA
        elif(parametro >= self.__item_necessario):
            print(f"Status da missão incorreto: {self.status}")
        else:
            print(f"Objetos insuficientes. Coletado: {parametro}, Esperado: {self.__item_necessario}")"""