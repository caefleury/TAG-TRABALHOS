import networkx as nx
from dados import vertices,edges
import matplotlib.pyplot as plt

# Criar o grafo
grafo = nx.Graph()

# Adicionar vértices para cada jogo
for vertice in vertices:
    grafo.add_node(vertice)

# Adicionar arestas
grafo.add_edges_from(edges)

# Exibir o grafo
#print("Vértices:", grafo.nodes())
#print("Arestas:", grafo.edges())

# Utilizar o algoritmo de coloração de grafos do NetworkX
coloracao = nx.coloring.greedy_color(grafo, strategy="largest_first")
num_rodadas = len(set(coloracao.values()))

#print(coloracao)
print(num_rodadas)
#print(coloracao)
# Atribuir as cores aos times
# for time in times:
#     time["cor"] = coloracao[time["sigla"]]

# Exibir a coloração
# for time in times:
#     print(f"Time: {time['nome']}, Rodada: {time['cor']}")

# Apply a graph coloring algorithm
color_map = nx.coloring.greedy_color(grafo, strategy="largest_first")

# Extract the colors for each node
colors = [color_map[node] for node in grafo.nodes()]

# Define a color palette (you can customize this)
color_palette = plt.cm.get_cmap('tab20', max(colors) + 1)

# Draw the graph
pos = nx.spring_layout(grafo)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(grafo, pos, with_labels=True, node_color=colors, node_size=800, cmap=color_palette, edge_color='gray', font_weight='bold')

# Show the plot
plt.show()