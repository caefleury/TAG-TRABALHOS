from utils import read_data


class TestDataStructure():

    def test_data_read(self):
        test_file = 'src/project_02/entradaproj2TAG.txt'
        assert read_data(test_file, 4, 4) == [['P1', '3', '5']]
        assert read_data(test_file, 4, 5) == [
            ['P1', '3', '5'], ['P2', '1', '5']]
        assert read_data(test_file, 4, 6) == [['P1', '3', '5'], [
            'P2', '1', '5'], ['P3', '2', '4']]
