a= 'a-b-c-d-e-f-g-h/1/2/3/4/5/6/7/8/9/0'
c= '1/2/3/4/5/6/7/8/9/0'
b =c.split('/')
d=a.split('-')
print (d)
print(b)
print(a.count('-') )
print(c.count('/'))
for items in b:
    print (items, end= ' ')
