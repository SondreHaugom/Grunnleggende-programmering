# funksjon for handlekurv som oppretter en tom handlekurv og en ordbok med varer og priser, og returnerer begge
def handlekurv():
    handlekurv =  [] # tom liste som fylles seg opp med varer og priser

    varer = { "melk": 22.9, "brød": 15.5, "ost": 45.0, "egg": 30.0, "smør": 25.0}
    if not varer:
        print("Ingen varer tilgjengelig.")
        return
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

 