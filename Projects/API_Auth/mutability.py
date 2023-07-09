# Mutable Data Types -----> List, Dictionary, Set
#Immutable Data Types -----> Numbers, Strings, Tuples


#action = "Dad"

#action = "John"

#print(id(action))
#print(id(action))
#print(action is action)

#my_tuple = (1,2,3)
#print(id(my_tuple))

#my_tuple_1 = (1,2,5,7)
#print(id(my_tuple))

#my_list = [1,2,3]
#print(id(my_list))

#my_list = [1,2,3]
#print(id(my_list))

my_list = [1,4,5]
print(id(my_list))

my_list[0] = 100
print(my_list)
print(id(my_list))

my_list = [100,4,5]
print(id(my_list))

count = 1
print(id(count))

count += 1
print(count)
print(id(count))

num = 10
print(id(num))

num = 12
print(id(num))

# When the same variable of an immutable data type are assigned the same value, they have the same address in memory
# When the same variable of an immutable data type are assigned different values, they have different address in memory
# When different variables are assigned the same value, they are assigned the same address in memory space.
# When an immutable data type is modified in memory space the modified variable is assigned a new address in memory space.

lam = [3, 37, 225, 6]
total = 225
lam.sort(reverse=True)
print(lam)