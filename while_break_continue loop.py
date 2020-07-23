#create a program which takes input from user until he insert a number
# greater than 100. if he insert a number greater than 100, print congratulations.
while (1):
    print ('insert a number \n')
    a= int (input())
    if a>100:
        print ('congrats')
        break
    else:
        print('enter again')
        continue