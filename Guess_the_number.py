#create a program that guess a number in 5 attempts and also tell you remaining attempts left with you
n=18
guesses=1

while (guesses<6):
    print ('Guess the number ')
    n= int (input())
    if (n==18):
        print ('You won')
        print ('No of attempts', guesses)
        guesses=guesses+1
        break
    elif(n<18):
        print ('Enter a greater number, your guesses left', 5-guesses)
        guesses = guesses + 1
    elif (n>18):
        print('Enter a lesser number, your guesses left', 5-guesses)
        guesses = guesses + 1

    # if guesses>5:
    #     guesses=guesses+1
    #     print ('Do you want to play more, Press', 'y')
    #     y = input()
    #     continue

























