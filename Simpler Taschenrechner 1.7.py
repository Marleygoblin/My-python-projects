print('Taschenrechner 1.75')
M = True
while M == True:
    x = int(input('Nummer 1: '))
    y = int(input('Nummer 2: '))
    Z = input('+, -, / oder *?: ')
    ß = int()
    if Z == '+':
        ß = x + y
        print(ß)
    if Z == '-':
        ß = x - y
        print(ß)
    if Z == '/':
        ß = x / y
        print(ß)
    if Z == '*':
        ß = x * y
        print(ß)
    else:
        print('Bitte benutze eines der Symbole die angefragt wurden!')
input('weiter rechnen...')
