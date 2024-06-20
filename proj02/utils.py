
def read_data(file, start_line, end_line):
    with open(file, 'r') as data:
        rows = []
        for i, current_row in enumerate(data, start=1):
            if start_line <= i <= end_line:
                rows.append(current_row[1:-2].strip().split(', '))
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
    for student in student_list:
        student = {
            'student_code': student[0],
            'preferences': student[1:-1],
            'grade': int(student[-1])
        }
        students.append(student)
    return students
