import math
import copy
import cv2 as cv

from .Setor import Setor

class Imagem:
    def __init__(self, *, caminhoImg, porcentagemSetor):
        self.__img = cv.imread(caminhoImg, 1)
        self.__particionaImagem(porcentagemSetor = porcentagemSetor)
        
        self.__setorAtual = 0
    

    def defineSetorAtual(self, setor):
        self.__setorAtual = setor

    def resetaContagemSetorAtual(self):
        self.__setores[self.__setorAtual].defineContagem(0)
        self.__setores[self.__setorAtual].defineContabilizado(False)
    
    def defineContagemSetorAtual(self, contagem):
        self.__setores[self.__setorAtual].defineContagem(contagem)
        self.__setores[self.__setorAtual].defineContabilizado(True)

    def obtemImg(self):
        return self.__img.copy()

    def obtemImgSetorAtual(self):
        coordendasSetor = self.__setores[self.__setorAtual].obtemCoordenadas()
        imgQuadro = self.img[coordendasSetor[0][1] : coordendasSetor[1][1] + 1, coordendasSetor[0][0] : coordendasSetor[1][0] + 1]
        return imgQuadro.copy()

    def obtemSetores(self):
        return copy.deepcopy(self.__setores)

    def obtemSetorSelecionado(self):
        return copy.deepcopy(self.__setores[self.__setorAtual]) 

    def obtemSaltoLinha(self):
        return self.__saltoLinha
    def obtemSaltoColuna(self):
        return self.__saltoColuna
    def obtemNumLinhas(self):
        return self.__numeroLinhas         
    def obtemNumColunas(self):
        return self.__numeroColunas

    def __particionaImagem(self, *, porcentagemSetor):

        alturaImg, larguraImg = self.__img.shape[:2]
        self.__saltoLinha = math.ceil(porcentagemSetor/100 * alturaImg)
        self.__saltoColuna = math.ceil(porcentagemSetor/100 * larguraImg)
        self.__numeroLinhas = math.ceil(alturaImg/self.__saltoLinha)
        self.__numeroColunas = math.ceil(larguraImg/self.__saltoColuna)

        self.__setores = []
        coordenadaBase = (0, 0)

        for _ in range(self.__numeroLinhas):
            for _ in range(self.__numeroColunas):
                
                self.__setores.append(Setor(
                    coordenadaInicial = coordenadaBase,
                    coordenadaFinal = (coordenadaBase[0] + self.__saltoColuna, coordenadaBase[1] + self.__saltoLinha)
                ))
                coordenadaBase = (coordenadaBase[0] + self.__saltoColuna, coordenadaBase[1])
            coordenadaBase = (0, coordenadaBase[1] + self.__saltoLinha)