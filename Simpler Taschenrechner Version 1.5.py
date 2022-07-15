print('Simpler Rechner Version 1.5')
Mathe = True

x = int(input('Nummer 1: '))
y = int(input('Nummer 2: '))
z = int()

while Mathe == True:
    
    Operator = input('Plus(+), Minus (-), Mal(*) oder Geteilt(/)? (Bitte eines der Symbole in den Klammern benutzen!: ')
    
    if Operator == '+':
        z = x + y
        print('Das Ergebniss ist: ', z, ' !')
    
    if Operator == '-':
        z = x - y
        print('Das Ergebniss ist: ', z, ' !')
        input('Weiter rechnen...')
    
    if Operator == '*':
        z = x * y
        print('Das Ergebniss ist: ', z, ' !')
        input('Weiter rechnen...')
    
    if Operator == '/':
        z = x / y
        print('Das Ergebniss ist: ', z, ' !')
        input('Weiter rechnen...')
