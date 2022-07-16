print('Taschenrechner 1.75')
x = int(input('Nummer 1: '))
y = int(input('Nummer 2: '))
Z = input('+, -, / oder *?: ')
ß = int()
M = True
while M == True:
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
input('weiter rechnen...')