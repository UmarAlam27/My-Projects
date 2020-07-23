class student:
    no_of_leaves=8
    pass #kuch ni
harry = student ()
larry= student()

#Harry data
harry.age=12
harry.grade=8
harry.school='FDC'
harry.leaves= 2
harry.subs=['Urdu','English']
#Larry data
larry.age=8
larry.grade=4
larry.school='FDC'
larry.subs=['Urdu','English', 'Physics']
larry.leaves=5
#output
print (larry.age,harry.school)
print (harry.__dict__)
print (student.__dict__)
