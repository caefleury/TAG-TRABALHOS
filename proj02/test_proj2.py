from utils import read_projects, read_students, define_project_structure, define_student_structure
from main import gale_shapley


class TestDataStructure():
    def test_read_projects(self):
        test_file = 'proj02/entradaproj2TAG.txt'
        assert read_projects(test_file, 4, 4) == [['P1', '3', '5']]
        assert read_projects(test_file, 4, 5) == [
            ['P1', '3', '5'], ['P2', '1', '5']]
        assert read_projects(test_file, 4, 6) == [['P1', '3', '5'], [
            'P2', '1', '5'], ['P3', '2', '4']]

    def test_read_students(self):
        test_file = 'proj02/entradaproj2TAG.txt'
        assert read_students(test_file, 62, 62) == [
            ['A1', ['P1', 'P30', 'P50'], '5']]
        assert read_students(test_file, 62, 63) == [
            ['A1', ['P1', 'P30', 'P50'], '5'], ['A2', ['P1', 'P30', 'P51'], '5']]
        assert read_students(test_file, 71, 71) == [
            ['A10', ['P8', 'P43', 'P10'], '4']]
        assert read_students(test_file, 161, 161) == [
            ['A100', ['P38', 'P3', 'P20'], '3']]

    def test_define_project_structure(self):
        test_data = [['P1', '3', '5'], ['P2', '2', '5']]
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
        test_data = ['A1', ['P1', 'P30', 'P50'], '5'], [
            'A2', ['P1', 'P30', 'P51'], '5']
        assert define_student_structure(test_data) == [
            {
                'student_code': 'A1',
                'preferences': ['P1', 'P30', 'P50'],
                'grade': 5,
                'project': ''
            },
            {
                'student_code': 'A2',
                'preferences': ['P1', 'P30', 'P51'],
                'grade': 5,
                'project': ''
            }
        ]


class TestGaleShapleyAlgorithm():
    def test_gale_shapley(self):
        student_data = [{'student_code': 'A1', 'preferences': ['P1', 'P30', 'P50'], 'grade': 5, 'project': ''},
                        {'student_code': 'A2', 'preferences': [
                            'P2', 'P30', 'P51'], 'grade': 5, 'project': ''},
                        {'student_code': 'A3', 'preferences': ['P3', 'P34', 'P35'], 'grade': 3, 'project': ''}]
        project_data = [{'project_code': 'P1', 'slots': 3, 'min_grade': 5, 'students': []},
                        {'project_code': 'P2', 'slots': 1,
                            'min_grade': 5, 'students': []},
                        {'project_code': 'P3', 'slots': 2, 'min_grade': 4, 'students': []}]
        assert gale_shapley(student_data, project_data) == [['A1', 'P1'], [
            'A2', 'P2']] or [['A2', 'P2'], ['A1', 'P1']]
