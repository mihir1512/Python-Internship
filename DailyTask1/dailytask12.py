n1 = int(input("enter the number : "))
n2 = int(input("enter the second number : "))
n3 = int(input("enter the third number : "))

if n1 > n2:
    if (n2 > n3):
        print("{} is the greatest number".format(n1))
    else:
        print("{} is the greatest number".format(n3))
else:
    if n2 > n3:
        print("{} is the gratest number".format(n2))
    else:
        print("{} is the greatest number ".format(n3))
