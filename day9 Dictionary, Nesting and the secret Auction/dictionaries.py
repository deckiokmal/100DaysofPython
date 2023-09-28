# Dictionaries {key: value}
# Multiple key value pair separate by comma

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Access data from dictionaries. Dict identify by key
# dictionary["key"]
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "Adding new items to dictionary"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# wipe an exsisting dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an items in a dictionary
programming_dictionary["Loop"] = "Edit an items in a dictionary"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # print key
    print(key)

    # print value
    print(programming_dictionary[key])
