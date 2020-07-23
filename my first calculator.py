print ('enter 1st number')
a = int (input())
print ('Enter 2nd number')
b = int (input())
print ('Select one of the following ')
print ('+')
print ('-')
print ('*')
print ('/')
c = input()
if a==56 and b==7 and c=='+':
    print ('77')
elif c=='*':
    multiply=a*b
    print ('Your answer is' ,multiply)
elif c=='-':
    subs=a-b
    print ('Your answer is \n' ,subs)
elif c=='+':
    add=a+b
    print ('Your answer is \n' ,add)
elif c=='/':
    divi=a/b
    print ('Your answer is \n' ,divi)

