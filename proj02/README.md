# Projeto 2 - Teoria e Análise de Grafos

## Como rodar o projeto:

Dentro da pasta do projeto 2 (proj2) rode o código abaixo:

```
python3 main.py
```

## Algoritmo Gale-Shapley

A lógica utilizada no algoritmo de Gale-shapley no projeto foi a seguinte:

Se o aluno tiver interesse no projeto, sua nota for maior que a nota minima e houver espaço no projeto ele é alocado automaticamente:

```
if project_code in student_preferences and student_grade >= min_grade:

    if len(project['students']) < project['slots']:
        student['project'] = project_code
        project['students'].append(student['student_code'])
        assigned_students.append([student_code,project_code])
        break
```

Se não houver espaço no projeto e algum aluno dentro do projeto houver uma preferência menor que a do estudante da iteração atual, o aluno com menor preferência é retirado e o estudante da iteração é emparelhado.

```
if applicant_project_index > student_preference_index:
    least_interested_student = applicant_code
```

Se não houver espaço no projeto e algum aluno dentro do projeto houver uma preferência igual a do estudante da iteração atual, o aluno com a menor nota é alocado para o projeto.

```
elif applicant_project_index == student_preference_index:

    if applicant_grade < student_grade:
        least_interested_student = applicant_code
```

O número de iterações afeta significativamente o resultado máximo do algoritmo. 10 iterações tem resultados entre 49-52 enquanto que 100 iterações possuem resultados entre 52-54. Isso se da pela função que embaralha a lista de alunos antes de cada ireração. Começar a iteraçao por alunos diferentes ajuda o algoritmo a encontrar alunos que deixam o emparelhamento estável maior.
