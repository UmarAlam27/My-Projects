#Exercise
#Design a calculator which will correctly solve all the problems except..
#..the following ones
#  45 * 3 = 555, 56 + 9 = 77,  56/6=4
# ...Your program should take operator and the two numbers as input from user and return the result
# making a faulty calculator


while(True):


    print ("Enter rrthe First no.\n")
    var1 = int (input())

    print ("Enterrr the Second no.\n")
    var2 = int (input())


    operator=input("Enter the , Available Operations: + , - , * , / , ** , %\n")

    if (max(var1, var2) == 45 and min(var1, var2) == 3 and operator == "*"):

        print("Result:", "555")

    elif (max(var1, var2) == 56 and min(var1, var2) == 9 and operator == "+"):

        print("Result:", "77")

    elif (var1== 56 and var2 == 6 and operator == "/"):

        print("Result:", "4")

    else:

        if (operator == "+"):

            print("Result:", var1 + var2)

        elif (operator == "-"):

            print("Result:", var1 - var2)

        elif (operator == "*"):

            print("Result:", var1 * var2)

        elif (operator == "/"):

            print("Result:", var1 / var2)

        elif (operator=="**"):

            print("Result:", var1 ** var2)

        elif(operator=="%"):

            print("Result:", var1 % var2)

    if((input("Do you want to continue calculating? If yes type 'Y' else type 'N' \n")).capitalize()

            =='Y'):

        continue

    else:

        print("Thank You for using the Calculator")

        break

        # created by aditya