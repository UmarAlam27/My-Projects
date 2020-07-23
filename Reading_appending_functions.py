##create and write a new file
##handle write only that washes already written text in text file
# f = open('u2u.txt', 'w')
# f.write('hi whatsuppp, na kro')
# f.close()

##handle fun that write and doesnot alter already written text in file
f= open('nakro.txt', 'a')
a=f.write('hi whatsuppp, na kro, acha') #append mode
f.close()

##handle read only
# f = open('u2u.txt', 'r')
# print (f.read())
# f.close()

##handle read and write both
#f = open('u2u.txt', "r+")
#print(f.read())
#f.write('thank u')
#f.close()