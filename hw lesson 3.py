import random

wordlist = ['mercedes', 'toyota', 'honda', 'globus']
secret = random.choice(wordlist)
guesses = 'eoaubm'
turns = 5

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
             print (letter, end=' ')
         else:
           print ('_', end=' ')
           missed += 1

     print()

     if missed == 0:
         print ('\nURA ty POBEDIL!')
         break

     guess = input('\nВведите букву:')
     guesses += guess

     if guess not in secret:
        turns -= 1
        if turns == 0:
         print('\n\n Ty budesh poveshen!!! Etim slovom bylo:', secret)