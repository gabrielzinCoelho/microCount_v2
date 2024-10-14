import os
import cv2 as cv

class ExportarContagem:

    @staticmethod
    def removeContagemAnterior(caminhoPastaExportacao):
        try:
            for elemento in os.listdir(caminhoPastaExportacao):
                caminhoElemento = os.path.join(caminhoPastaExportacao, elemento)

                if(os.path.isdir(caminhoElemento)):
                    ExportarContagem.removeContagemAnterior(caminhoPastaExportacao=caminhoElemento)
                else:
                    os.remove(caminhoElemento)

            os.rmdir(caminhoPastaExportacao)

        except Exception as err:
            print(err)

    def __init__(self, *, imagem, caminhoExportacao) -> None:
        self.__imagem = imagem
        self.__caminhoExportacao = caminhoExportacao

    def exportaContagem(self):

        nomeImg = self.__imagem.obtemNomeImg()
        extensaoImg = self.__imagem.obtemExtensaoImg()

        caminhoPastaExportacao = os.path.join(self.__caminhoExportacao, nomeImg)

        if(os.path.isdir(caminhoPastaExportacao)):
            ExportarContagem.removeContagemAnterior(caminhoPastaExportacao=caminhoPastaExportacao)
        os.makedirs(caminhoPastaExportacao)

        img = self.__imagem.obtemImg()
        for setor in self.__imagem.obtemSetores():

            coordendasSetor = setor.obtemCoordenadas()
            imgQuadro = img[coordendasSetor[0][1] : coordendasSetor[1][1] + 1, coordendasSetor[0][0] : coordendasSetor[1][0] + 1]
            cv.imwrite(os.path.join(caminhoPastaExportacao, f"setor_{setor.obtemId()}.{extensaoImg}"), imgQuadro)

