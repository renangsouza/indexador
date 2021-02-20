#!/usr/bin/env python3

import sys

# Menu de ajuda.
def ajuda():
    print("Sintaxe: ./indexador.py <arquivo>")
    sys.exit(1)

# Variáveis
indice = "# Índice\n"
topicos = []
saida = ""

# Funções
def deleta():
    return True

def aprofunda(linha):
    n = 0 # Nível do tópico (H1, H2, H3...).
    for c in linha:
        if c == ' ':
            break
        else:
            n = n + 1
                  
    par = (n, linha[(n + 1):].rstrip()) # .rstrip() arranca nova linha ou espaços em branco no final.
    topicos.append(par)


def montaIndice(indice):
    for topico in topicos:
        if topico[0] == 1:
            indice = indice + "* [" + topico[1] + "]" + "(#" + topico[1] + ")\n"
        elif topico[0] % 2 != 0:
            indice = indice + (' ' * (topico[0] + 1)) + "* [" + topico[1] + "]" + "(#" + topico[1] + ")\n" 
        else:
            indice = indice + (' ' * topico[0]) + "* [" + topico[1] + "]" + "(#" + topico[1] + ")\n"

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
            deleta() # Deleta um índice já existente.
        elif linha[0] == '#':
            aprofunda(linha)

indice = montaIndice(indice)
salvaArquivo(indice)