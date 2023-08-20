# Membuat class
class Hero:
    # class variable
    jumlah = 0
    list_Hero = []

    # Membuat Method di dalam Class
    # __init__ adalah constructor yang dijalankan saat object dibuat
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable atau Atribut
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        Hero.list_Hero.append(inputName)
        print(f"Membuat Hero dengan nama {inputName}")


print(Hero.__dict__)

# Membuat Object dengan instansiasi class Hero()
hero1 = Hero("Gani", 100, 110, 5)
print(Hero.jumlah)
print(Hero.list_Hero)
hero2 = Hero("Shiska", 1000, 10, 0)
print(Hero.jumlah)
print(Hero.list_Hero)
