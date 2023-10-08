from art import logo
from replit import clear

MENU = {
    "espresso": {
        "bahan": {
            "air": 50,
            "kopi": 18,
        },
        "harga": 1.5,
    },
    "latte": {
        "bahan": {
            "air": 200,
            "susu": 150,
            "kopi": 24,
        },
        "harga": 2.5,
    },
    "cappuccino": {
        "bahan": {
            "air": 250,
            "susu": 100,
            "kopi": 24,
        },
        "harga": 3.0,
    },
}

money = 0

resources = {
    "air": 300,
    "susu": 200,
    "kopi": 100,
}


def cek_ketersediaan(bahan_orderan):
    for item in bahan_orderan:
        if bahan_orderan[item] > resources[item]:
            print(f"Maaf tidak cukup {item} untuk membuat Kopi.\nSisa bahan dimesin:")
            print(f"Air  : {resources['air']}ml")
            print(f"Susu : {resources['susu']}ml")
            print(f"Kopi : {resources['kopi']}g")
            return False
    return True


def masukkan_coins():
    print("Masukkan coins.")
    coins = int(input("Masukkan quarters: ")) * 0.25
    coins += int(input("Masukkan dimes   : ")) * 0.1
    coins += int(input("Masukkan nickles : ")) * 0.05
    coins += int(input("Masukkan pennies : ")) * 0.01

    return coins


def cek_transaksi(pembayaran, harga_kopi):
    if pembayaran == harga_kopi:
        global money
        money += harga_kopi
        return True
    elif pembayaran > harga_kopi:
        money += harga_kopi
        pembayaran -= harga_kopi
        print(f"kembalian anda : {round(pembayaran,2)}")
        return True
    else:
        print("Maaf uang anda tidak cukup. Uang akan di refund.")
        return False


def buat_kopi(nama_kopi, bahan):
    for item in bahan:
        resources[item] -= bahan[item]
    print(f"Silahkan nikmati {nama_kopi} anda ☕️. Enjoy!")


def cek_harga():
    for item in MENU:
        harga_kopi = MENU[item]["harga"]
        print(f"Harga {item} : {harga_kopi}")


mesin_menyala = True
while mesin_menyala:
    print(logo)
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        mesin_menyala = False
    elif user_input == "report":
        print(f"Air  : {resources['air']}ml")
        print(f"Susu : {resources['susu']}ml")
        print(f"Kopi : {resources['kopi']}g")
        print(f"money: ${round(money, 2)}")
    elif user_input == "cek harga":
        cek_harga()
    else:
        drink = MENU[user_input]
        if cek_ketersediaan(drink["bahan"]):
            pembayaran = masukkan_coins()
            if cek_transaksi(pembayaran, drink["harga"]):
                clear()
                buat_kopi(user_input, drink["bahan"])
