# a = 'XD'
# b = (1,2,3)
# c = [1,2,3]
# d = 1.2

# print (a.lower())  #drukuje małymi literami stringi można uzyć też .upper i wszystkie będą powiększone

#------------------------------------------------------
# x = int('1') # pozmieniaj typ.
# if isinstance(x, int):
#     print('x to int', x, type(x))

#------------------------------------------------------

# x = 2

# print('czy to prawda że x = 1?')

# if x == 1:
#     print("tak to prawda")
# else:
#     print('to inna wartość')

#------------------------------------------------------
# y = 'abc'
# x = 'a'
# if x in y:
#     print("x zawiera się w y. Czyli 'a' zawiera się w 'abc.")

#------------------------------------------------------
# x = 1
# y = 3

# if x == 1:
#     print(x)
#     if y == 2:
#         print(y)
#     elif x+y > 2:
#         print('y zmieniło wartość, to już nie 2 ale', y)
#         if x == 1 and y <= 10:
#             print('ale y jest nadal mniejsze od 10.')
# else:
#     print('x zmieniło wartość, to już nie 1 ale', x)
#     print('do y w ogóle tu nie docieramy. Zmień x na 1 aby dotrzeć do rozwidlenia z x.')

#------------------------------------------------------
# lista = list(range(1,,2))
# print (lista)

#print (int(20%8))

#------------------------------------------------------

# M = [[1,2,3],   #przecinki muszą być po nawiasie oddzielającym jedną listę od drugiej
#     [4,5,6],
#     [7,8,9]]

# print(M[1][2]) #indeks zawsze wrzucamy w nawiasy kwadratowe #drugi element zwraca wartość indeksu 2 w macierzy 1

#------------------------------------------------------

# X = ['aa','bb','cc']
# X.reverse() # sort

# print(X)

#------------------------------------------------------

# D = {} #stworzenie klucza jako set
# D['imie'] = 'Robert'  
# D['wiek'] = '40'
# D['zawod'] = 'stolarz' # przypisanie do klucza tych wszystkich wartosci 

# print(D)

#------------------------------------------------------
# M = list('mielonka')

# for c in M:
#     print(c.upper()) #wyświetla listę ze słowa mielonka dużymi literami

#------------------------------------------------------

# kwadraty = []

# for x in [1,2,3,4,5]:  #nie zapominaj o dwukropku po funkcji!
#     kwadraty.append(x**2)
# print(kwadraty)

#------------------------------------------------------

# f = open('data.txt', 'w') #tworzenie nowego pliku w trybie do odczytu
# f.write('siema')
# f.close

# help(f)

#------------------------------------------------------

