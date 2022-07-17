A = True
while A == True:
    B = int(input('Nummer 1: '))
    C = int(input('Nummer 2: '))
    D = input('+, -, * oder /(:)? ')
    E = int()
    F = print('Das Ergebniss ist ', E, ' !')
    if D == '+':
        E = B + C
        print(F)
    if D == '-':
        E = B - C
        print(F)
    if D == '*':
        print(F)
    if D == '/' or ':':
        E = B / C
        print(F)