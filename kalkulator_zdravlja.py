import math

aplikacije = ["1. Kalkulator indeksa tjelesne mase", "2. Provjeri koliko si blizu idealne težine"]
print("Dobrodošli na našu aplikaciju! Izaberite jednu od navedenih igrica")
print(aplikacije)
odgovor = int(input("Unesite broj 1 ili 2: "))

#aplikacika broj 1

if odgovor == 1:
    visina = float(input("Unesite svoju visinu u centimetrima: "))
    tezina = float(input("Unesite vasu tezinu u kilogramima: "))

    visina = visina / 100
    indeks_tm = tezina / math.pow(visina, 2)

    print("Vas indeks tjelesne mase je: ", indeks_tm)
    if indeks_tm > 0:
        if indeks_tm <= 16:
            print("Vi ste poprilicno mrsavi.")
    elif indeks_tm <= 18.5:
        print("Vi ste mrsavi.")
    elif indeks_tm <= 25:
        print("Vi ste zdravi.")
    elif indeks_tm <= 30:
        print("Vi biste trebali malo smrsati.")
    elif indeks_tm <= 35:ł
        print("Vi ste preteski.")
    elif indeks_tm <= 40:
        print("Vi ste zabrinjavajuce teski")
    else:
        print("Molim Vas unesite validne parametre.")

# aplikacija broj 2

elif odgovor == 2:
    starost = int(input("Koliko imate godina?: "))
    visina = float(input("Unesite svoju visinu u centimetrima: "))
    tezina = float(input("Unesite vasu tezinu u kilogramima: "))

    aktivnosti = ["Plivanje", "Kosarka", "Setnja", "Biciklizam", "Planinarenje", "Teretana"]

    proracun = int(visina - tezina)
    idealna_tezina = proracun - 100

    if proracun == 100:
        print("Vi ste idealne težine")
    elif proracun > 100:
        print("Vi bi trebali da se udebljate " + str(idealna_tezina) + " kilograma")
    elif proracun < 100:
        print("Vi bi trebali da smrsate " + str(idealna_tezina) + " kilograma")
        if starost <= 35:
            print("Za mrsavljenje Vam se preporucuje: " + aktivnosti[1] + " i " + aktivnosti[5])
        elif starost > 35 & starost <= 55:
            print("Za mrsavljenje Vam se preporucuje: " + aktivnosti[3] + " i " + aktivnosti[4])
        elif starost >= 55:
            print("Za mrsavljenje Vam se preporucuje: " + aktivnosti[0] + " i " + aktivnosti[2])