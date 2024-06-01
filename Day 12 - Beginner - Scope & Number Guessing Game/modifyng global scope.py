################### Modifyng Global Scope ####################

# Kita ingin memodifikasi variable enemies di global scope
# dan melakukan modifikasi nilai didalam function (local scope)
enemies = 0


def increase_enemies():
    # jika kita memodifikasi global variable secara langsung maka akan mendapat error message.
    """UnboundLocalError: cannot access local variable 'enemies' where it is not associated with a value"""

    # untuk mengatasi error kita perlu menggunakan global function
    # penggunaan global function akan menyebabkan banyak bug pada aplikasi besar
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 0


def increase_enemies():
    print(f"enemies inside function: {enemies}")

    # jika ingin memodifikasi global variable menggunakan function
    # kita bisa menggunakan return
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
