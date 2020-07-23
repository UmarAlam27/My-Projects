
print ('snake game \n')
c=0
player = 0
cpu = 0
while (c<5):
    c=c+1
    a= int (input(' Press 1 for Snake \n Press 2 for Gun \n Press 3 for Water \n'))
    list1= ['snake', 'gun', 'water']
    import random
    b=random.choice (list1)
    print (b)
    if a==1 and b=="snake":
        print ('Same choice, tie')
    elif a==1 and b=="water":
        print('You lose, PC win')
        cpu+=1
    elif a==1 and b=="gun":
        print('You lose, PC win')
        cpu += 1
    elif a==2 and b=="snake":
        print ('You win, PC lose')
        player += 1
    elif a==2 and b=="water":
        print('You lose, PC win')
        cpu += 1
    elif a==2 and b=="gun":
        print('Same choice, tie')
    elif a==3 and b=="snake":
        print ('You win, PC lose')
        player += 1
    elif a==3 and b=="water":
        print('Same choice, tie')
    elif a==3 and b=="gun":
        print('You lose, PC win')
        cpu += 1
    d= int (input ('press 1 for continue , 2 for exit'))
    if d==1:
        continue
    else:
        break
if player == cpu:
    print(f"Match tied: Player: {player}\tComputer: {cpu}")
elif player > cpu:
    print(f"Finally Player won the game: Player: {player}\tComputer: {cpu}\tTie: {5-player-cpu}")
else:
    print(f"Finally Computer won the game: Computer: {cpu}\tPlayer: {player}\tTie: {5-player-cpu}")

