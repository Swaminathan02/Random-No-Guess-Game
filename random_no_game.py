import numpy as np
print("     Welcome to Number guessing Game\n     ****RULES****\n 1. You will be given 5 chances to guess the number correctly\n 2. The number lies between 1 to 100 (inclusive)\n    Procced to play\n    All the best!")
chances=5
dup=chances
i=1
random_number=np.random.randint(1,100,1)
while chances:
    print("Here is your chance number: ",i)
    guess=int(input("Enter the Number: "))
    if guess==random_number:
        print(" Hurray You WON! Congratulations! ")
        break
    elif random_number-5<guess<random_number+5 and chances!=1:
        print(" You have only ",dup-i," You are close! Come on")
    elif random_number>guess and chances!=1:
        print(" You have only ",dup-i," chances left! Think Higher")
    elif random_number<guess and chances!=1:
        print(" You have only ",dup-i," chances left! Think Lower")
    else:
        print(" You Lost! The number was: ",random_number," Try again")
    i+=1
    chances-=1