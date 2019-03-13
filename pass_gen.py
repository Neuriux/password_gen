import random
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ234567890!@#$.,'
passlen= input(' How long would you like your password?:')
passlen = int(passlen)
numpass = input('How many password would you like')
numpass = int(numpass)

for x in range(numpass):
        password = ''
        for x in range(passlen):
                password+=random.choice(char)
        print(password)
