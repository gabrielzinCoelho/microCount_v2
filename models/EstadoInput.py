from .Estado import Estado
from views import RenderizaInput

class EstadoInput(Estado):

    def __init__(self, *, imagem, callbackEncerrarInput):
        self.__renderizaInput = RenderizaInput(imagem = imagem)
        self.__callbackEncerrarInput = callbackEncerrarInput

    def iniciarEstado(self):
        pass

    def emExecucao(self):
        self.__renderizaInput.renderizaInput()
        self.__callbackEncerrarInput()
    
    def sairEstado(self):
        pass

    