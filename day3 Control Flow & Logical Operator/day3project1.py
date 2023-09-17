# Rollercoaster Gate check and Bill

"""
Rule:
1. Hanya seseorang dengan tinggi badan lebih dari 120cm boleh naik Rollercoaster
2. Jika seseorang berumur < 12, maka harga tiket $5
3. Jika seseorang berumur >= 12 and <= 18, maka harga tiket $10
4. Jika seseorang berumur > 18, maka harga tiket $12
5. Gate keeper akan bertanya akan seseorang ingin berfoto, jika Y maka akan ditambahkan $3 ke bill mereka.
"""

print("Wellcome to RollerCoaster!")
print("==========================\n")

tinggi = int(input("Berapa tinggi badan anda (cm)? "))
bill = 0

if tinggi > 120:
    print("Anda boleh naik Rollercoaster!")
    umur = int(input("Masukkan umur anda: "))

    if umur < 12:
        bill = 5
        print(f"Tiketmu seharga ${bill}")
    elif umur >= 12 and umur <= 18:
        bill = 10
        print(f"Tiketmu seharga ${bill}")
    else:
        bill = 12
        print(f"Tiketmu seharga ${bill}")

    photo = input("Apakah anda ingin difoto ? Y or N: ")
    if photo.lower() == "y":
        bill += 3

    print(f"Tiketmu seharga ${bill}")

else:
    print("Anda tidak boleh naik Rollercoaster!")
