from abc import ABC, abstractmethod

class Estado(ABC):

    def __init__(self, id, encerrarExecucao):
        self.__id = id
        self.__encerrarExecucao = encerrarExecucao

    @abstractmethod
    def iniciarEstado(self):
        pass

    @abstractmethod
    def emExecucao(self):
        pass
    
    @abstractmethod
    def sairEstado(self):
        pass