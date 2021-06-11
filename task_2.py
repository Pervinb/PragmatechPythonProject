# 1)Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
# 1


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:   
    print(b)
elif c>a and c>b and c>d:   
    print(c) 
elif d>a and d>b and d>c:   
    print(d)         