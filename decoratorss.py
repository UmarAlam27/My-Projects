def dec1(func1):
    def nowexec():
        print ('Executing now')

        print ('Executed')
    return  nowexec()
a= dec1('go')
print (a)

@dec1
def qwerty():
     print ('hi')
qwerty=dec1(qwerty)
