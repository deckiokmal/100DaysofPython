# Day2 Project "Tip Calculator"
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Tip Calculator")
print("==============\n")

pay = float(input("Berapa besar yang ingin dibayar:\n$"))
tip = int(input("Berapa persen tip yg diberikan 5 / 10 / 12:\n"))
person = int(input("Berapa orang yang akan dibagi:\n"))

result_tip = pay * (1 + tip / 100)
result_pay = result_tip / person
decimal_place = round(result_pay, 2)
print(f"Masing-masing harus membayar sebesar ${decimal_place}")
