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

# def get_value(i):
#     for key, value in my_dict.items():
#          if i == key:
#              return value
 
#     return "key doesn't exist"
 

 
# my_dict ={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Satuday", 7:"Sunday"}
# print(get_value(1))
# print(get_value(2))

returnDay = {
1: 'Monday',
2: 'Tuesday',
3: 'Wednesday',
4: 'Thursday',
5: 'Friday',
6: 'Saturday',
7: 'Sunday',

}
 
def day(number):
    try:
        return returnDay[number]
    except:
        return "error"

print(day(5))
        
