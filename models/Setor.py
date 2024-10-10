class Setor:
    def __init__(self, *, coordenadaInicial, coordenadaFinal):
        self.__coordenadaInicial = coordenadaInicial
        self.__coordenadaFinal = coordenadaFinal
        self.__contagem = 0
        self.__contabilizado = False

    def obtemCoordenadas(self):
        return self.__coordenadaInicial, self.__coordenadaFinal
    
    def obtemContagem(self):
        return self.__contagem
    
    def obtemContabilizado(self):
        return self.__contabilizado
    
    def defineContagem(self, contagem):
        self.__contagem = contagem
    
    def defineContabilizado(self, contabilizado):
        self.__contabilizado = contabilizado
    