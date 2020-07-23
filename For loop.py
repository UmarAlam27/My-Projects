#Create a random list of any thing and then print out  numbers from it that are graeter than 6.

a = ['harry', 'sherry', 'Larry', 'berry', 6, 9, 10, 11, 'marie', 24]
#print (a[0], a [2])
for item in a:

    if str(item) .isdigit() and item>6:
        print(item)
