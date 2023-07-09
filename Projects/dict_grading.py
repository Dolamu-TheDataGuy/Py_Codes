"""
Program that converts scores to a grade;

Scoring criteria;
Score 91-100 = "Outstanding"
Score 81-90 = "Exceeds Expectations"
Score 71-80 = "Acceptable"
Score 70 or lower = "Fail"

"""

student_scores = {
    "John": 81,
    "Ronke": 78,
    "Tobi": 99,
    "Johnson": 74,
    "Emmanuel": 88
}

#Create an empty dictionary called student grade
student_grades = {}

#Code to add the grades to student_grades
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    
#print student grades
print(student_grades)