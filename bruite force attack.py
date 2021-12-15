#python project by Benjamin Swanson

#import
import string
import random

#variables
letters = ""
guess = 0
used_passwords = []
random_number = random.randint(5,15)
password = "urmomis"

#freebies
freebie = ['12345', 'qwerty', 'password', 'qwerty123', 'abc124', 'I love you', 'liverpool', 'rufos', 'jo Biden', 'ellan', '']

#run freebies
for Pass in freebie:
    print(Pass)

#main
while letters != password:
    random_number = random.randint(5,15)
    letters = string.ascii_letters
    guess = ''.join(random.choice(letters) for i in range(random_number))
    print(guess)


#finish
print ("get hacked nerd")
freebie.append(guess)



