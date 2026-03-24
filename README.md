# Grunnleggende programmering

Oppgave for å gjennomføre de mest basic programerings metoder

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Status](https://img.shields.io/badge/Status-Under%20arbeid-FF9800?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/status-under%20arbeid-yellow)](#)


---


## Innholdsfortegnelse
- [Om-prosjektet](#Om-prosjektet)
- [Prosjektstruktur](#Prosjektstruktur)
- [Filstruktur](#Filstruktur)
- [Biblioteker-og-begrunnelse](#Biblioteker-og-begrunnelse)
- [Oppgaver](#Oppagver)
- [Installasjon-og-oppsett](#Installasjon-og-oppsett)
- [Sikkerhet-og-personvern](#Sikkerhet-og-personvern)
- [Feilsøkings-strategier](#Feilsøkings-strategier)

---

## Om prosjektet
Dette prosjektet er et øvingsprosjekt hvor jeg skal jobbe systematisk med de mest brukte programmeringsmetodene og ferdighetene. Prosjektet er delt inn i fire ulike, mindre delprosjekter/oppgaver. Hver oppgave har som hensikt å fokusere på én spesifikk, grunnleggende ferdighet innen programmering.

Gjennom disse delprosjektene skal jeg arbeide med følgende temaer:

- Løkker – Forstå og implementere ulike typer løkker for å automatisere gjentakende oppgaver.
- Funksjoner/pytest – Lære å skrive funksjoner å sikre at funksjoenn gjør det den skal med pytest modulen.
- Databaser – Få innsikt i hvordan man kan lagre, hente og manipulere data ved hjelp av databaser.
- Logikk – Utvikle evnen til å bruke betingelser og logiske uttrykk for å styre programflyten.
Målet med prosjektet er å tilegne meg solide, grunnleggende ferdigheter i programmering, uten å bruke kunstig intelligens til å løse oppgavene. Jeg skal i stedet benytte dokumentasjon og andre tilgjengelige, tradisjonelle hjelpemidler. Dette vil styrke min selvstendighet og forståelse for sentrale konsepter innen programmering.

---

## Filstruktur

```
 Grunnlegende Programmering/
├── README.md
├── .vscode/
│   └── settings.json
└── Oppgaver/                       # Main project folder
    ├── .gitignore
    ├── pyvenv.cfg                  # Virtual environment configuration
    ├── Include/                    # Python headers
    ├── Lib/                        # Python libraries
    ├── Scripts/                    # Virtual environment scripts
    │   ├── Activate.ps1            # Environment activation
    │   ├── python.exe              # Python executable
    │   ├── Passord/                # 🔐 Password exercises
    │   │   ├── oppgave2_passord.py
    │   │   └── test_oppgave2_passord.py
    │   └── Logg/                   # 📝 Logging exercises
    │       ├── logg.py
    │       ├── logg.csv
    │       └── logg.txt
    └── [other virtual environment files...]
```

---

## Biblioteker-og-begrunnelse
|Import / Bibliotek           |Formål                                                 |
|-----------------------------|-------------------------------------------------------|
| `os`                        |	Håndterer fil- og mappestier                          |
| `re`                        | Regulære uttrykk matcher tekstmønstre i Python med re |
| `pytest`                    | pytest brukes til å kjøre tester i Python             |


---

## Oppgaver
Som nevnt er det fire forksjellige små porsjketer/ oppgaver.
- løkker
- Funksjoner
- Databaser
- Logikk
 
Jeg har gjennomført alle oppgavene gradevis og begynt med Løkker


## Logg.py
Den aller første oppgaven handler om å bruke løkker i Python. Hensikten er å få kompetanse i å bruke dem til å løse forskjellige typer oppgaver og formål.

Oppgaven handler spesifikt om å bruke for-løkker til å hente ut ulike typer data fra en tekstfil (txt). Denne tekstfilen inneholder en del data/informasjon som vi skal bruke for-løkker til å skrive ut. I txt-filen ligger det mange logger med dato, bruker og status (OK eller FEIL). Ut fra dette er det tre ting vi skal hente ut.
- antall linjer totalt
- antall OK og FAIL
- antall per bruker (hvor mange linjer hver bruker har)

### Løsning 
For å løse denne oppgaven brukte jeg litt tid på å utforske. Jeg satte opp en løkke og begynte med å prøve å hente ut alle linjene i logg.txt. Det jeg måtte passe på, var at den ikke hentet ut flere linjer enn nødvendig. Jeg ville kun hente linjer der det faktisk var tekst, og kun linjene der loggen var skrevet.

Slik holdt jeg på med de andre dataene jeg skulle hente ut, og til slutt fikk jeg et skript som hentet ut alt jeg trengte. Skriptet fungerte, men det var langt fra en god og robust kode som jeg var fornøyd med. For å løse dette satte jeg meg ned og refaktorerte koden min. Jeg visste hvordan dataene skulle skrives ut og hvordan jeg leste dem inn, så jeg kunne endre litt på logikken for å få en mer robust og lettlest kode som er enklere å vedlikeholde.

Måten det ble løst på var at jeg, i stedet for å ha mange for-løkker etter hverandre, samlet alt i en funksjon med én for-løkke og ulike sjekker. Hver sjekk skrev ut de forskjellige dataene fra txt-filen som skulle vises.

#### Resultat
![Skjermbilde](bilder/Skjermbilde%202026-03-18%20093942.png)



## Passord
Passordoppgaven handler om funksjoner og pytest. Målet er å lage en funksjon og bruke pytest til å sjekke om den gjør det den skal. Funksjonen skal kontrollere fire forskjellige krav som passordet må oppfylle:
- minst 10 tegn
- minst 1 stor bokstav
- 1 liten bokstav og 1 t
- ingen mellomrom

Oppgaven skal ha to filer (oppgave2_passord.py og test_oppgave2_passord.py) en fil for funksjonen og den andre for teste funksjonen med pytest. Målet er å sjekke at funksjonen klarer å oppdage når et passord er feil, og at den også klarer å bekrefte når et passord er riktig

### Løsning 
Måten jeg løste det på var ganske lik den første oppgaven. Siden jeg skulle sjekke forskjellige krav, begynte jeg med å sette opp en liten funksjon som sjekket at passordet hadde minst 10 tegn. Etter det satte jeg opp test_oppgave2_passord.py for å kjøre pytest-testene. Når jeg hadde sett at det fungerte, bygde jeg videre på de andre kravene passordet trengte, og sjekket underveis.

#### Resultat
![Skjermbilde](/bilder/Skjermbilde%202026-03-18%20101858.png)




## Handlekurv (CRUD)
Handlekurvoppgaven handler om å håndtere data som kan vises, opprettes og fjernes. Dette er en form for CRUD, som står for Create, Read, Update og Delete. Det eneste dette prosjektet ikke implementerer, er Update, men all annen funksjonalitet er på plass. Oppgaven gitt ut på at bruker skulle følge en meny som lar bruker gjennomføre forkjellige behov. 
- 1: Legge til varer
- 2: Vise varer/ handlekurv
- 3: Slette varer
  Målet med oppgaven er å få trening i å håndtere data på ulike måter som kan dekke behovene til systemet og brukeren generelt.


### Løsning 
Løsningen er gjennomført med lik strategi som de to første, der jeg begynte smått og la til mer og mer. Jeg har laget to løsninger for denne oppgave PGA en liten misforståelse. 

#### Løsning 1:
I den første løsningen følger jeg ikke en helt tradisjonell meny, men heller en fast sti som brukeren skal følge. Denne stien tar brukeren gjennom hele prosessen, fra å legge til varer, til å se handlekurven og få mulighet til å slette varer. Løsningen viser også totalprisen. Jeg misforsto litt hvordan oppgaven skulle løses, så derfor fikk løsningen litt av min egen vri. Likevel er den satt opp og fungerer som den skal.

Måten dette er løst på, er at jeg implementerer én funksjonalitet om gangen, slik at jeg kan bygge videre på den underveis. Det betyr at jeg startet med for eksempel å legge til varer, og deretter implementerte resten av funksjonaliteten. Dette er gjort for at jeg ikke skal låse meg fast i én bestemt løsning, slik at jeg kan utforske og prøve meg frem dersom jeg ser nye muligheter underveis. 


#### Løsning 2: 
Løsning to er litt annerledes, siden oppgaven spesifikt ber om en meny. Jeg måtte derfor tenke gjennom hvordan jeg kunne implementere dette i Python på en enkel og forståelig måte. Dette ble løst ved at brukeren kan velge et tall fra 1 til 3, og ut fra dette valget får brukeren mulighet til å legge til varer, vise handlekurven og slette varer. Totalbeløpet blir også vist.

Løsningen er gjennomført på samme måte som sist, ved at jeg gradvis implementerer funksjonalitet. Jeg startet med å lage funksjonen for å legge til varer. Den store forskjellen er at hele løsningen er bygd opp av funksjoner, noe som betyr at valgene brukeren gjør fører til at en bestemt funksjon blir kalt.



#### Reslutat (Alternativ løsning)
![Skjermbilde](/bilder/Skjermbilde%202026-03-23%20094025.png)


#### Resultat (Nåverende løsning)
![Skjermbilde](/bilder/Skjermbilde4%202026-03-24%20121513.png)




## FizzBuzz (Logikk)
FizzBuzz er en logikk oppgave. Oppagven går ut på at man skal skrive ut 100 tall i terminalen. For for vert tall som er delelig med 3 skal tallet erstattes med Fizz og vert tall som er deleig med 5 skal erstattes med Buzz og tilslutt tallet som er deleig med både 3 og 5 skal erstattes med FizzBuzz. 