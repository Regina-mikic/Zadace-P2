def pozdrav(ime):
    return "Pozdrav " + ime + "!"

dobrodosao = lambda ime: "Dobrodošao " + ime + "!"

def ispisi_poruku(funkcija):
    print(funkcija("Regina"))

ispisi_poruku(pozdrav)

