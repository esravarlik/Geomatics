import random
import numpy

lowerAlphabet = "abcdefghijklmnropqstuvwxyz"
upperAlphabet = "ABCDEFGHIJKLMNROPQSTUVWXYZ"
number = "0123456789"

length = int(input("Enter password length:"))
password = "".join(random.sample((lowerAlphabet+ upperAlphabet+ number),length))
print(password)
