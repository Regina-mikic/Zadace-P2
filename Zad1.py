import random

matrica = []
for i in range(7):
    red = []
    for j in range(7):
        red.append(random.randint(1, 9))
    matrica.append(red)

for red in matrica:
    print(red)

zbroj = 0

for i in range(7):
    zbroj += matrica[0][i]  
    zbroj += matrica[6][i]  

for i in range(1, 6):
    zbroj += matrica[i][0]  
    zbroj += matrica[i][6]  

print("Zbroj elemenata na rubovima matrice:", zbroj)
