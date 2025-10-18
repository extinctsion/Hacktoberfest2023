import random
d={1:"Snake",2:"Water",3:"Gun"}
def check(user,com):
    r_score="False"
    if user not in [1,2,3,-1]:
        return None
    else:
        print("Your Choice     :",d[user])
        print("Computer Choice :",d[com])
        if user==com :
            print("Draw")
            return "Draw"
        elif user== 1 and  com== 3 :
            print("**You Lose**")
            return False
        elif user== 3  and  com== 2 :
            print("**You Lose**")
            return False
        elif user== 2 and  com== 1 :
            print("**You lose**")
            return False
        else:
            print("**You Win**")
            return True
user=int(input("Enter: 1 for snake,2 for water, 3 for Gun OR -1 to stop :"))
l=0
c=0
while user!=-1:
    com=random.randint(1,3)
    result=check(user,com)
   
    if result == True:  
        l+=1
        print("Your Score:", l)
        c+=0
        print("Computer Score :",c)
    elif result is None:
        print("Invalid Input! Please enter a valid choice.")
    elif result == "Draw": 
        print("Your Score:", l)
        print("Computer Score :",c)
    else:
        l+=0
        print("Your Score:", l)
        c+=1
        print("Computer Score :",c)

    print()
    user=int(input("Enter: 1 for snake,2 for water, 3 for Gun : "))

if l>c:
    print()
    print("YOU WIN THE GAME")
    print(f'YOUR SCORE:{l} v/s COMPUTER SCORE:{c}')
    print()
else:
    print()
    print("YOU LOSE THE GAME")
    print(f'YOUR SCORE:{l} v/s COMPUTER SCORE:{c}')
    print("")

