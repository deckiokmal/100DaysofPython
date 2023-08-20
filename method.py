# membuat class
class Hero:
    # class variabel
    jumlah_hero = 0

    # inisiasi instace object
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method terbagi 3 : method dengan argument, method tanpa argument, method dgn return
    # membuat method tanpa return/argumen
    def siapa(self):
        print(f"menyerang {self.name}")

    # membuat method dengan argumen
    # nama atribut harus sama dengan atribut inisiasi
    def tambahdarah(self, tambahDarah):
        self.health += tambahDarah  # atribut health

    # membuat method dengan return (mengembalikan nilai ke user)
    def getPower(self):
        return self.power


# membuat object
hero1 = Hero("Gani", 100, 10, 5)
hero2 = Hero("Siska", 99, 12, 10)

# menjalankan method pada object
# 1 method tanpa return dan argumen
hero1.siapa()
# 2 method dengan argumen tanpa return
hero1.tambahdarah(100)
print(hero1.health)
# 3 method dengan return tanpa argumen
print(hero1.getPower())
