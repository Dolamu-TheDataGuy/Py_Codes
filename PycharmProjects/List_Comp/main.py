with open("file1.txt", "r") as file1:
    file_1_data = file1.readlines()

with open("file2.txt", "r") as file2:
    file_2_data = file2.readlines()
    print(file_2_data)

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)
