from utils import read_projects,read_students,define_project_structure,define_student_structure
import random

# Extração de dados
data_file = 'proj02/entradaproj2TAG.txt'
student_data = read_students(data_file, 62, 261)
project_data = read_projects(data_file, 4, 58)

# Grafo bipartido
student_structured_data = define_student_structure(student_data)
project_structured_data = define_project_structure(project_data)

# Função que extrai o inteiro do código do estudante para ajudar com a ordenação
def extract_student_code(item):
    return int(item['student_code'][1:])

# Algoritmo de Gale-Shapley
def gale_shapley(student_list,project_list):
    assigned_students = []
    maximal_assigned_students = []
    matching_sizes = []
    for i in range(10):
        random.shuffle(student_list)
        for student in student_list:
            student_preferences = student['preferences']
            student_code = student['student_code']
            student_grade = student['grade']

            # Sai da iteração do estudante se ele ja estiver emparelhado 
            if assigned_students:
                student_already_assigned = False
                for st in assigned_students:
                    if st[0] == student_code:
                        student_already_assigned = True
                        break
                if student_already_assigned:
                    break
            
            for project in project_list:
                project_code = project['project_code']
                min_grade = project['min_grade']
                if project_code in student_preferences and student_grade >= min_grade:
                    
                    # Se houver espaço no projeto  
                        # Criar emparelhamento
                    if len(project['students']) < project['slots']:
                        student['project'] = project_code
                        project['students'].append(student['student_code'])
                        assigned_students.append([student_code,project_code])
                        break

                    # Se não houver espaço no projeto -> 
                    else:
                        student_preference_index = student_preferences.index(project_code)
                        least_interested_student = student_code
                        
                        for applicant_code in project['students']:
                            current_applicant = dict()

                            # Extrai as informações do aluno selecionado de dentro do projeto
                            for applicant in student_list:
                                if applicant['student_code'] == applicant_code:
                                    current_applicant = applicant
                            
                            applicant_preferences = current_applicant['preferences']
                            applicant_project_index = applicant_preferences.index(project_code)
                            applicant_grade = current_applicant['grade']

                            # Se a preferência de um aluno no projeto for menor(maior index da preferencia) que a preferência do estudante atual
                            if applicant_project_index > student_preference_index:
                                least_interested_student = applicant_code

                            # Se a preferência de um aluno no projeto for a mesma que a preferência do estudante atual
                                # Entra no projeto quem tiver a menor nota  
                            elif applicant_project_index == student_preference_index:
                                if applicant_grade < student_grade:
                                    least_interested_student = applicant_code

                        # Se dentre os alunos no projeto e o estudante atual, o estudante atual tiver uma preferência maior 
                            # Tirar aluno  menos interessados da lista de estudantes do projeto
                            # Tirar projeto do aluno
                            # Atualizar lista de estudantes com projeto
                        if least_interested_student != student_code:
                            project['students'].remove(least_interested_student)
                            project['students'].append(student_code)
                            student['project'] = project_code
                            assigned_students.append([student_code,project_code])
                            for assigned_student in assigned_students:
                                if assigned_student[0] == applicant_code:
                                    assigned_students.remove(assigned_student)
                                    break
                            break

        # Exibe os emparelhamentos da iteração atual
        print('Tabela dos emparelhamentos -> Número de emparelhamentos')
        sorted_students = sorted(student_list, key=extract_student_code)
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
        
        if len(assigned_students) > len(maximal_assigned_students):
            matching_sizes.append(len(assigned_students))
            maximal_assigned_students = assigned_students

    # Exibe o maior emparelhamento
    print("\033[1;32m" + "======================================" + "\033[0m")
    print("\033[1;32m" + "Emparelhamento máximo:"+ "\033[0m")
    sorted_students = sorted(student_list, key=extract_student_code)
    for student in sorted_students:
        student_code = student['student_code']
        project_code = student['project']
        if len(student_code) == 2:
            print("\033[1;32m" + f"{student_code}   ---------------- {project_code}"+ "\033[0m")
        elif len(student_code) == 3: 
            print("\033[1;32m" + f"{student_code}  ---------------- {project_code}"+ "\033[0m")
        else: 
            print("\033[1;32m" + f"{student_code} ---------------- {project_code}"+ "\033[0m")
    print("\033[1;32m" + f"Quantidade máxima de emparelhamentos:  {len(maximal_assigned_students)}"+ "\033[0m")
    

    return maximal_assigned_students


gale_shapley(student_structured_data,project_structured_data)




