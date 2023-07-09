import random

name = ["Alex", "Bata", "John", "James"]

student_score = {student: random.randint(1, 100) for student in name}

passed_student = {student: score for (student, score) in student_score.items() if score >= 50}
print(passed_student)

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
