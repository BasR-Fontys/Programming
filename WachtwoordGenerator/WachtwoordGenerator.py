import random
import click

# Welkoms tekst + keuze om het wachtwoord genereren te starten.
print('Bedankt voor het gebruiken van mijn Wachtwoord Generator.\nHet programma zal je vragen aan welke eisen het '
      'wachtwoord moet voldoen.\nWanneer er zonder waardes op enter gedrukt wordt zal de standaard waarde Nee zijn')
Start = click.confirm('Wil je een wachtwoord creëren?', default=False)

# Vraagt de gebruiker om zijn wachtwoord eisen, wanneer de gebruiker er voor kiest om een wachtwoord te creëren.
if Start:
    Lengte = click.prompt('Hoe lang moet het wachtwoord zijn?', type=int)
    Kleineletters = click.confirm('Wil je ook gebruik maken van Kleine letters?', default=False)
    Hoofdletters = click.confirm('Wil je ook gebruik maken van hoofdletters?', default=False)
    Nummers = click.confirm('Wil je ook gebruik maken van nummers?', default=False)
    Speciale_tekens = click.confirm('Wil je ook gebruik maken van Speciale tekens?', default=False)
else:  # sluit het programma af wanneer de gebruiker geen wachtwoord wil genereren.
    print('Helaas wil je geen wachtwoord creëren. \nHet programma zal afgesloten worden.')
    exit()


# Mogelijke karakters voor het wachtwoord.
Kleineletters_Char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
Hoofdletters_Char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
Nummers_Char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Speciale_tekens_Char = ['!', '@', '#', '$', '%', '&', '*', '(', ')']


# Functie om het wachtwoord te genereren. Wanneer er Yes gekozen is voor een optie tijdens het opgeven van de eisen,
# worden de bruikbare karakters ingeladen in een lijst voor bruikbare karakters. Er wordt direct 1 random karakter
# uit de reeks in het wachtwoord gezet om te garanderen dat er minimaal 1 van dit soort in voor komt.
def GenereerWachtwoord(num, klein = False, hoofd = False, nummers=False , speciaal=False):
    # verwachte parameters (Lengte, Kleineletters, Hoofdletters, Nummers, Speciale_tekens)
    Wachtwoord = ''
    Mogelijke_chars = []
    Aantal = 0
    if klein:   # Voegt de toegestaande karakters toe aan de lijst met bruikbare karakters.
        Mogelijke_chars.append(Kleineletters_Char)
        Wachtwoord += random.choice(Kleineletters_Char)
        Aantal += 1

    if hoofd:
        Mogelijke_chars.append(Hoofdletters_Char)
        Wachtwoord += random.choice(Hoofdletters_Char)
        Aantal += 1

    if nummers:
        Mogelijke_chars.append(Nummers_Char)
        Wachtwoord += random.choice(Nummers_Char)
        Aantal += 1

    if speciaal:
        Mogelijke_chars.append(Speciale_tekens_Char)
        Wachtwoord += random.choice(Speciale_tekens_Char)
        Aantal += 1

# Hier wordt nagekeken of er 0 is opgegeven of dat de gewenste wachtwoord lengte korter is dan de gewenste eisen.
    if Aantal == 0 or Aantal >= num:
        print('De lengte van je gewenste wachtwoord is te kort voor dit aantal eisen.\nKies een langere lengte of '
              'verminder het aantal eisen.')
        quit()

# Na het toevoegen van de meerdere lists wordt list Mogelijke_chars een nested list, dit gaf wat problemen
# daarom flatten ik de list. Hierna wordt er een random karakter uit de lijst gehaald en in Wachtwoord geplaatst.
    for n in range(num - Aantal):
        flat_list = []
        for sublist in Mogelijke_chars:
            for item in sublist:
                flat_list.append(item)

        x = random.randint(0, len(flat_list))
        Wachtwoord += flat_list[x]

# Omdat de eerste 4 karakters altijd in de zelfde volgorde geplaatst worden, randomise ik de karakters door elkaar.
    Wachtwoord = ''.join(random.sample(Wachtwoord, len(Wachtwoord)))
    return Wachtwoord


print(GenereerWachtwoord(Lengte, Kleineletters, Hoofdletters, Nummers, Speciale_tekens))