def pozdrav(ime):
    return "Pozdrav " + ime + "!"

dobrodosao = lambda ime: "Dobrodošao " + ime + "!"

def ispisi_poruku(funkcija, ime):
    print(funkcija(ime))
