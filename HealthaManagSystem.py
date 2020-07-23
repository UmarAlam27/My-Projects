def getdate():

    import datetime

    return datetime.datetime.now()

i=int(input("Enter 1 to log data and 2 to retrieve data : \n"))

if i==1:

    #custom function for log

    customer=int(input("Enter 0 for Umar , 1 for Asfi , 2 for Tauqeer \n"))

    de=int(input("Enter 0 for Diet , 1 For exercise \n"))

    l1=["Umar","Asfi","Tauqeer"]

    l2=["Diet","Exercise"]


    f=open(str(l1[customer])+"_"+str(l2[de])+".txt","a")

    entry1=str(input("Enter your entry\n"))

    f.write(str(getdate())+" "+entry1+"\n")

    f.close()

elif i==2:

    # custom function for retrieve

    customer=int(input("Enter 0 for Umar , 1 for Asfi , 2 for Tauqeer \n"))

    de=int(input("Enter 0 for Diet , 1 For exercise \n"))

    l1=["Umar","Asfi","Tauqeer"]

    l2=["Diet","Exercise"]

    f=open(str(l1[customer])+"_"+str(l2[de])+".txt")

    g = f.read()

    f.close()

    print(g)

else:

    print("Are you tricking with me?")