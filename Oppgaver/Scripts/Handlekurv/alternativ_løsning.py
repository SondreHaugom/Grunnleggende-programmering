def handlekurv():
    handlekurv = []
    varer = { "melk": 22.9, "brød": 15.5, "ost": 45.0, "egg": 30.0, "smør": 25.0}
    return handlekurv, varer


if __name__ == "__main__":
    handlekurv, varer = handlekurv()
    print("Velkommen til handlekurven!")

    while True:
        print("\nTilgjengelige varer:")
        for vare, pris in varer.items():
            print(f"{vare}: {pris} kr")

        print("\nSkriv inn navnet på varen og prisen for å legge den i handlekurven (trykk 'q' for å avslutte): ")

        vare = input("Vare: ")
        if vare.lower() == 'q':
            print("Takk for handleturen!")
            break
        try:
            pris = float(input("Pris: "))
            handlekurv.append({"Vare": vare, "Pris": pris})
            print(f"{vare} lagt i handlekurven til {pris} kr.")

            vis_handlekurv = input("Vil du se handlekurven? (ja/nei): ")
            
            
            if vis_handlekurv.lower() == 'ja':
                while True:
                    print("\n Din handlekurv:")
                    if not handlekurv:
                        print("Handlekurven er tom.")
                    else:
                        for item in handlekurv:
                            print(f"{item['Vare']} - {item['Pris']} kr")
                            print("Vil du fjerne en vare fra handlekurven? (ja/nei): ")
                            fjern_vare = input()
                            if fjern_vare.lower() == 'ja':
                                vare_fjern = input("Skriv inn navnet på varen du vil fjerne: ")
                                handlekurv = [item for item in handlekurv if item['Vare'].lower() != vare_fjern.lower()]
                                print(f"{vare_fjern} fjernet fra handlekurven.")

                            total_pris = sum(item['Pris'] for item in handlekurv)
                        print(f"Total pris: {total_pris:.2f} kr")

                    kasse = input("Vil du gå til kassen? (ja/nei): ")
                    if kasse.lower() == 'ja':
                        while True:
                            print(f"Du betalte: {total_pris:.2f} kr. Takk for handleturen!")
                            exit()
                    elif kasse.lower() == 'nei':
                        print("Du fortsetter å handle.")
                        break

        except ValueError:
            print("Ugyldig pris. Vennligst skriv inn et gyldig tall.")
