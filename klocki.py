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
x = 1
y = 3

if x == 1:
    print(x)
    if y == 2:
        print(y)
    elif x+y > 2:
        print('y zmieniło wartość, to już nie 2 ale', y)
        if x == 1 and y <= 10:
            print('ale y jest nadal mniejsze od 10.')
else:
    print('x zmieniło wartość, to już nie 1 ale', x)
    print('do y w ogóle tu nie docieramy. Zmień x na 1 aby dotrzeć do rozwidlenia z x.')