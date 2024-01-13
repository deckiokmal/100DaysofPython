# import python module
# askpython for detail random module

import random
import my_module  # Test membuat module

print(my_module.my_test)  # Memanggil fungsi di dalam module

# using random interger : randint(1,10) -> include all value
random_integer = random.randint(1, 10)
print(random_integer)

# using random float : 0.00000 - 0.999999
random_float = random.random()
print(random_float)

# kali random_float akan mengahasilkan 0.00000 - x.9999999
# dimana x adalah angka kali - 1. contoh : *5 = 0.0000 - 4.99999
multi_randfloat = random_float * 5
print(multi_randfloat)
