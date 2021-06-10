#  1) Write a Python function to sum all the numbers in a list.


#  Sample List : (8, 2, 3, 0, 7) Expected Output : 20 

 
list = [8, 2, 3, 0, 7]

def summ(num):
    
    sum= 0

    for i in num:

         sum+= i

    return sum


print(summ(list))


list = [8, 2, 3, -1, 7]

def multiply(num):
    
    a= 1

    for i in num:

         a*= i

    return a

x = multiply(list)
print(x)


