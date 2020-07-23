#n=18
#make a program which takes input from user until user insert 18.
#no of guesses 9
#print no of guessesleft
##if guesses expire print GAME OVER
#NO OF GUESSES TO FINISH
# YOU WON


#MINE PROGRAM
#print ('guess no \n')
#attempts = 5
#n=int (input())
#while (attempts<5):
 #   if (n==18):
  #      print ('You Won in',  attempts )

   #     attempts = attempts -1
    #    break


    #elif (n > 18):

     #   print('Try lesser number')

      #  print ('Try again', attempts)
       # attempts = attempts - 1
        #continue


#program2:::::
n=18
no_of_guesses=1
while(no_of_guesses<=5):
    print ('Guess the number')
    g = int (input())
    if g>18:
        print ('You have entered large number, try again')
    elif (g<18):
        print ('You have entered small no, try again')
    else:
        print ('You won')
        print (no_of_guesses, 'no of guess he took to finish')
        break
    print ('You have done in', 5-no_of_guesses)
    no_of_guesses= no_of_guesses+1
    continue
if (no_of_guesses>9):
    print('Game over')






        
