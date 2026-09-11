from models import Imagem, EstadoImagem, EstadoSetor, EstadoInput

import cv2 as cv

class GerenciaImagem:
    def __init__(self, *, caminhoImg, caminhoExportacao, contagemPadrao, porcentagemSetor, zoomSetor, corPrimaria, corSecundaria, espessuraDivisoria, opacidadeDivisoria, opacidadeSetorContabilizado, fonteTexto, escalaTexto, corTexto, espessuraTexto, raioMarcacao, opacidadeMarcacao, corMarcacaoExportacao, raioMarcacaoExportacao, opacidadeMarcacaoExportacao):
        self.__imagem = Imagem(
            caminhoImg = caminhoImg, 
            porcentagemSetor = porcentagemSetor
        )

        self.__emExecucao = True

        self.__idEstadoAtual = None
        self.__idProximoEstado = 'imagem'
        
        estadoImagem = EstadoImagem(
                imagem = self.__imagem, 
                encerrarExecucao = self.__encerrarExecucao,
                fonteTexto = fonteTexto,
                escalaTexto = escalaTexto,
                corTexto = corTexto,
                espessuraTexto = espessuraTexto,
                corLinha = corPrimaria,
                espessuraLinha = espessuraDivisoria,
                opacidadeLinha = opacidadeDivisoria,
                opacidadeSetorContabilizado = opacidadeSetorContabilizado,
                callbackNavegarSetor = lambda : self.__defineIdProximoEstado('setor'),
                corMarcacao = corSecundaria,
                raioMarcacao = raioMarcacao,
                opacidadeMarcacao = opacidadeMarcacao,
                corMarcacaoExportacao = corMarcacaoExportacao,
                raioMarcacaoExportacao = raioMarcacaoExportacao,
                opacidadeMarcacaoExportacao = opacidadeMarcacaoExportacao,
                caminhoExportacao = caminhoExportacao,
                contagemPadrao = contagemPadrao
            )

        self.__estados = {
            'imagem': estadoImagem,
            'setor': EstadoSetor(
                imagem = self.__imagem,
                callbackNavegarInput = lambda : self.__defineIdProximoEstado('input'),
                callbackAtualizaPontosSetor = estadoImagem.atualizaPontosSetor,
                callbackObtemPontosSetor = estadoImagem.obtemPontosSetor,
                opacidadeMarcacao = opacidadeMarcacao,
                raioMarcacao = raioMarcacao,
                corMarcacao = corSecundaria,
                zoomSetor = zoomSetor
            ),
            'input': EstadoInput(
                imagem = self.__imagem,
                callbackEncerrarInput = lambda : self.__defineIdProximoEstado('imagem')
            )
        }

    def __defineIdProximoEstado(self, proxEstado):
        if proxEstado in self.__estados:
            self.__idProximoEstado = proxEstado

    def __encerrarExecucao(self):
        if self.__idEstadoAtual in self.__estados:
            self.__estados[self.__idEstadoAtual].sairEstado()
        self.__idEstadoAtual = self.__idProximoEstado = None
        self.__emExecucao = False
        
    def __trocaEstados(self):
        if self.__idEstadoAtual in self.__estados:
            self.__estados[self.__idEstadoAtual].sairEstado()
        if self.__idProximoEstado in self.__estados:
            self.__estados[self.__idProximoEstado].iniciarEstado()
        
        self.__idEstadoAtual = self.__idProximoEstado
        self.__idProximoEstado = None

    def contagem(self):
        try:
            while self.__emExecucao:
                if self.__idProximoEstado is not None and self.__idProximoEstado != self.__idEstadoAtual:
                    self.__trocaEstados()
                if self.__idEstadoAtual in self.__estados:
                    self.__estados[self.__idEstadoAtual].emExecucao()
        except Exception as err:
            print(err)
