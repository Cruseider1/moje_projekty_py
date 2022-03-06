import random #biblioteka do losowania
import string #biblioteka znaków specjalnych


lowercase = string.ascii_lowercase #znaki alfabetu małe
uppercase = string.ascii_uppercase #znaki alfabetu duże
digits = string.digits #dodaje cyfry
punctuation = string.punctuation #dodaje znaki specjalne

n_znakow = 8
#n_znakow_typu = 2

wszystkie_znaki = random.sample(lowercase, 2) + random.sample(uppercase, 2) + random.sample(digits, 2) + random.sample(punctuation, 2)

losowe_znaki = random.sample(wszystkie_znaki, n_znakow) #generuje 8 różnych znaków ze zmiennej


#hasło to ciąg znaków (stringi)
haslo = ''.join(losowe_znaki) #powoduje że znaki hasła nie będą przedzielone jak stringi znakiem ''

print(haslo)

 