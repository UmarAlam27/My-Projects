'''Make a program using object oriented programing andd classes
that takes inputt of particulars of candidates inn specific
format annd give output'''

class candidate:
    def __init__(self, rank, name, pak, trade, unit, service):
        self.rankk=rank
        self.name=name
        self.pakk=pak
        self.trade=trade
        self.unit=unit
        self.service=service
    def printout (self):
        return f'Rank:{self.rankk}\nName:{self.name}\nPak:{self.pakk}\nTrade:{self.trade}\nUnit:{self.unit}\nService:{self.service}'
printoutt= candidate('sep', 'Umar', '1111', 'Eps', '414 Eq', '10 yrs')
print (printoutt.printout())

#Above prgram can be made without using classes as below '''
# def candy(rank, name, pak):
#     return f'The rank is {rank}\nName is {name}\nPak is {pak}'
# a= 'Flt Lt'
# b= 'Umar'
# c='17013'
# print (candy(a,b,c))


#2 class employee:
#     def __init__(self, name, grade,school):
#         self.name= name
#         self.grade=grade
#         self.school=school
#     def printdetails (self):
#         return  f'The name is {self.name}. The grade is {self.grade}. The school is {self.school}'
#
#
# umar = employee ('umar',12,'FDC')
#
# print (umar.printdetails())
