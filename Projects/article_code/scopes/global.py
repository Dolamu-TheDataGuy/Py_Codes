# num = 0
# golf = 2

# def add_number():
#     print(num)
#     print(golf)

# print()
# add_number()


print(globals())

x = 'jack' # Global variable

print(globals())

y = 200  # Global variable

def add_number():
	num = 50
	return num * 2

print(globals())