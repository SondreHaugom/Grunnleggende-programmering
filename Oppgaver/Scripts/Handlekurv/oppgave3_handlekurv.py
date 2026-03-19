def handlekurv():
    handlekurv =  []

    varer = { "melk": 22.9, "brød": 15.5, "ost": 45.0, "egg": 30.0, "smør": 25.0}
    if not varer:
        print("Ingen varer tilgjengelig.")
        return
    return handlekurv, varer



if __name__ == "__main__":
    handlekurv, varer = handlekurv()    
    print("Velkommen til handlekurven!")
    while True:
        # viser tigjengelige varer og priser
        print("Tilgjengelige varer:")
        for vare, pris in varer.items():
            print(f"{vare}: {pris} kr")

        # ber brukeren om å skrive inn navnet på varen de ønsker å legge til i handlekurven
        valg = input("Skriv inn navnet på varen: ")
        if valg == "q":
            print("Takk for handelen")
            break
        if valg.lower() == "d":
            handlekurv.clear()
            print("Handlekurven er tømt.")

        # sjekker om varen er tilgjengelig og legger den til i handlekurven hvis den er det
        elif valg in varer:
            handlekurv.append(valg)
            print(f"{valg} lagt til i handlekurven. Nåværende handlekurv: {[(v, varer[v], 'kr') for v in handlekurv]}")
        else:
            print("Varen er ikke tilgjengelig. Prøv igjen.")

        vis_total = pris = sum(varer[vare] for vare in handlekurv)
        print(f"Total pris: {vis_total} kr")

        # spør brukeren om de vil se handlekurven og viser den hvis de svarer "j"
        vise_handlekurv = input("Vil du se handlekurven? (j/n): ")
        if vise_handlekurv.lower() == "j":
            if handlekurv:
                print("Nåværende handlekurv:")
                for vare in handlekurv:
                    print(f"{vare}: {varer[vare]} kr")
            else:
                print("Handlekurven er tom.")

