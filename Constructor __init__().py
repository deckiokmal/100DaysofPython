# Membuat class
class Hero:
    # Membuat Method di dalam Class
    def __init__(
        self, inputName, inputHealth, inputPower, inputArmor
    ):  # __init__ adalah constructor yang dijalankan saat object dibuat
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


# Membuat Object dengan instansiasi class Hero()
hero1 = Hero("Gani", 100, 110, 5)
hero2 = Hero("Shiska", 1000, 10, 0)

print(hero1.name)
print(hero1.health)
print(hero1.power)
print(hero1.armor)

print(hero1.__dict__)
print(hero2.__dict__)
