import re

regex = r"^R.*[0-5].*\s.*M$"

tekst = input("Unesi string: ")

rezultat = re.search(regex, tekst)

if rezultat:
    print("Ispravno uneseno!")
else:
    print("Neispravno – mora početi s R, završiti s M, i sadržavati broj 0-5 i razmak.")
