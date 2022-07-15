A = int()
B = int()

print('_________________________________')
print('Simpler +/-/* und / Rechner für 2 Operatoren')
print('_________________________________')
Rechner = True
while Rechner == True:
    Was = input('+, -, * oder / ?: ')

    A = int(input('Erste Nummer: '))
    B = int(input('Zweite Nummer: '))

    if Was == '-':
        Minus = A - B  # Subtraktion
        print('Ergebniss: ')
        print(Minus)
        input('Fahre fort um weiter zu rechnen')
    
    if Was == '+':
        Plus = A + B  # Addition
        print('Ergebniss: ')
        print(Plus)
        input('Fahre fort um weiter zu rechnen')
    
    if Was == '*':
        Multi = A * B  # Multiplikation
        print('Ergebniss: ')
        print(Multi)
        input('Fahre fort um weiter zu rechnen')
    
    if Was == '/':
        Div = A / B  # Divison
        print('Ergebniss: ')
        print(Div)
        input('Fahre fort um weiter zu rechnen')