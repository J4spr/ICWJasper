'''
Program to see what bakery you want to go to
'''

name = "mateo"

bread = "tijgerbrood"
bread1 = "pistolet"
bread2 = "volkorenbrood"

# assign values in array
bakery = [bread, bread1, bread2, ""]

# print the bread on a second shelf
# print ("The bread on the second plank is a", bakery[1])

competingbakery = [bread, "rozijnenbrood", bread2, bread1]

if bakery[0] == competingbakery[0] and bakery[1] == competingbakery[1] and bakery[2] == competingbakery[2]:
    print("serious competitions")

if bakery[0] == competingbakery[0] or bakery[1] == competingbakery[1] or bakery[2] == competingbakery[2]:
    print("succes")

'''
# compare shelfs with eachother
if bakery[0] == competingbakery[0]:
    print("choosing stress")

if bakery[1] == competingbakery[1]:
    print("choosing stress")

if bakery[2] == competingbakery[2]:
    print("choosing str#ess")

if bakery[3] == competingbakery[3]:
    print("choosing stress")

# assign variable to user input
userinput = input("Give name of bread")
bakery[3] = userinput

# compare without error of array index list out of bounds
if bakery[3] == competingbakery[3]:
    print("choosing stress")
else:
    print("not")

a, b = 9, 5
# c = input("geef een nummer voor c:")
print(a + b + c)
'''
if "rozijenenbrood" in bakery:
    print("rozijenbrood is there")
elif "croissant" in bakery:
    print("geen rozijn , wel croissant")
else:
    print("de bakkerij is best zielig")

# make for loop
for i in competingbakery:
    print(i)
for i in bakery:
    print(i)
