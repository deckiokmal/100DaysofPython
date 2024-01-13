# if else statement
angka = int(input("Masukkan angka :\n"))

if angka != 1:
    print("Angka tidak sama dengan 1")
else:
    print("Ok")

# Nested if else
print("Rollercoaster Gate check!")
tinggi_badan = int(input("Berapa tinggi badan anda ?\n"))
umur = int(input("Berapa umur anda ?\n"))
if tinggi_badan >= 120:
    print("Tinggi badan anda memenuhi syarat")
    if umur >= 12:
        print("Silahkan bersenang-senang")
    else:
        print("Anda tidak boleh naik, karna umur anda kurang dari 12 tahun")
else:
    print("Mohon maaf tinggi badan anda tidak memenuhi syarat!")

# elif statement

panjang = int(input("Berapa Panjang ? "))
lebar = int(input("Berapa Lebar ? "))

if panjang == lebar:
    print(f"Ini adalah kotak sempurna")
elif panjang > lebar:
    print(f"Ini adalah persegi panjang")
elif panjang < 100 and lebar > panjang:
    print("Ini adalah persegi panjang juga")
else:
    print("Nothing")
