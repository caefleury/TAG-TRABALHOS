import networkx as nx


def coloracao_grafo(grafo):
    """
    Aplica o algoritmo de coloração 'largest first' ao grafo fornecido.

    Parâmetros:
    grafo (networkx.Graph): O grafo a ser colorido.

    Retorna:
    dict: Um dicionário onde as chaves são os vértices e os valores são as cores atribuídas.
    """
    # Cores (rodadas)
    cores = {}
    cores_utilizadas = set()
    maior_cor = 0

    # Ordenar vertices
    graus = dict(grafo.degree())
    lista_de_graus = list(graus.items())

    for i in range(len(lista_de_graus)):
        for j in range(i + 1, len(lista_de_graus)):
            if lista_de_graus[i][1] < lista_de_graus[j][1]:
                lista_de_graus[i], lista_de_graus[j] = lista_de_graus[j], lista_de_graus[i]

    vertices_ordenados = lista_de_graus

    # Algoritmo de coloração utilizando a estratégia 'largest first' que começa pelo vértice de maior grau (4 possibilidades)
    for vertice, _ in vertices_ordenados:
        vizinhos = list(grafo.neighbors(vertice))

        # Encontrar cores já usadas pelos vizinhos
        cores_usadas = set()
        for vizinho in vizinhos:
            if vizinho in cores:
                cores_usadas.add(cores[vizinho])

        # Atribuir a menor cor disponível que não está sendo usada pelos vizinhos
        cor = 0
        while cor in cores_usadas:
            cor += 1
        cores[vertice] = cor
        cores_utilizadas.add(cor)

        if cor > maior_cor:
            maior_cor = cor
            print(f"Vértice {vertice} colorido com a cor {maior_cor}")

    return [cores, cores_utilizadas]
