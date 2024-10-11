import cv2 as cv

from Utilitarios import Utilitarios

class RenderizaSetor:

    def __init__(self, *, imagem, callbackMarcarElemento, callbackEncerrarSetor, opacidadeMarcacao, raioMarcacao, corMarcacao, zoomSetor, ehNovaRenderizacao, resetaPontosSetor):
        self.__imagem = imagem
        self.__callbackEncerrarSetor = callbackEncerrarSetor
        self.__callbackMarcarElemento = callbackMarcarElemento
        self.__opacidadeMarcacao = opacidadeMarcacao
        self.__zoomSetor = zoomSetor
        self.__raioMarcacao = raioMarcacao
        self.__corMarcacao = corMarcacao
        self.__ehNovaRenderizacao = ehNovaRenderizacao
        self.__imgZoom = None
        self.__resetaPontosSetor = resetaPontosSetor

    def __mostraSetor(self, *, img):
        self.__imagemEstaAberta = True
        cv.imshow("Setor", img)
        cv.setMouseCallback("Setor", self.__mouseEventCallback)
        while self.__imagemEstaAberta:
            key = chr(cv.waitKey(1000) & 0xFF)
            if key == 'q':
                self.__callbackEncerrarSetor()
                break
            elif key == 'r':
                self.__resetaPontosSetor()
                break

    def renderizaSetor(self, pontosSetor):
        if self.__ehNovaRenderizacao():
            self.__imgZoom = self.__renderizaZoom(self.__imagem.obtemImgSetorAtual())
        copiaImg = self.__renderizaMarcacoes(self.__imgZoom, pontosSetor)
        self.__mostraSetor(img = copiaImg)

    def __renderizaZoom(self, img):
        alturaImg, larguraImg = img.shape[:2]
        novaAltura, novaLargura = self.__zoomSetor * alturaImg, self.__zoomSetor * larguraImg
        imgZoom = cv.resize(img, (novaLargura, novaAltura), interpolation=cv.INTER_LANCZOS4)
        return imgZoom

    def __renderizaMarcacoes(self, img, pontosSetor):
        copiaImg = img.copy()
        for ponto in pontosSetor:
            cv.circle(copiaImg, ponto, self.__raioMarcacao, self.__corMarcacao, -1)
        return Utilitarios.renderizaComOpacidade(imgOriginal=img, imgModificada=copiaImg, opacidade=self.__opacidadeMarcacao)


    def __mouseEventCallback(self, event, x, y, *_):
        if event == cv.EVENT_LBUTTONDOWN:
            self.__imagemEstaAberta = False
            self.__callbackMarcarElemento(x, y)