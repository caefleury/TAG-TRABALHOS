from grafo import arestas, grafo
from utils import is_inverted, arestas_duplicadas, maior_grau


class TestDataStructure():
    def test_ida_volta(self):
        """
        Testa se todas as arestas têm uma correspondente na direção oposta (ida e volta).

        Este método verifica se cada aresta no conjunto de arestas tem uma aresta correspondente na direção inversa,
        garantindo que para cada par (A, B) existe um par (B, A). Conta quantas dessas pares existem e compara com o valor esperado.
        """
        count = 0
        for edge in arestas:
            if is_inverted(edge[0], edge[1]):
                count += 1
        assert count == 190, f"Foram encontrados {count} pares de arestas invertidas, esperava-se 190."

    def test_duplicados(self):
        """
        Verifica se há arestas duplicadas no conjunto de arestas.

        Este teste garante que não existem arestas duplicadas no conjunto fornecido, o que é crucial para a integridade do grafo.
        Espera-se que a função arestas_duplicadas retorne False, indicando ausência de duplicatas.
        """
        assert arestas_duplicadas(
            arestas) == False, "Foram encontradas arestas duplicadas."

    def checa_maior_grau(self):
        """
        Verifica o grau do vértice com maior grau no grafo.

        Este teste verifica se o vértice de maior grau no grafo tem um grau específico, neste caso, espera-se que o maior grau seja 76.
        Isso ajuda a validar a estrutura do grafo e a lógica de cálculo do grau dos vértices.
        """
        assert maior_grau(
            grafo) == 76, f"O maior grau encontrado foi {maior_grau(grafo)}, esperava-se 76."
