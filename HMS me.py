
def getdate():

    import datetime

    return datetime.datetime.now()
print ("Health Managment System")
print ('Press 1 to Log data, Press 2 for retrieve')
i= int (input())
if (i==1):
    print ('Press 1 for Harry')
    print('Press 2 for Sherry')
    print('Press 3 for Jerry')
    a= int (input())
    if (a==1):
        print ('Press 1 for Diet, Press 2 for Exercise')
        b= int (input())
        if (b==1):
            f = open ("dietHarry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()
        else:
            f = open("ExerciseHarry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()

    if (a==2):
        print ('Press 1 for Diet, Press 2 for Exercise')
        b= int (input())
        if (b==1):
            f = open ("dietSherry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()
        else:
            f = open("ExerciseSherry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()
    if (a==3):
        print ('Press 1 for Diet, Press 2 for Exercise')
        b= int (input())
        if (b==1):
            f = open ("dietJerry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()
        else:
            f = open("ExerciseJerry1.txt", "a")
            entry1 = str(input("Enter your entry\n"))
            f.write(str(getdate())+" "+entry1+"\n")
            f.close()
if (i == 2):
    print('Press 1 for Harry')
    print('Press 2 for Sherry')
    print('Press 3 for Jerry')
    a = int(input())
    if (a == 1):
        print('Press 1 for Diet, Press 2 for Exercise')
        b = int(input())
        if (b == 1):
            f = open("dietHarry1.txt", "r")
            print (f.read())
            f.close()
        else:
            f = open("ExerciseHarry1.txt", "r")
            print (f.read())
            f.close()
    if (a == 2):
        print('Press 1 for Diet, Press 2 for Exercise')
        b = int(input())
        if (b == 1):
            f = open("dietSherry1.txt", "r")
            print (f.read())
            f.close()
        else:
            f = open("ExerciseSherry1.txt", "r")
            print (f.read())
            f.close()
    if (a == 3):
        print('Press 1 for Diet, Press 2 for Exercise')
        b = int(input())
        if (b == 1):
            f = open("dietJerry1.txt", "r")
            print (f.read())
            f.close()
        else:
            f = open("ExerciseJerry1.txt", "r")
            print (f.read())
            f.close()
print ('Press 1 to continue, Press 2 to quit')
s=int (input())
#if (s==1):






