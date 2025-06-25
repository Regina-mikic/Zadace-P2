def unazad(tekst):
    if tekst == "":
        return tekst
    else:
        return tekst[-1] + unazad(tekst[:-1])

unos = input("Unesi neki tekst: ")
print("Unatrag:", unazad(unos))
