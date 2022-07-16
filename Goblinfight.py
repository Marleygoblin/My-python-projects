Name = input('Name: ')
print('Hello', Name, 'Type options to see what you can do!')
input('continue...')

# Game
Gameover = False
Game = ()
Fight = ()

# XP
XP = int()
XPLevel = int(1)
XPGet = int()

# Weapon
Axe = int(10)
Axe2 = False
Axe2Axe = int(20)
Repair = True
Axerepair = int()
Axerepairallowed = True
Axeupgrade = True
Axestrenght = 10

# Shop
Shop = True

# Gold
Goldallowed = False
Gold = int()
Goldreward = int()  # Adds Gold
Goldpain = int()  # Removes Gold
Goldrepair = True
Goldhack = False

Game = input('Do you want to start the game? : ')  # Starts the game
if Game == 'yes':
    Goldallowed = True
if Game == 'no':
    Goldallowed = False

if Goldallowed == False:
    print(Name + ' Wrong Values were found!')
    input('continue?: ')

if Goldallowed == True:
    Gold = Gold + 4

while Goldallowed == True:

    if XP >= 101:
        XP = XP - XP
    if Goldhack == True:
        Gold = Gold + 100000
    if Gold >= -1:
        Axerepairallowed = True
    if Gold <= 1:
        Axerepairallowed = False

    if Axe2 == True:
        Axe = 69.75

    print('You are level ', XPLevel, ' !')

    Fight = input('Fight the goblin?:  ')

    if Fight == 'options':
        print('axe, gold, repair, yes, no, XP, upgrade, shop, axeinfo')

    if Axe <= 1:
        input('Gameover, the goblin killed you!')
        exit()

    if Gold <= 1:
        Repair = False
        Goldrepair = False

    if Gold >= 1:
        Repair = True
        Goldrepair = True

    if Fight == 'yes':
        if Axe >= -1:
            Axe = Axe - 2
            Gold = Gold + 2
            print('You have', Gold, 'gold now!')
            print('Your axe took damage and has', Axe, 'durability now!')
            print('You got 2 gold after fighting the goblin')

            if XPLevel <= 3:
                XPGet = 10
            if XPLevel >= 4:
                XPGet = 5
            if XP >= 99:
                XPLevel = XPLevel + 1
                XP = 0
            XP = XP + XPGet


            print('You won the fight! Level ', XPLevel, )

    if Fight == 'XP':
        print('You are level ', XPLevel, ' and have', XP, ' XP! ')

    if Fight == 'repair':
        print('repairing the axe... ')
        if Axerepairallowed == True:
            print('Your axe was repaired! (-4.5 Gold/ +6 durability) ')
            Gold = Gold - 4.5
            Axe = Axestrenght + 6

        if Axerepairallowed == False:
            print('You dont have enough gold now! ')
            print('You need 4 Gold!')

    if Fight == 'gold':
        print('Goldwallet of ' + Name)
        if Axerepairallowed == True:
            print('You have ', Gold, ' gold ! ')
        if Axerepairallowed == False:
            print('The goldwallet of ', Name, ' is empty!')

    if Fight == 'no':
        print('The goblin attacked you from behind and stole all of your remaining gold')
        Gold = Gold - Gold

    if Fight == 'upgrade':
        input('You try to upgrade your axe!')
        if XPLevel <= 0:
            print('You dont have enough levels!')
        if XPLevel >= 1:
            Axeupgrade = True
            XPLevel = XPLevel - 1
            XP = 0
            Axestrenght = Axestrenght + 2
            print('Axestrenght was increased!')

    if Fight == 'shop':
        print('A: Stronger axe (15 Gold)')
        Shopbuy = input(' Do you want to buy one of these items? ')
        if Shopbuy == 'A':
            if Gold <= 1:
                print('The shopowner got angry because you had no gold, your axe was damaged!')
                Axe = Axe - 5
            if Gold >= 0:
                Gold = Gold - 15
                Axe2 = True

    if Fight == 'axeinfo':
        print('Your axe has the durabilty of', Axe, ' !')
        if Axe2 == True:
            print('You have the strongest axe!')
        if Axe2 == False:
            print('Maybe they are shops you can get better a better axe...')

    if Fight == 'Goldhack = true':
        Goldhack = True
        print('Money,money,money!')

    if Fight == 'Goldhack = false':
        Goldhack = False
        Gold = Gold - 100000
        print('inflation...')

    input('continue...')
