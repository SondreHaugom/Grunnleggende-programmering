def handlekurv():
    handlekurv =  []

    while True:
        produkt = input("Skriv inn produktet du vil legge inn i handlekurven: ")
        if produkt.lower() ==  "q":
            break
        handlekurv.append(produkt)
        print(f"Produktet '{handlekurv}' er lagt til i handlekurven.")


if __name__ == "__main__":
    handlekurv()