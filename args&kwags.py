def funargs_kwags(normal, *bcs, **acs ): # * and ** is called args and kwargs respectively
    print (normal)
    for i in bcs :
        print (i)
    for key, value in acs.items():
        print (f"{key}, 'is a', {value}") #without f" values of key and value wont insert


normal = f"I m a normal student, other students are"
bcs= ['Umar', 'Mehroo', 'Mado', 'Kala billa']
acs= {'hamid':'the programer', 'Maira':'The actor', 'Wasif': 'The Poet'}
funargs_kwags(normal, *bcs, **acs)

