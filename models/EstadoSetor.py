import cv2 as cv

from .Estado import Estado
from views import RenderizaSetor

class EstadoSetor(Estado):

    def __init__(self, *, imagem, callbackNavegarInput, callbackAtualizaPontosSetor, callbackObtemPontosSetor, opacidadeMarcacao, raioMarcacao, corMarcacao, zoomSetor):
        self.__imagem = imagem
        self.__callbackAtualizaPontosSetor = callbackAtualizaPontosSetor
        self.__callbackObtemPontosSetor = callbackObtemPontosSetor
        self.__zoomSetor = zoomSetor
        self.__renderizaSetor = RenderizaSetor(
            imagem = imagem,
            callbackMarcarElemento = self.__marcarElemento,
            callbackEncerrarSetor = callbackNavegarInput,
            opacidadeMarcacao = opacidadeMarcacao,
            raioMarcacao = raioMarcacao,
            corMarcacao = corMarcacao,
            zoomSetor = zoomSetor,
            ehNovaRenderizacao = self.obtemNovaRenderizacao,
            resetaPontosSetor = self.resetaPontosSetor
        )

    def obtemNovaRenderizacao(self):
        return self.__novaRenderizacao
    
    def resetaPontosSetor(self):
        self.__pontosSetor = []
        self.__atualizaPontosSetor()

    def __marcarElemento(self, x_event, y_event):
        self.__pontosSetor.append((x_event, y_event))
        self.__atualizaPontosSetor()

    def __atualizaPontosSetor(self):
        coordenadaInicial, _ = self.__imagem.obtemSetorSelecionado().obtemCoordenadas()
        pontosMarcados = [
            (
                coordenadaInicial[0] + round(x / self.__zoomSetor),
                coordenadaInicial[1] + round(y / self.__zoomSetor)
            )
            for x, y in self.__pontosSetor
        ]
        self.__callbackAtualizaPontosSetor(self.__imagem.obtemSetorAtual(), pontosMarcados)

    def __obtemPontosSetor(self):
        coordenadaInicial, _ = self.__imagem.obtemSetorSelecionado().obtemCoordenadas()
        return [
            (
                (x - coordenadaInicial[0]) * self.__zoomSetor,
                (y - coordenadaInicial[1]) * self.__zoomSetor
            )
            for x, y in self.__callbackObtemPontosSetor(self.__imagem.obtemSetorAtual())
        ]
     
    def iniciarEstado(self):
        self.__novaRenderizacao = True
        self.__pontosSetor = self.__obtemPontosSetor()

    def emExecucao(self):
        self.__renderizaSetor.renderizaSetor(list(self.__pontosSetor))
        self.__novaRenderizacao = False
    
    def sairEstado(self):
        cv.destroyWindow("Setor")
