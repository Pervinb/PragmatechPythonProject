#  1) Write a Python function to sum all the numbers in a list.


#  Sample List : (8, 2, 3, 0, 7) Expected Output : 20 

 
list = [8, 2, 3, 0, 7]

def summ(num):
    
    sum= 0

    for i in num:

         sum+= i

    return sum


print(summ(list))

# 2)Write a Python function to multiply all the numbers in a list. 

# Sample List : (8, 2, 3, -1, 7) Expected Output : -336

list = [8, 2, 3, -1, 7]

def multiply(num):
    
    a= 1

    for i in num:

         a*= i

    return a

x = multiply(list)
print(x)

# 3)Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week
# #  ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.

def get_value(i):
    for key, value in my_dict.items():
         if i == key:
             return value
 
    return "key doesn't exist"
 

 
my_dict ={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Satuday", 7:"Sunday"}
print(get_value(1))
print(get_value(2))

# 4)Write a function called lastElement. This function takes one parameter (a list) and returns the last value in the list.
#  It should return None if the list is empty.

# Example Output lastElement([1,2,3]) # 3 lastElement([]) # None



def list_test (list1):
    if not list1      :
         print('list is empty')
    else: 
        print(list1[-1])


list_test([])
list_test([1,2,3])

# 5)Write a Python program to print the even numbers from a given list. 

# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]  
 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list1:
   if num % 2 == 0:
      print(num, end = " ")


