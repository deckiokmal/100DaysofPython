# Love Score Calculator
"""
Rule:
T L
R O
U V
E E

The lower() : mengubah caracter menjadi huruf kecil
The count() : Menghitung jumlah caracter
"""
print("Love Calculator.\n")

name1 = input("Your name : ")
name2 = input("Their name : ")

combine_name = name1 + name2
name_lower = combine_name.lower()

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t + r + u + e

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

# print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}. Your love like a coke and coca cola")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}. Your like be together.")
else:
    print(f"Your score is {love_score}.")
