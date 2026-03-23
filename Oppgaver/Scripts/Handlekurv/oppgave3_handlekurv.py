def main():
    handlekurv = {"Vare": [], "Pris": []}  # Flytt denne utenfor while-løkka
    
    while True:
        menu()
        valg = input("Velg et alternativ (1-3) eller 'q' for å avslutte: ")

        if valg == 'q':
            print("Takk for handleturen!")
            break

        elif valg == '1':
            handlekurv = legg_til_varer(handlekurv)  # Send handlekurv som parameter
        
        elif valg == '2':
            vis_handlekurv(handlekurv) # Viser handlekurven
        
        elif valg == '3':
            handlekurv = slett_vare(handlekurv) # Sletter varer fra handlekurven
        
        else:
            print("Ugyldig valg. Velg 1-3 eller 'q' for å avslutte.")




def menu():
    print("Velkommen til handlekurven!")
    print("1. Legg til vare")
    print("2. Vis handlekurv")
    print("3. Slett vare")






# funksjon for å legge til varer i handlekurven
def legg_til_varer(handlekurv_liste):    
    varer = { "melk": 22.9, "brød": 15.5, "ost": 45.0, "egg": 30.0, "smør": 25.0}

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
            handlekurv_liste["Vare"].append(vare)
            handlekurv_liste["Pris"].append(pris)
        except ValueError:
            print("Ugyldig pris. Vennligst skriv inn et gyldig tall.")
    return handlekurv_liste 



def vis_handlekurv(handlekurv_liste):
    print("\nDin handlekurv:")
    if not handlekurv_liste["Vare"]:
        print("Handlekurven er tom.")
    else:
        for vare, pris in zip(handlekurv_liste["Vare"], handlekurv_liste["Pris"]):
            total_pris = sum(handlekurv_liste["Pris"])
            print(f"{vare} - {pris} kr")
        print(f"Total pris: {total_pris:.2f} kr")

    return handlekurv_liste







def slett_vare(handlekurv_liste):
    print("Vil du fjerne en vare fra handlekurven? (ja/nei): ")
    fjern_vare = input()
    if fjern_vare.lower() == 'ja':
        vare_fjern = input("Skriv inn navnet på varen du vil fjerne: ")
        if vare_fjern in handlekurv_liste["Vare"]:
            index = handlekurv_liste["Vare"].index(vare_fjern)
            del handlekurv_liste["Vare"][index]
            del handlekurv_liste["Pris"][index]
            print(f"{vare_fjern} fjernet fra handlekurven.")
        else:
            print(f"{vare_fjern} finnes ikke i handlekurven.")
    return handlekurv_liste


        


if __name__ == "__main__":
    main()
