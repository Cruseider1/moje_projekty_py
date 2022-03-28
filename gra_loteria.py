import random

play = str("tak")

given = []
lottery = []

while play == str("tak"):
    for i in range(6):
        given.append(int(input("Podaj liczbę numer "+str(i+1)+": ")))
        lottery.append(random.randint(1,50))
    result = 0
    for z in given:
        for j in lottery:
            if z == j:
                result = result + 1
    
    print ("twój wynik to:  "+str(result))
    print("wylosowane liczby: ")
    for i in lottery:
        print(i)

    given.clear()
    lottery.clear()

    gramy = input ("czy chcesz zagrać jeszcze raz (tak/nie) ")