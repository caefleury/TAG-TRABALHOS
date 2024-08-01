import networkx as nx


def is_inverted(tuple1, tuple2):
    """
    Verifica se duas tuplas são inversas uma da outra.

    Esta função compara duas tuplas e retorna True se uma é a inversão da outra, ou seja, se os elementos da primeira tupla estão na ordem inversa na segunda tupla.
    É útil para verificar se uma aresta e sua correspondente na direção oposta estão presentes em um conjunto de arestas.

    Parâmetros:
    tuple1 (tuple): A primeira tupla para comparação.
    tuple2 (tuple): A segunda tupla para comparação.

    Retorna:
    bool: True se as tuplas são inversas uma da outra, False caso contrário.
    """
    return tuple1 == tuple2[::-1]


def arestas_duplicadas(arestas):
    """
    Verifica a existência de arestas duplicadas em um conjunto de arestas.

    Esta função itera sobre um conjunto de arestas, representadas como tuplas, e verifica se alguma aresta duplicada (considerando a direção) está presente.
    Arestas são consideradas duplicadas se existirem duas arestas com os mesmos vértices, independentemente da direção.

    Parâmetros:
    arestas (list of tuple): Uma lista de arestas, onde cada aresta é uma tupla de dois vértices.

    Retorna:
    bool: True se houver arestas duplicadas, False caso contrário.
    """
    arestas_verificadas = set()

    for aresta in arestas:
        aresta_ordenada = tuple(sorted(aresta))

        if aresta_ordenada in arestas_verificadas:
            return True
        else:
            arestas_verificadas.add(aresta_ordenada)

    return False


def maior_grau(grafo):
    """
    Encontra o grau do vértice com o maior grau em um grafo.

    Esta função itera sobre todos os vértices de um grafo e retorna o grau do vértice com o maior número de conexões.

    Parâmetros:
    grafo (networkx.Graph): O grafo a ser analisado.

    Retorna:
    int: O grau do vértice com o maior número de conexões no grafo.
    """
    vertice_maior_grau = None
    maior_grau = 0

    # Iterar sobre todos os vértices e seus graus
    for vertice, grau in grafo.degree():
        if grau > maior_grau:
            maior_grau = grau
            vertice_maior_grau = vertice

    return maior_grau
