#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import os

def load_mobilenet():
    """Não mude ou renomeie esta função
        Carrega o modelo e os parametros da MobileNet. 
        Retorna a rede carregada.
    """

    return None


def detect(net, frame, CONFIDENCE, COLORS, CLASSES):
    """
        Recebe:
            net - a rede carregada
            frame - uma imagem colorida BGR
            CONFIDENCE - o grau de confiabilidade mínima da detecção
            COLORS - as cores atribídas a cada classe
            CLASSES - o array de classes
        Devolve: 
            img - a imagem com os objetos encontrados
            resultados - os resultados da detecção
    """
    img = frame.copy()
    resultados = None

    return img, resultados

def separar_caixa_entre_animais(img, resultados):
    """Não mude ou renomeie esta função
        recebe o resultados da MobileNet e retorna dicionario com duas chaves, 'vaca' e 'lobo'.
        Na chave 'vaca' tem uma lista de cada caixa que existe uma vaca, no formato: [ [min_X, min_Y, max_X, max_Y] , [min_X, min_Y, max_X, max_Y] , ...]. Desenhe um retângulo azul em volta de cada vaca
        Na chave 'lobo' tem uma lista de uma unica caixa que engloba todos os lobos da imagem, no formato: [min_X, min_Y, max_X, max_Y]. Desenhe um retângulo vermelho em volta dos lobos

    """
    img = img.copy()

    animais = {}
    animais['vaca'] = []
    animais['lobo'] = [0, 0, 0, 0]

    return img, animais

def calcula_iou(boxA, boxB):
    """Não mude ou renomeie esta função
        Calcula o valor do "Intersection over Union" para saber se as caixa se encontram
    """
    return None

def checar_perigo(image, animais):
    """Não mude ou renomeie esta função
        Recebe as coordenadas das caixas, se a caixa de uma vaca tem intersecção com as do lobo, ela esta em perigo.
        Se estiver em perigo, deve escrever na imagem com a cor vermlha, se não, escreva com a cor azul.
        *Importante*: nesta função, não faça cópia da imagem de entrada!!
        
        Repita para cada vaca na imagem.
    """
    return