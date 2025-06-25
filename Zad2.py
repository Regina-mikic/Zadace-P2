import random

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan',
         'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra',
         'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša',
         'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela',
         'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip',
         'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej',
         'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ocjene = [random.randint(1, 5) for _ in imena]

brojac = {}
for ocjena in ocjene:
    if ocjena not in brojac:
        brojac[ocjena] = 1
    else:
        brojac[ocjena] += 1

prolaznost= sum(1 for ocjena in ocjene if ocjena > 1) / len(ocjene) * 100

print("Broj ocjena :", brojac)
print("Postotak prolaznosti: ",prolaznost, "%")
