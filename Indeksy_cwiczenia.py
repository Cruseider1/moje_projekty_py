
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

# lista_a = [1, 2]
# lista_b = [1, 2,3]
# if lista_a == lista_b:
#     print('Listy są identyczne.')
# else: 
#     print('nie ma tego elementu')
#---------------------------------------------------------------------

# lista = ['a', 'b', 'c', 'b', 'z', 'b']

# szukany_element = 'a' #tworzymy zmienną szukany element i podajemy wartość z listy stringów
# i = lista.index( szukany_element) #zmienna i przybierz wartość szukanego indeksu
# print('Szukany element jest na indexie:',i)

#---------------------------------------------------------------------

#fory i loopy 
#lista = [1, 2, 3]
# for i in lista:
#     print(i*2)

# for i in [1,2,3]:
#     print('Element "i" z pierwszej listy:', i)
#     for j in ['a', 'b', 'c']:
#         print('Litera z drugiej listy:', j)
#         for z in ['xD', '^_^', ':O']:
#             print('Buźka:', z)
#         print('----------------')

#---------------------------------------------------------------------

#enumerate Dzięki enumerate indeks każdego z elementów listy można wyciągnąć do zmiennej


# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for i, element in enumerate(lista): #jest for 'i,element' bo i oznacza zmienną indeks a element stringi w liście 
#     print(i)

#---------------------------------------------------------------------

# numbers = [1, 2, 3, 5, 7]
# letters = ['a', 'b', 'c']
# z = zip(numbers, letters) #zip łączy ze sobą element pierwszy z pierwszym z drugiej listy 
# z = list(z) #list sprawia że połączone elementy printują się jako lista. 

# print(z)

#---------------------------------------------------------------------

# lista_1 = [1,2,3,4,5,6,7]
# lista_2 = []
# for i in lista_1:
#     if i <= 3:
#         lista_2.append(i)
# print(lista_2)

#---------------------------------------------------------------------
# from itertools import count 

# c = count(1,4) # będzie printował co 4 i w zakresie miedzy 10 a 20 wrzuci dwa xd bo printuje to jako osobną liste. 

# for i in c:
#     print(i)
#     if i > 100:
#         break
#     if i in range(10, 20):
#         print('xD')
#---------------------------------------------------------------------

# import itertools
# # Define a list of the number of carrots picked across several days
# carrotsPickedToday = [3, 5, 0, 6, 0, 1]
# # Calculate the sum of the numbers in carrotsPickedToday using accumulate()
# # Notice that only carrotsPickedToday has been passed to accumulate() - as the function is optional, it will default to summing the values in the supplied list
# result = itertools.accumulate(carrotsPickedToday)
# # Print the result - it will be a list!
# for item in result:
#     print(item)

#---------------------------------------------------------------------
# import itertools
# lista = [1,2,3,5,6,7,8,9]

# lista2 = itertools.repeat(lista) #w przypadku napisania wirusa może zawalić pamięć.

# for i in lista2:
#     print(i)
#---------------------------------------------------------------------
# from itertools import permutations
 
# # Get all permutations of [1, 2, 3]
# perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
 
# # Print the obtained permutations
# for i in list(perm):
#     print (i)
#---------------------------------------------------------------------
