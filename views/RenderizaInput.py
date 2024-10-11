import cv2 as cv

from Utilitarios import Utilitarios

class RenderizaInput:

    def __init__(self, *, imagem):
        self.__imagem = imagem
    
    def renderizaInput(self):
        Utilitarios.limparTerminal()
        contagem = input(f"Setor {self.__imagem.obtemSetorAtual()} - Contagem: ").strip()
        self.__imagem.defineContagemSetorAtual(contagem)
        Utilitarios.limparTerminal()