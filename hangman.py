import time

print ("Hello and welcome user, Time to play hangman!")

time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

from random import choice
word = choice(['ant', 'alpaca', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
                'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose',
                'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl',
                'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal',
                'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout',
                'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra'])

guesses = ''
turns = 5

while turns > 0:         
    failed = 0                
    for char in word:      
        if char in guesses:    
            print (char,end=""),    
        else:
            print ("_",end=""),     
            failed += 1    

    if failed == 0:        
        print ("You won")
        break            
    guess = input("guess a character:") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )

        if turns == 0:           
            print ("You Lose"  )
            print("The word was", word)