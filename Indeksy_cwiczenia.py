
#'a' (indeks 0),
#'b' (indeks 1),
#'c' (indeks 2),
#lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #, 'h', 'i', 'j', 'k', 'l']
#i = 0 # indeks - i
#element = lista[i]

#print(element) #teraz indeks jest ustawiony na element '0' więc wydrukuje literę 'a'
#---------------------------------------------------------------------

#string = 'ala ma kota'
#lista_1 = ['a', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']
#lista_2 = ['ala', ' ', 'ma', ' ', 'kota']

#indeks = -1 #jeżeli damy wartość -1 to pokaże nam ostatni element listy

#print (string[indeks])
#print(lista_2[indeks])

#oddo = lista_2[1:5] #printuje słowa / litery / znaki w tym zakresie

#print (oddo)

#---------------------------------------------------------------------

#lista = ['a','b','c','d','e','f','g','h','i','j']
#print('Lista przed odwróceniem:', lista)

#lista2 = lista[::-1] #ten nawias powoduje odwrócenie listy to jak polecenie reverse 
#print('\nPo odwróceniu:') #znak /n robi taki enter
#print('Stara lista:            ', lista) #w momencie gdy cudzysłów przesuniemy spacjami printuje nam się to ładnie oddzielone
#print('Nowa odwrócona lista:   ', lista2)

#lista.reverse() #tak samo odwraca listę 
#print('lista_z_reversem        ', lista)
#---------------------------------------------------------------------

lista = [1, 2, 3]
print('Lista przed zmianą wartości jednego z elementów', lista)

lista[2] = 'xD' #zmiana wartości w kwadratowym nawiasie to zmiana wartości indeksu co powoduje przesunięcie xd w prawo lub lewo
print('Lista po zmianie wartości jednego z elementów  ', lista)