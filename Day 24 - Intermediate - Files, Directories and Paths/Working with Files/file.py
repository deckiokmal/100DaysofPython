# Working with file-1 (Read)
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Working with file-2 (Read)
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Working with file (Write)
with open("my_file.txt", mode="w") as file:
    file.write("new text") # replace data in mode="w"

# Working with file (Append)
with open("my_file.txt", mode="a") as file:
    file.write("\nnew text") # append data in mode="a"

# Working with file (Append)
with open("my_file_append.txt", mode="a") as file:
    file.write("new text") # append data in mode="a"