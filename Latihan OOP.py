# membuat class
class Hero:
    # inisiasi atribut object
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    # membuat method
    def serang(self, enemy):
        print(f"{self.name} menyerang {enemy.name}")  # Object interactive
        enemy.bertahan(self, self.power, self.health)

    def bertahan(self, enemy, enemyPower, enemyHealth):
        print(f"{self.name} diserang {enemy.name}")  # Object interactive
        print(enemyPower)
        print(enemyHealth)
        attack_diterima = enemyPower / self.armor
        print(f"Serangan terasa : {attack_diterima}")
        self.health -= attack_diterima
        print(f"Sisa darah {self.name} saat ini : {str(self.health)}")


# membuat object Hero
Gani = Hero("Gani", 100, 15, 5)
Shiska = Hero("Shiska", 200, 8, 2)

# Menjalankan Method pada Object Hero
Gani.serang(Shiska)
print("\n")
Shiska.serang(Gani)
print("\n")
Gani.serang(Shiska)
