from utils import read_data,define_project_structure,define_student_structure


class TestDataStructure():

    def test_data_read(self):
        test_file = 'proj02/entradaproj2TAG.txt'
        assert read_data(test_file, 4, 4) == [['P1', '3', '5']]
        assert read_data(test_file, 4, 5) == [
            ['P1', '3', '5'], ['P2', '1', '5']]
        assert read_data(test_file, 4, 6) == [['P1', '3', '5'], [
            'P2', '1', '5'], ['P3', '2', '4']]

    def test_define_project_structure(self):
        test_data = [['P1', '3', '5'],['P2', '2', '5']]
        assert define_project_structure(test_data) == [
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

    def test_define_student_structure(self):
        test_data = [['A1', 'P1', 'P30', 'P50','5'],['A2', 'P1', 'P30', 'P51','5']]
        assert define_student_structure(test_data) == [
            {
                'student_code': 'A1',
                'preferences': ['P1','P30','P50'],
                'grade': 5
            },
            {
                'student_code': 'A2',
                'preferences': ['P1','P30','P51'],
                'grade': 5
            }
        ]