import random 

def get_choice(player_name):
    while True:
        try:
            choice=input(f"{player_name},ENTER rock /paper/scissor :").lower()
            if choice in ['rock','paper','scissor']:
                return choice
            else:
                print("invalid choice")
        except Exception as e:
            print(" error",e)

def decide_win(p1,p2):
    if(p1==p2):
        print("IT'S A TIE ")
    elif(p1=='rock' and p2=='scissor') or \
        (p1=='scissor' and p2=='paper') or \
        (p1=='paper' and p2 =='rock'):
        print("player1 WIN")
    else:
        print("player2 WIN")
            

def player_vs_computer():
    print("PLAYER1 VS COMPUTER")
    player1=get_choice("player1")
    computer=random.choice(['rock','scissor','paper'])
    print(f"Computer chose: {computer}")
    result=decide_win(player1,computer)
    print(result)

def player_vs_player():
    print("PLAYER VS PLAYER")
    player1=get_choice("player1")
    player2=get_choice("player2")
    result=decide_win(player1,player2)
    print(result)


print(" ************* WELCOME ROCK ,PAPER ,SCISSOR GAME ************** ")
while True:
    print(" Choose Game Mode  ")
    print("1. PLAYER VS COMPUTER ")
    print("2. PLAYER VS PLAYER ")
    print("3. Quit")

    try:
        mode=input("ENTER 1/2/3 ")
        if mode=="1":
            player_vs_computer()
        elif mode=="2":
            player_vs_player()
        elif mode=="3":
            quit
        else:
             print("invalid")
        
        again=input(" PLAY AGAIN? (y/n): ").lower()
        if again!='y':
            print("GOODBYE")
            break
    
    except Exception as e:
            print("unexpected error :",e)


