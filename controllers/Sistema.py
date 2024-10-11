import os
from glob import glob
import re

from .GerenciaImagem import GerenciaImagem
from .SelecionaImagem import SelecionaImagem

from Settings import *

class Sistema:

    def __init__(self):
    
        # try:
        caminhoImg = SelecionaImagem.selecionaImagem(extensoesValidas = EXTENSOES_VALIDAS)
        gerenciaImagem = GerenciaImagem(
            caminhoImg = caminhoImg, 
            porcentagemSetor = PORCENTAGEM_SETOR, 
            zoomSetor = ZOOM_SETOR,
            corPrimaria = COR_PRIMARIA,
            corSecundaria = COR_SECUNDARIA, 
            espessuraDivisoria = ESPESSURA_DIVISORIA,
            opacidadeDivisoria = OPACIDADE_DIVISORIA,
            opacidadeSetorContabilizado = OPACIDADE_SETOR_CONTABILIZADO,
            fonteTexto = FONTE_ROTULO_SETOR,
            escalaTexto = ESCALA_ROTULO_SETOR,
            corTexto = COR_ROTULO_SETOR,
            espessuraTexto = ESPESSURA_ROTULO_SETOR
        )
        gerenciaImagem.contagem()
        # except Exception as err:
        #     print(err)         

        