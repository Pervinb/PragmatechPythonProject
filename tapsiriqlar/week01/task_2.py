# 1)Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))
h = a*b*c*d
q = a+b+c+d
if a==b==c==d:
    print(h)
else:
    print(q)

# # 2) Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))
# d = int(input("Enter d:"))
# if a>b and a>c and a>d:
#     print(a)
# elif b>a and b>c and b>d:   
#     print(b)
# elif c>a and c>b and c>d:   
#     print(c) 
# elif d>a and d>b and d>c:   
#     print(d)        

# a = int(input("Menudakı meyvələrdən birini yazıb,qiymətini öyrənin!\n
# "Alma"  "heyva"  "nar" ")) 
