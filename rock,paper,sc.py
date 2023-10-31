import random as r
u,c=0,0
print("\n\n\t****\tROCK, PAPER AND SCISSOR GAME\t****\t\n\n\n")
print("\tINSTRUCTIONS:-")
print("\t * This is a single user vs computer game.")
print("\t * First, the user will specify the number of rounds which must be an odd number.")
print("\t * The user will be given the first chance and then computer.\n\n")
print("\t\t****    GAME STARTS    ****\n\n")
roundz=int(input("ENTER THE NUMBER OF ROUNDS: "))
print("\n******************************************************************************************************************************\n\n")
choices=['r','R','s','S','p','P']
i=0
while(i<roundz):
    f=0
    print("\t\t\t\tUSER's SCORE=",u,"\t\t\t\tCOMPUTER's SCORE=",c)
    print("\n\t\t\t\t\t----ROUND:",i+1)
    print("\n\t\t----USER'S CHANCE----")
    print("\t* For rock, PRESS r and hit enter key.")
    print("\t* For paper, PRESS p and hit enter key.")
    print("\t* For scissor, PRESS s and hit enter key.\n")
    user=input("ENTER YOUR CHOICE: ")
    print("\n\t\t----COMPUTER'S CHANCE----\n")
    comp=r.choice(choices)
    print("COMPUTER'S CHOICE:",comp)
    if (user=='r' or user=='R')and(comp=='s' or comp=='S'):
        print("\n\t- - USER WON THIS ROUND - -\n")
        u+=1
    elif(user=='s' or user=='S')and(comp=='p' or comp=='P'):
        print("\n\t- - USER WON THIS ROUND - -\n")
        u+=1
    elif(user=='p' or user=='P')and(comp=='r' or comp=='R'):
        print("\n\t- - USER WON THIS ROUND - -\n")
        u+=1
    else:
        if user.lower()==comp.lower():
            print("\n\t\tOOPS ITS A DRAW\n")
            f=1
        else:
            print("\n\t- - COMPUTER WON THIS ROUND - -\n")
            c+=1
    if f==0:
        i+=1
    print("\n\n")
if c>u:
    print("\n\n\n\t\t\t\t\t--- COMPUTER WON ---\n\n\n")
elif u>c:
    print("\n\n\n\t\t\t\t\t--- USER WON ---\n\n\n")
else:
    print("\n\n\n\t\t\t\t\t----DRAW----\n\n\n")