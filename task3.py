import random
import string

print("Password Generator")
length = int(input("Enter length of the password: "))

letters = string.ascii_letters       
digits = string.digits             
punctuation = string.punctuation   

characters = letters+ digits+ punctuation

password = ""
for i in range(length):
    password = password + random.choice(characters)
print("Generated Password is:", password)