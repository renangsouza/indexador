#!/usr/bin/env python3

import sys

def ajuda():
    "Menu de ajuda."
    print("Sintaxe: ./indexador.py <arquivo>")
    sys.exit(1)

# Variáveis
indice = "# Índice\n"
topicos = []
saida = ""

def deleta(linhas):
    "Remove índice pré-existente."
    linhas.pop(0)
    while linha in linhas:
        if linha[0] == '#': break
        else: linhas.pop(0)

def ajeita(linha):
    "Substitui espaço em branco por &nbsp;"
    lAjeitada = []
    for c in linha:
        if c == ' ': lAjeitada.append("&nbsp;")
        else: lAjeitada.append(c)

    return "".join(lAjeitada)

def aprofunda(linha):
    "Monta lista de tópicos e suas respectivas profundidades."
    n = 0 # Nível do tópico (H1, H2, H3...).
    for c in linha:
        if c == ' ':
            break
        else:
            n = n + 1

    par = (n, linha[(n + 1):].rstrip())
    topicos.append(par)


def montaIndice(indice):
    for topico in topicos:
        if topico[0] == 1:
            indice = indice + "* [" + topico[1] + "]" + "(#" + ajeita(topico[1]) + ")\n"
        elif topico[0] % 2 != 0:
            indice = indice + (' ' * (topico[0] + 1)) + "* [" + topico[1] + "]" + "(#" + ajeita(topico[1]) + ")\n" 
        else:
            indice = indice + (' ' * topico[0]) + "* [" + topico[1] + "]" + "(#" + ajeita(topico[1]) + ")\n"

    indice = indice + "\n"
    return indice

def salvaArquivo(indice):
    saida = indice
    for linha in linhas:
        saida = saida + linha

    arquivoIndexado = open(((sys.argv[1])[:-3] + "-indexado.md"), "w")
    arquivoIndexado.write(saida)
    arquivoIndexado.close()

# Tratamento de entrada.
if len(sys.argv) != 2:
    ajuda()

else:
    arquivo = open(sys.argv[1], "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha == "# Índice\n":
            deleta(linhas)
            break
        elif linha[0] == '#':
            aprofunda(linha)

indice = montaIndice(indice)
salvaArquivo(indice)