grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_grades = dict(zip(students, grades))

for student, grade_list in student_grades.items():
    average_grade = sum(grade_list) / len(grade_list)
    print(f"{student}: {average_grade}")
