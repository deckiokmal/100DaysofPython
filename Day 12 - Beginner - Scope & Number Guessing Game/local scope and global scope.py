################### Scope ####################

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # global scope
# global_var = 10


# def lawan():
#     # local scope
#     local_var = 11

#     def kawan():
#         # local scope
#         insidelocal_var = 22
#         print(local_var)  # error karna variable diluar function

#     print(insidelocal_var)  # error karna variable didalam function kawan()


# print(local_var)
# print(insidelocal_var)


# block scope
# local scope tidak berlaku dengan ifelse statement, forloop, while loop
game_level = 5
if game_level > 2:
    enemies = 10

print(enemies)
