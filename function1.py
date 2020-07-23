#1 Way of writing function
# def suumm (x,y):
#     return x+y
# x= suumm(5,6)
# print (x)

#2 Way of writing function using lambda


# x= (lambda a,b:a+b)
# print (x(5,6))
#OR
x= (lambda a,b:a+b)
a=int (input('Enter 1st number \n'))
b=int (input('Enter 2nd number\n'))
print (x(a,b))

