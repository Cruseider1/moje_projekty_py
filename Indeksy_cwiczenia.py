
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

#lista = [1, 2, 3,1,1,1,2]

#policz = lista.count(1) #ta funkcja liczy ile jest jedynek w liście powyższej, oczywiście trzeba tylko podmienić zmienną poniżej w kodzie
#print('Lista przed zmianą wartości jednego z elementów', lista)

#lista[2] = 'xD' #zmiana wartości w kwadratowym nawiasie to zmiana wartości indeksu co powoduje przesunięcie xd w prawo lub lewo
#print('Lista po zmianie wartości jednego z elementów  ', lista)

####lista.clear() tym poleceniem czyścimy listy z elementów np. pusta = lista.clear()
####''.join(lista) tym poleceniem łączymy elementy w liście usuwając znaki '' jeśli są to słowa np. Ala ma kota to robią '' będzie Alamakota więc trzeba wstawić 1 spację w ' ' i będzie poprawnie
### list.copy() - jeśli chcemy skopiować listę a i sprawić aby każdy nowy element dodany do listy a nie był w liście b

#---------------------------------------------------------------------  

#lista = ['a', 'b']
#print(lista)

#lista = lista * 2 # 3, 4, 5
#print(lista) #wynik to a,b, a, b więc można mnożyć nie tylko liczby

#---------------------------------------------------------------------

#lista_z_kotkiem = [1, 2, 'kotek', 3, 4, 5]
#lista_bez_kotka = [1, 2, 3, 4, 5]

#lista = lista_z_kotkiem
#szukany_element_w_liscie = 'kotek'
#if szukany_element_w_liscie in lista: #if i in - to polecenie pozwala nam sprawdzić czy dany element znajduje się w liście która nas interesuje
#    print('kotek')


#---------------------------------------------------------------------

#lista_int = [4, 3, 1]
#print(lista_int)

#lista_int.sort() # w ten sposób sortuje się lista rosnąco, żeby sortowała się malejąco należy wpisać w nawias (reverse=True)
#lista_nowa = sorted(lista, reverse=True) #Sort od Sorted różni się tym, że sorted tworzy nowy elemenet teraz można byłoby wyprintować lista_int i osobno lista_nowa (tak samo można użyć reverse=true w sorted)


#print(lista_int)

#---------------------------------------------------------------------

lista_a = [1, 2]
lista_b = [1, 2,3]
if lista_a == lista_b:
    print('Listy są identyczne.')
else: 
    print('nie ma tego elementu')
#---------------------------------------------------------------------

# lista = ['a', 'b', 'c', 'b', 'z', 'b']

# szukany_element = 'a' #tworzymy zmienną szukany element i podajemy wartość z listy stringów
# i = lista.index( szukany_element) #zmienna i przybierz wartość szukanego indeksu
# print('Szukany element jest na indexie:',i)

#---------------------------------------------------------------------
