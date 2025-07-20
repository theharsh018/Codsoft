# ROCK PAPER  AND SCISSORS.
#rule:- rock wins agains scissors.
# sicssors wins agains paper,
# paper wins agains rock.

#LET
#0-->rock
#1-->paper
#2-->scissors
#Take one input from user and another input is take use random as a computer input.
# use ramdom module and random.choice function.

#CODE STEPS...
import random
user=int(input("Enter the number: "))
list =[0,1,2]
computer  = random.choice(list)
print("user input is: ",user)
print("computer input is: ",computer)
#conditional statement.
if(user==0 and computer==1):
    print("computer win")
elif(user==0 and computer==2):
    print("user win")
elif(user==1 and computer==0):
    print("user win")
elif(user==1 and computer==2):
    print("computer win")
elif(user==2 and computer==0):
    print("computer win")
elif(user==2 and computer==1):
    print("user win")
else:
    print("draw")

print("TRY AGAIN!")
