
import cv2 as cv

from .Estado import Estado
from views import RenderizaImagem

class EstadoImagem(Estado):

    def __init__(self, *, imagem, encerrarExecucao, fonteTexto, escalaTexto, corTexto, espessuraTexto, corLinha, espessuraLinha, opacidadeLinha):
        super().__init__()
        self.__imagem = imagem
        self.__renderizaImagem = RenderizaImagem(
            imagem = imagem, 
            callbackQuadroSelecionado = self.selecionarQuadro,
            callbackFecharImagem = encerrarExecucao,
            fonteTexto = fonteTexto,
            escalaTexto = escalaTexto,
            corTexto = corTexto,
            espessuraTexto = espessuraTexto,
            corLinha = corLinha,
            espessuraLinha = espessuraLinha,
            opacidadeLinha = opacidadeLinha
        )
        self.__modoVisualizacao = 0

    def selecionarQuadro(self, x_event, y_event):
        setorSelecionado = ((y_event // self.__imagem.saltoLinha) * self.__imagem.numeroColunas) + (x_event // self.__imagem.saltoColuna)
        self.__imagem.setorAtual = setorSelecionado

        if self.__imagem.setores[setorSelecionado].contabilizado:
            self.__imagem.resetaContagemSetorAtual()
            self.__atualizarImagem()

    def iniciarEstado(self):
        pass

    def emExecucao(self):
        self.__renderizaImagem.atualizaImagem()
        cv.destroyWindow("Imagem")
    
    def sairEstado(self):
        pass