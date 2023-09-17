# row of list
list1 = ["🫡", "🫣", "🫣"]
list2 = ["🫣", "🫣", "🫣"]
list3 = ["🫣", "🫣", "🫣"]
map = [list1, list2, list3]

print(f"{list1}\n{list2}\n{list3}")
position = input("Where do you want to put the treasure? ")

x_position = position[0]
y_position = position[1]

map[int(x_position)][int(y_position)] = "X"
print(f"{map[0]}\n{map[1]}\n{map[2]}")
