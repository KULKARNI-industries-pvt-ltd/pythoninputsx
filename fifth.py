a = str("YOUR name ")
b = str("YOUR surname ")
x = str(input(a))
y = str(input(b))
c = str("Swayam")
d = str("Kulkarni")
c1 = str("swayam")
d1 = str("kulkarni")
e = str("Aditya")
f = str("Jadhav")
e1 = str("aditya")
f1 = str("jadhav")
n = str("Your fathers name is 'Gajendra Jadhav'")
if(x==c and y==d or x==c1 and y==d1 or x==c1 and y==d or x==c and y==d1):
    print("Your fathers name is 'Sameer kulkarni'")
    pass
elif(x==e and y==f or x==e1 and y==f1 or x==e1 and y==f or x==e and y==f1):
    print(n)
else:
    print("you are not registered with us!")
    print("Lets get registered yourself!")
    a1 = str(input("Your name to register = "))
    ab1 = str(input("Your fathers_name to register = "))
    b1 = str(input("Your surname to register = "))
    print("Registered succesfully!")
    print("check yourself now!")
    pass

a2 = str(input("Your name = "))
b2 = str(input("Your surname = "))

if(a2==a1 and b2==b1):
    print("Your fathers name is = ")
    print(ab1, b1)
    pass



