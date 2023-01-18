import random

#vars
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numbers = "0123456789"
simbols = "*#+@¡?¿!/{<>=}&;[]%$"

#all vars in one
base = minus + mayus + numbers + simbols

#password length introduced by user
length = 0

while length < 2: 
    length = int(input("Insert the number of characters that the password will have: "))

#random list
list = random.sample(base, length)

#join the list to a var
password = "".join(list)

#show the password
print(password)
