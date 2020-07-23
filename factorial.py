#Factorial Function
# def factorial1 (n):
#     if n==1:
#         return 1
#     else:
#    # a = 1
#     #for i in range (n): #n means from "i" is from 0 t0 n-1
#         #a = a * (i+1)
#         return  n * factorial1(n-1)
# print (factorial1(6))
def factorial1(n):
    if n==0:
        return  0
    elif n==1:
        return 1
    else:
        return n*(factorial1(n-1))

print(factorial1(6))