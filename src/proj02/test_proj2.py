from utils import read_data,define_projects_structure


class TestDataStructure():

    def test_data_read(self):
        test_file = 'src/proj02/entradaproj2TAG.txt'
        assert read_data(test_file, 4, 4) == [['P1', '3', '5']]
        assert read_data(test_file, 4, 5) == [
            ['P1', '3', '5'], ['P2', '1', '5']]
        assert read_data(test_file, 4, 6) == [['P1', '3', '5'], [
            'P2', '1', '5'], ['P3', '2', '4']]

    def test_define_projects_structure(self):
        test_data = [['P1', '3', '5'],['P2', '2', '5']]
        assert define_projects_structure(test_data) == [
            {
                'project_code': 'P1',
                'slots': 3,
                'min_grade': 5,
                'students': []
            },
            {
                'project_code': 'P2',
                'slots': 2,
                'min_grade': 5,
                'students': []
            }
        ]