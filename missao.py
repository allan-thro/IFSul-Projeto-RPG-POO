from Enumerators import Status

class Missao:
    def __init__(self, nome:str, descricao:str, recompensa:int, status:Status = Status.PENDENTE):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = status

    def __eq__(self, value):
        return self.nome == value.nome and self.status == value.status

    def __str__(self):
        return f"Missão: {self.nome}"

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
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def status(self):
        return self.__status
    
    @nome.setter
    def nome(self, nome:str):
        if nome is None: raise Exception("Nome nao pode ser nulo")

        palavras = nome.split(" ")
        validas = []
     
        for s in palavras:
            if(len(s.strip()) != 0):
                validas.append(s.strip())

        nome_ajustado = " ".join(validas)

        self.__nome = nome_ajustado

    @recompensa.setter
    def recompensa(self, recompensa:int):
        if recompensa is None: raise Exception("Recompensa nao pode ser nulo")
        if recompensa > 50 or recompensa < 1: raise Exception("Valores fora do intervalo permitido [1, 50]")
        self.__recompensa = recompensa

    @status.setter
    def status(self, novo_status: Status):
        if novo_status is None: 
            raise Exception("Status nao pode ser nulo")
        
    
        if (self.status == Status.PENDENTE and novo_status != Status.EM_ANDAMENTO or
            self.status == Status.EM_ANDAMENTO and novo_status != Status.CONCLUIDA or
            self.status == Status.CONCLUIDA): 
            
            raise Exception("Ordem de alteração incorreta: PENDENTE -> EM ANDAMENTO -> CONCLUIDA")
        
        
        self._Missao__status = novo_status

    @descricao.setter
    def descricao(self, descricao:str):
        if descricao is None: raise Exception("Descricao nao pode ser nulo")
        self.__descricao = descricao

    
class MissaoCombate(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:int, tipo_inimigo:str, inimigos_a_derrotar:int, status:Status = Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)   

        self.__inimigos_a_derrotar = inimigos_a_derrotar
        self.__tipo_inimigo = tipo_inimigo

    def concluir_missao(self, parametro):
        if not isinstance(parametro, int): raise Exception("Inimigos derrotados deve ser numérico")

        if(parametro >= self.inimigos_a_derrotar and self.status == Status.EM_ANDAMENTO):
            print(f"Missão concluida com sucesso! Todos os inimigos foram derrotados")
            self.status = Status.CONCLUIDA
        elif(parametro >= self.inimigos_a_derrotar):
            print(f"Status da missão incorreto: {self.status}")
        


    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo

    @tipo_inimigo.setter
    def tipo_inimigo(self, tipo_inimigo:str):
        self.__tipo_inimigo = tipo_inimigo

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, inimigos_a_derrotar:int):
        self.__inimigos_a_derrotar = inimigos_a_derrotar
    
    
class MissaoColeta(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:int, item_necessario:str, quantidade_item:int, status:Status = Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)       

        self.__item_necessario = item_necessario
        self.__quantidade_item = quantidade_item

    

    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo

    @tipo_inimigo.setter
    def tipo_inimigo(self, tipo_inimigo:str):
        if tipo_inimigo is None: raise Exception("Tipo de inimigo não pode ser nulo")
        self.__tipo_inimigo = tipo_inimigo

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, inimigos_a_derrotar:int):
        if inimigos_a_derrotar <= 0: raise Exception("Quantidade de inimigos deve ser maior que zero")
        self.__inimigos_a_derrotar = inimigos_a_derrotar

class MissaoExploracao(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:int, regiao_destino:str, distancia_em_km:float, status:Status = Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        
        self.__distancia_em_km = distancia_em_km
        self.__regiao_destino = regiao_destino

    @property
    def regiao_destino(self):
        return self.__regiao_destino

    @regiao_destino.setter
    def regiao_destino(self, regiao_destino: str):
        if regiao_destino is None: raise Exception("Região de destino não pode ser nula")
        self.__regiao_destino = regiao_destino

    @property
    def distancia_em_km(self):
        return self.__distancia_em_km

    @distancia_em_km.setter
    def distancia_em_km(self, distancia_em_km: float):
        if distancia_em_km < 0: raise Exception("Distância não pode ser negativa")
        self.__distancia_em_km = distancia_em_km

