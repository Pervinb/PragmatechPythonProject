mark1 = int(input("Enter your English marks: "))
mark2 = int(input("Enter your Physics marks: "))
mark3 = int(input("Enter your Math marks: "))
mark4 = int(input("Enter your Bio marks: "))
total = 400


if mark1 and mark2 and mark3 and mark4 > 90:
    print("Conguratulation your grade is in A grade ")
elif 80 < mark1 and mark2 and mark3 and mark4  <=90:
    print("your grade B")
elif 70 < mark1 and mark2 and mark3 and mark4  <=80:
    print("your grade C")
else:
    print("You failed")


print("total")
total_marks = mark1 + mark2 + mark3 + mark4
print(total_marks)   
percentage = total_marks/total 
