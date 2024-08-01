# Projeto 3 - Teoria e Análise de Grafos

Caetano Korilo Fleury de Amorim - 212006737

## Como Executar o Projeto

Primeiro, crie um ambiente virtual e instale os pacotes necessários com o seguinte comando:

```python
pip install -r requirements.txt
```

Navegue até a pasta do projeto (proj2) e execute o script principal:

```python
python3 main.py
```

Para rodar os testes (não relacionados diretamente com a entrega), utilize:

```python
pytest
```

## Algoritmo de Coloração Ótima Utilizando a Estratégia 'largest_first'

A lógica empregada no algoritmo de Gale-Shapley neste projeto foi a seguinte:

O algoritmo determina o grau dos vértices utilizando a biblioteca NetworkX e ordena esses graus em uma lista.

Começando pelo vértice de maior grau, são atribuídas cores aos vértices, onde o objetivo é colorir os vértices do grafo de modo que nenhum par de vértices adjacentes compartilhe a mesma cor.

No contexto deste projeto, cada vértice representa um jogo, e um vértice é adicionado como adjacente se estiver contido em um dos casos das restrições impostas.

### Restrições

1. Jogos não podem ocorrer na mesma cidade na mesma rodada (mesmo que o mandante seja diferente).
2. Um time não pode participar de dois jogos ao mesmo tempo.

#### Não foi possivel exibir um grafo com mais de 20 cores devido a restrição da própria bilbioteca

![Grafo Cinza](/assets/gray.png)
![Grafo Colorido](/assets/colored.png)

### grafo.py

Contém os grafo do grafo do projeto (vértices e arestas).

### algoritmo.py

Contém o algoritmo de coloração.

## Ferramentas

### Pacotes python

- networkx
- matplotlib

### Ferramenta de teste

- pytest

### Ferramenta de documentação

- phind.ai
