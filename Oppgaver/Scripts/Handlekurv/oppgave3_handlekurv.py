def handlekurv():
    handlekurv =  []

    varer = { "melk": 22.9, "brød": 15.5, "ost": 45.0, "egg": 30.0, "smør": 25.0}

    while True:
        print("Velkommen til handlekurven! Skriv 'q' for å avslutte.")
        for vare, pris in varer.items():
            print(f"{vare}: {pris} kr")
        valg = input("Skriv inn navnet på varen du vil legge i handlekurven: ")
        if valg.lower() == 'q':
            break
        elif valg in varer:
            handlekurv.append(valg)
            print(f"{valg} har blitt lagt i handlekurven. {varer[valg]} kr")
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

if __name__ == "__main__":
    handlekurv()