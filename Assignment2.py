
import random
guess = 0
a = random.randint(0,10)
print("Hi you will be provided three chances..Go ahead")
while guess < 3 :
    b = input("Choose a Number Between 0 to 10 : ")
    b = int(b)
    guess = guess+1
    if guess == 1:
        print("This is your 1st guess..")
    if guess == 2:
        print("This is your 2nd guess..")
    if guess == 3:
        print("This is your last guess")
    if b == a:
        break
if a == b:
    print("Great..Your guess is correct")
if a != b:
    a = str(a)
    print("You are wrong..The exact number is",a)


        

    
            
