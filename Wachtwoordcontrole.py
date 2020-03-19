import re

Score = 0
Sterkte = ''
print('Met dit programma kan je testen hoe sterk je wachtwoord is.')
print('Er zal een score van 1 tot 10 gegeven worden waar 1 zeer zwak is en 10 erg sterk.')
Wachtwoord = input('Vul hier een wachtwoord in om de sterkte te testen: ')


if re.search("[a-z]", Wachtwoord):
    Score = Score + 1
if re.search("[A-Z]", Wachtwoord):
    Score = Score + 1
if re.search("[0-9]", Wachtwoord):
    Score = Score + 1
if re.search("[!#$%&'*+.^_`|~:]", Wachtwoord):
    Score = Score + 1

if len(Wachtwoord) >= 100:
    Score = Score + 6
elif len(Wachtwoord) >= 33:
    Score = Score + 5
elif len(Wachtwoord) >= 17:
    Score = Score + 4
elif len(Wachtwoord) >= 8:
    Score = Score + 3
elif len(Wachtwoord) >= 4:
    Score = Score + 2
elif len(Wachtwoord) >= 1:
    Score = Score + 1

if Score >= 8:
    Sterkte = 'Zeer Sterk'
elif Score >= 6:
    Sterkte = 'Sterk'
elif Score > 3:
    Sterkte = 'zwak'
elif Score >= 0:
    Sterkte = 'Zeer Zwak'


print('Het wachtwoord ' + Wachtwoord + ' heeft een score van ' + str(Score) + ' en is ' + Sterkte)

