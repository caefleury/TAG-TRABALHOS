import re


def read_projects(file, start_line, end_line):
    with open(file, 'r') as data:
        rows = []
        for i, current_row in enumerate(data, start=1):
            if start_line <= i <= end_line:
                rows.append(current_row[1:-2].strip().split(', '))
            elif i > end_line:
                break
    return rows


def read_students(file, start_line, end_line):
    with open(file, 'r') as data:
        rows = []
        for i, current_row in enumerate(data, start=1):
            if start_line <= i <= end_line:
                grade = current_row[-3:-2]
                if 61 <= i <= 70:
                    code = current_row[1:3]
                    preferences = current_row[6:-6].strip().split(', ')
                elif 71 <= i <= 160:
                    code = current_row[1:4]
                    preferences = current_row[7:-6].strip().split(', ')
                else:
                    code = current_row[1:5]
                    preferences = current_row[8:-6].strip().split(', ')
                row = [code, preferences, grade]
                rows.append(row)
            elif i > end_line:
                break
    return rows


def define_project_structure(project_list):
    projects = []
    for project in project_list:
        project = {
            'project_code': project[0],
            'slots': int(project[1]),
            'min_grade': int(project[2]),
            'students': []
        }
        projects.append(project)
    return projects


def define_student_structure(student_list):
    students = []
    for current_student in student_list:
        student = {
            'student_code': current_student[0],
            'preferences': current_student[1],
            'grade': int(current_student[2]),
            'project': ''
        }
        students.append(student)
    return students

# Função que extrai o inteiro do código do estudante para ajudar com a ordenação


def extract_student_code(item):
    return int(item['student_code'][1:])

# Função que exibe na tela os emparelhamentos
    # Se maximal = True exibe no formato de maior emparelhamento


def print_matchings(student_list, assigned_students, maximal=False):
    print('Tabela dos emparelhamentos:')
    sorted_students = sorted(student_list, key=extract_student_code)
    if maximal == False:
        for student in sorted_students:
            student_code = student['student_code']
            project_code = student['project']
            if len(student_code) == 2:
                print(f"{student_code}   ---------------- {project_code}")
            elif len(student_code) == 3:
                print(f"{student_code}  ---------------- {project_code}")
            else:
                print(f"{student_code} ---------------- {project_code}")
        print(f"Emparelhamentos: {len(assigned_students)}")
    else:
        print("\033[1;32m" +
              "======================================" + "\033[0m")
        print("\033[1;32m" + "Emparelhamento máximo:" + "\033[0m")
        for student in sorted_students:
            student_code = student['student_code']
            project_code = student['project']
            if len(student_code) == 2:
                print(
                    "\033[1;32m" + f"{student_code}   ---------------- {project_code}" + "\033[0m")
            elif len(student_code) == 3:
                print(
                    "\033[1;32m" + f"{student_code}  ---------------- {project_code}" + "\033[0m")
            else:
                print(
                    "\033[1;32m" + f"{student_code} ---------------- {project_code}" + "\033[0m")
        print(
            "\033[1;32m" + f"Quantidade máxima de emparelhamentos:  {len(assigned_students)}" + "\033[0m")
