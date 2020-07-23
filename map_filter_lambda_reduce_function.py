#1.map function
#2.lambda function
#3. filter function
#Reduce function

#------------MAP FUNCTION---------#
#Make a program that return output of numbers greater than 5 in the list
# list1 = [1,2,3,4,5,6,7,8,9]
# def gr_than_5(num):
#     return num>5
# in_list= list (map(gr_than_5,list1))
# print (in_list) #it will return True , False statment


# list1 = [1,2,3,4,5,6,7,8,9]
# def sqr(n):
#     return n*n
# in_list= list (map(sqr,list1))
# print (in_list) #square root of items in list

#------------MAP+LAMBDA----------#
list1 = [1,2,3,4,5,6,7,8,9]
in_list= list (map(lambda x:x*x,list1))
print (in_list) #square root of items using lambda

#------------FILTER----------#
# list1 = [1,2,3,4,5,6,7,8,9]
# def gr_than_5(num):
#     return num>5
# in_list= list (filter(gr_than_5,list1))
# print (in_list) #it will return numbers greater than 5

#------------REDUCE----------#
####Make a program that adds/multiply all items in the list
# a=[1,2,3,4]
# num=0
# for i in a:
#     num=num+i
# print (num)
#This can be done by using reduce function
# from functools import reduce
# a=[1,2,3,4]
# b= reduce(lambda x,y: x+y, a)
# print (b)
