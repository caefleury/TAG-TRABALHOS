import networkx as nx
import matplotlib.pyplot as plt
from grafo import vertices, arestas, grafo
from algoritmo import coloracao_grafo


def main():
    cores = coloracao_grafo(grafo)[0]
    rodadas = coloracao_grafo(grafo)[1]

    # Exibir o número total de rodadas
    print('----------------------------------------------')
    print("\033[1;32m" +
          f'\nNúmero de vértices (jogos): {len(vertices)}' + "\033[0m")
    print("\033[1;32m" + f'Número de arestas: {len(arestas)}' + "\033[0m")
    print("\033[1;32m" + f'Número de rodadas: {len(rodadas)}' + "\033[0m")

    plt.figure(figsize=(15, 10))

    # Todos os vertices em cinza
    pos = nx.spring_layout(grafo)
    # Define a cor dos nós como cinza
    nx.draw_networkx_nodes(grafo, pos, node_color='gray')
    nx.draw_networkx_edges(grafo, pos, edge_color='gray', alpha=0.5)
    plt.title("Visualização sem coloração")
    plt.show()

    plt.clf()

    cmap_maior = plt.cm.get_cmap('gist_rainbow', 100)
    # Vértices com coloração
    nx.draw_networkx_nodes(grafo, pos, node_color=[
        cores[v] for v in grafo.nodes()], cmap=cmap_maior)
    nx.draw_networkx_edges(grafo, pos, edge_color='gray', alpha=0.5)
    plt.title("Visualização com coloração")
    plt.show()


if __name__ == '__main__':
    main()
