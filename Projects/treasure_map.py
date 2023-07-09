row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3].
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) 
vertical = int(position[1])

#Put "X" in row 2 column 3
#selected_row = map[horizontal - 1]
#selected_row[vertical - 1] = "X"

map[vertical - 1][horizontal - 1] = "X"

print(map)

