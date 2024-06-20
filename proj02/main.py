from utils import read_projects,read_students,define_project_structure,define_student_structure


data_file = 'proj02/entradaproj2TAG.txt'
student_data = read_students(data_file, 62, 261)
project_data = read_projects(data_file, 4, 58)

# Grafo bipartido
student_list = define_student_structure(student_data)
project_list = define_project_structure(project_data)

assigned_students = []
#for i in range(10):
for student in student_list:
    student_preferences = student['preferences']
    student_code = student['student_code']
    student_grade = student['grade']
    for project in project_list:
        project_code = project['project_code']
        min_grade = project['min_grade']
        if project_code in student_preferences and student_grade >= min_grade:
            if len(project['students']) < project['slots']:
                student['project'] = project_code
                project['students'].append(student['student_code'])
                assigned_students.append({'student_code':student_code, 'project_code':project_code})
            else:
                student_preference_index = student_preferences.index(project_code)
                least_interested_student = student_code
                for applicant in project['students']:
                    apllicant_code = applicant['student_code']
                    applicant_preferences = applicant['preferences']
                    applicant_project_index = applicant_preferences.index(project_code)
                    if applicant_project_index < student_preference_index:
                        least_interested_student = apllicant_code
                # se o applicant mais desinteressado não for o student atual
                    # tirar o applicant mais desinteresado da lista do projeto
                    # tirar o applicant da lista de alunos com projeto
                    # atribuir o codigo atual do student no projeto
                    # adicionar o student na lista de student com projeto
                # se for -> pular
                if least_interested_student != student_code:
                    project['students'].remove(least_interested_student)
                    project['students'].append(student_code)

                    student['project'] = project_code

                    assigned_students.append({'student_code':student_code, 'project_code':project_code})
                    
                    for assigned_student in assigned_students:
                        if assigned_student["student_code"] == apllicant_code:
                            assigned_students.remove(assigned_student)
                            break



