student_heights = (input("Input the height of each student\n "))

student_heights = student_heights.split(" ")

total = 0

for student in student_heights:
    total += int(student)
print(total)

count = 0

for height in student_heights:
    count += 1
print(count)

Average_height = int(total/count)
print(Average_height)