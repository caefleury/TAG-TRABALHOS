teams = [
    {"nome": "Athletico (Pr)", "sigla": "CAP", "adjacentes": [], "cor": None},
    {"nome": "Atlético (Go)", "sigla": "ACG", "adjacentes": [], "cor": None},
    {"nome": "Atlético (MG)", "sigla": "CAM", "adjacentes": ["CEC2"], "cor": None},
    {"nome": "Bahia", "sigla": "ECB", "adjacentes": ["ECV"], "cor": None},
    {"nome": "Botafogo (RJ)", "sigla": "BFR", "adjacentes": ["CRF", "FFC", "CRVG"], "cor": None},
    {"nome": "Corinthians", "sigla": "SCCP", "adjacentes": ["SEP", "SPFC"], "cor": None},
    {"nome": "Criciúma", "sigla": "CEC1", "adjacentes": [], "cor": None},
    {"nome": "Cruzeiro", "sigla": "CEC2", "adjacentes": ["CAM"], "cor": None},
    {"nome": "Cuiabá", "sigla": "CEC3", "adjacentes": [], "cor": None},
    {"nome": "Flamengo", "sigla": "CRF", "adjacentes": ["BFR", "FFC", "CRVG"], "cor": None},
    {"nome": "Fluminense", "sigla": "FFC", "adjacentes": ["CRF", "BFR", "CRVG"], "cor": None},
    {"nome": "Fortaleza", "sigla": "FSC", "adjacentes": [], "cor": None},
    {"nome": "Grêmio", "sigla": "FBPA", "adjacentes": ["SCI"], "cor": None},
    {"nome": "Internacional", "sigla": "SCI", "adjacentes": ["FBPA"], "cor": None},
    {"nome": "Juventude", "sigla": "ECJ", "adjacentes": [], "cor": None},
    {"nome": "Palmeiras", "sigla": "SEP", "adjacentes": ["SPFC", "SCCP"], "cor": None},
    {"nome": "Red Bull Bragantino", "sigla": "RBB", "adjacentes": [], "cor": None},
    {"nome": "São Paulo", "sigla": "SPFC", "adjacentes": ["SEP", "SCCP"], "cor": None},
    {"nome": "Vasco da Gama", "sigla": "CRVG", "adjacentes": ["CRF", "FFC", "BFR"], "cor": None},
    {"nome": "Vitória", "sigla": "ECV", "adjacentes": ["ECB"], "cor": None},
]

vertices = []
edges = []

for t,team in enumerate(teams):  
    sigla = team['sigla']
    siglas_adjacentes = team['adjacentes']


    jogos = []

    # 1. adjacentes
    for sigla_adjacente in siglas_adjacentes:
        jogo = (sigla,sigla_adjacente)
        jogo_volta = (sigla_adjacente,sigla)
        
        jogos.append(jogo)
        jogos.append(jogo_volta)

        if jogo not in vertices:
            vertices.append(jogo)
        if jogo not in jogos:
            jogos.append(jogo)

        if jogo_volta not in vertices:
            vertices.append(jogo_volta)
        if jogo_volta not in jogos:
            vertices.append(jogo_volta)

    # outros times (cada time tem que jogar com todos os outros)

    for o,opponent in enumerate(teams):
        if t != o: # se os times não forem o mesmo
            sigla_oponente = opponent['sigla']
            jogo = (sigla,sigla_oponente)
            jogo_volta = (sigla_oponente,sigla)

            jogos.append(jogo)
            jogos.append(jogo_volta)
            
            if jogo not in vertices:
                vertices.append(jogo)
            if jogo not in jogos:
                jogos.append(jogo)

            if jogo_volta not in vertices:
                vertices.append(jogo_volta)
            if jogo_volta not in jogos:
                vertices.append(jogo_volta)


    # edges
    for i in range(len(jogos)):
        for j in range(i + 1, len(jogos)):
            edge = (jogos[i], jogos[j])
            edge_volta = (jogos[j], jogos[i])
            if edge not in edges and edge_volta not in edges:
                edges.append(edge)

