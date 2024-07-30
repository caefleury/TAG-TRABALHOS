from dados import vertices,edges
from utils import is_inverted

class TestDataStructure():
    def test_ida_volta(self):
        count = 0
        for edge in edges:
            if is_inverted(edge[0],edge[1]):
                count += 1
        assert count == 190 
