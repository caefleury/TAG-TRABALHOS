import networkx as nx

times = [
    {"nome": "Athletico (Pr)", "sigla": "CAP", "adjacentes": [], "cor": None},
    {"nome": "Atlético (Go)", "sigla": "ACG", "adjacentes": [], "cor": None},
    {"nome": "Atlético (MG)", "sigla": "CAM", "adjacentes": [
        "CEC2"], "cor": None},
    {"nome": "Bahia", "sigla": "ECB", "adjacentes": ["ECV"], "cor": None},
    {"nome": "Botafogo (RJ)", "sigla": "BFR", "adjacentes": [
        "CRF", "FFC", "CRVG"], "cor": None},
    {"nome": "Corinthians", "sigla": "SCCP",
        "adjacentes": ["SEP", "SPFC"], "cor": None},
    {"nome": "Criciúma", "sigla": "CEC1", "adjacentes": [], "cor": None},
    {"nome": "Cruzeiro", "sigla": "CEC2", "adjacentes": ["CAM"], "cor": None},
    {"nome": "Cuiabá", "sigla": "CEC3", "adjacentes": [], "cor": None},
    {"nome": "Flamengo", "sigla": "CRF", "adjacentes": [
        "BFR", "FFC", "CRVG"], "cor": None},
    {"nome": "Fluminense", "sigla": "FFC", "adjacentes": [
        "CRF", "BFR", "CRVG"], "cor": None},
    {"nome": "Fortaleza", "sigla": "FSC", "adjacentes": [], "cor": None},
    {"nome": "Grêmio", "sigla": "FBPA", "adjacentes": ["SCI"], "cor": None},
    {"nome": "Internacional", "sigla": "SCI",
        "adjacentes": ["FBPA"], "cor": None},
    {"nome": "Juventude", "sigla": "ECJ", "adjacentes": [], "cor": None},
    {"nome": "Palmeiras", "sigla": "SEP",
        "adjacentes": ["SPFC", "SCCP"], "cor": None},
    {"nome": "Red Bull Bragantino", "sigla": "RBB", "adjacentes": [], "cor": None},
    {"nome": "São Paulo", "sigla": "SPFC",
        "adjacentes": ["SEP", "SCCP"], "cor": None},
    {"nome": "Vasco da Gama", "sigla": "CRVG",
        "adjacentes": ["CRF", "FFC", "BFR"], "cor": None},
    {"nome": "Vitória", "sigla": "ECV", "adjacentes": ["ECB"], "cor": None},
]

vertices = []
arestas = []

for t, time in enumerate(times):
    sigla = time['sigla']
    siglas_adjacentes = time['adjacentes']

    # Definir vertices para os times da mesma cidade do mandante
    for sigla_adjacente in siglas_adjacentes:
        jogo = (sigla, sigla_adjacente)
        jogo_volta = (sigla_adjacente, sigla)

        if jogo not in vertices:
            vertices.append(jogo)
        if jogo_volta not in vertices:
            vertices.append(jogo_volta)

    # Definir vertices para todos os jogos do time
    for o, opponent in enumerate(times):
        if t != o:  # se os times não forem o mesmo
            sigla_oponente = opponent['sigla']
            jogo = (sigla, sigla_oponente)
            jogo_volta = (sigla_oponente, sigla)

            if jogo not in vertices:
                vertices.append(jogo)
            if jogo_volta not in vertices:
                vertices.append(jogo_volta)


# Definir arestas
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        edge = (vertices[i], vertices[j])
        edge_volta = (vertices[j], vertices[i])
        if edge not in arestas and edge_volta not in arestas:
            # Mesmo time em dois vertices diferentes
            if vertices[i][0] == vertices[j][0] or vertices[i][0] == vertices[j][1] or vertices[i][1] == vertices[j][1]:
                arestas.append(edge)
            # Dois mandantes na mesma cidade
            else:
                for team in times:
                    if vertices[i][0] == team['sigla'] and vertices[j][0] in team["adjacentes"]:
                        arestas.append(edge)
                        break

# Gerar estrutura do grafo
grafo = nx.Graph()

for vertice in vertices:
    grafo.add_node(vertice)

grafo.add_edges_from(arestas)
