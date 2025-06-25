def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

broj = int(input("Unesi granicu: "))

print("Parni brojevi:")
for p in parni(broj):
    print(p)

print("Neparni brojevi:")
for np in neparni(broj):
    print(np)
