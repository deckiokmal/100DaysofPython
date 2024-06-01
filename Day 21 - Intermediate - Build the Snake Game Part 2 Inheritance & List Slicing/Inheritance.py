class Animal:
    
    def __init__(self):
        self.num_eyes = 2
        
    def bernafas(self):
        print("tarik nafas, buang nafas")
        

# Class Inheritance
class Ikan(Animal):
    
    def __init__(self):
        super().__init__()
        self.num_eyes = 1
        
    def berenang(self):
        print("bergerak didalam air.")
        
    def bernafas(self):
        super().bernafas()
        print("lakukan ini didalam air.")
        

nemo = Ikan()
nemo.bernafas()
nemo.berenang()
print(f"{nemo.num_eyes}")
