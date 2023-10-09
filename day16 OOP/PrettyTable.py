from prettytable import PrettyTable

tabel = PrettyTable()
tabel.add_column("Pokemon Name", ["Pokemon Air", "Pokemon Api", "Pokemon Luyak"])
tabel.add_column("Type", ["Air", "Api", "Luyak"])

tabel.align = "l"

print(tabel)
