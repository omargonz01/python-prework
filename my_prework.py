# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello" + "_username".upper())

hello_name("Username")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for numbers in range(1, 101):
        if numbers % 2 !=0:
            print(numbers)
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = a_list[1]  
    for num in a_list:
        if num>max_num:
            max_num=num

    return max_num
test = [23, 45, 12, 67, 89, 420, 34, 55]
check = max_num_in_list(test)
print("Max number is", check)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:  
        if a_year % 100 != 0 or a_year % 400 == 0:  
            return True
    return False

test_year = int((2023))
result = is_leap_year(test_year)
print(result)


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if len(a_list) < 2:
        return False  

    for a in range(len(a_list) - 1):
        if a_list[a] + 1 != a_list[a + 1]:
            return False 
    return True 
list1 = [2, 3, 4, 5, 6, 7]
list2 = [1, 2, 4, 5]

print(is_consecutive(list2))  
print(is_consecutive(list1))  


