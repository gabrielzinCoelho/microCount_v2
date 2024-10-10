from models import Imagem, EstadoImagem, EstadoSetor, EstadoInput

import cv2 as cv

class GerenciaImagem:
    def __init__(self, *, caminhoImg, porcentagemSetor, zoomSetor, corPrimaria, corSecundaria, espessuraDivisoria, opacidadeDivisoria, opacidadeSetorContabilizado, fonteTexto, escalaTexto, corTexto, espessuraTexto):
        self.__imagem = Imagem(
            caminhoImg = caminhoImg, 
            porcentagemSetor = porcentagemSetor
        )

        self.__idEstadoAtual = 'imagem'
        self.__estados = {
            'imagem': EstadoImagem(
                imagem = self.__imagem, 
                encerrarExecucao = self.__encerrarExecucao,
                fonteTexto = fonteTexto,
                escalaTexto = escalaTexto,
                corTexto = corTexto,
                espessuraTexto = espessuraTexto,
                corLinha = corPrimaria,
                espessuraLinha = espessuraDivisoria,
                opacidadeLinha = opacidadeDivisoria
            )
        }

    def __encerrarExecucao(self):
        self.__idEstadoAtual = None

    def contagem(self):
        try:
            while self.__idEstadoAtual is not None:
                self.__estados[self.__idEstadoAtual].emExecucao()
        except:
            pass