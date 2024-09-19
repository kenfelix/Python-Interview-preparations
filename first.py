"""14. How can you replace string space with a given character in Python?
It is a simple string manipulation challenge. You have to replace the space with a specific character.  

Example 1: a user has provided the string “l vey u” and the character “o”, and the output will be “loveyou”.

Example 2: a user has provided the string “D t C mpBl ckFrid yS le” and the character “a”, and the output will be “DataCampBlackFridaySale”.

In the `str_replace()` function, we will loop over each letter of the string and check if it is space or not. If it consists of space, we will replace it with the specific character provided by the user. Finally, we will be returning the modified string. 
"""

def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i 
    return result

text = "D t C mpBl ckFrid yS le"
ch = "a"

str_replace(text,ch)
# 'DataCampBlackFridaySale'

"""
15. Given a positive integer num, write a function that returns True if num is a perfect square else False.
This has a relatively straightforward solution. You can check if the number has a perfect square root by:

Finding the square root of the number and converting it into an integer.
Applying the square to the square root number and checking if it's a perfect square root.
Returning the result as a boolean. 
Test 1  
We have provided number 10 to the `valid_square()` function. 

By taking the square root of the number, we get 3.1622776601683795.
By converting it into an integer, we get 3.
Then, take the square of 3 and get 9.
9 is not equal to the number, so the function will return False. 
a

Test 2
We have provided number 36 to the `valid_square()` function. 

By taking the square root of the number, we get 6.
By converting it into an integer, we get 6.
Then, take the square of 6 and get 36.
36 is equal to the number, so the function will return True. 
"""

def valid_square(num):
    square = int(num**0.5)
    check = square**2==num
    return check

valid_square(10)
# False
valid_square(36)
# True

"""
16. Given an integer n, return the number of trailing zeroes in n factorial n!
To pass this challenge, you have to first calculate n factorial (n!) and then calculate the number of training zeros. 

Finding factorial 
In the first step, we will use a while loop to iterate over the n factorial and stop when the n is equal to 1. 

Calculating trailing zeros
In the second step, we will calculate the trailing zero, not the total number of zeros. There is a huge difference. 


7! = 5040
Powered By 
The seven factorials have a total of two zeros and only one trailing zero, so our solution should return 1. 

Convert the factorial number to a string.
Read it back and apply for a loop.
If the number is 0, add +1 to the result, otherwise break the loop.
Returns the result.
The solution is elegant but requires attention to detail. 
"""

def factorial_trailing_zeros(n):

    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    result = 0

    for i in str(fact)[::-1]:
        if i == "0":
            result += 1
        else:
            break

    return result


factorial_trailing_zeros(10)
# 2
factorial_trailing_zeros(18)
# 3

"""
Take the essential practicing coding interview questions course to prepare for your next coding interviews in Python.

FAANG Python Interview Question
Below, we’ve picked out some of the questions you might expect from the most sought-after roles in the industries, those at Meta, Amazon, Google, and the like. 

Facebook/Meta Python interview questions
The exact questions you’ll encounter at Meta depend largely on the role. However, you might expect some of the following: 

17. String segmentation
You are provided with a large string and a dictionary of the words. You have to find if the input string can be segmented into words using the dictionary or not.  

String segmentation

Image by Author

The solution is reasonably straightforward. You have to segment a large string at each point and check if the string can be segmented to the words in the dictionary.

Run the loop using the length of the large string.
We will create two substrings. 
The first substring will check each point in the large string from s[0:i]
If the first substring is not in the dictionary, it will return False.
If the first substring is in the dictionary, it will create the second substring using s[i:0].
If the second substring is in the dictionary or the second substring is of zero length, then return True. Recursively call `can_segment_str()` with the second substring and return True if it can be segmented. 
"""

def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        first_str = s[0:i]
        if first_str in dictionary:
            second_str = s[i:]
            if (
                not second_str
                or second_str in dictionary
                or can_segment_str(second_str, dictionary)
            ):
                return True
    return False


s = "datacamp"
dictionary = ["data", "camp", "cam", "lack"]
can_segment_str(s, dictionary)
# True

"""
18. Remove duplicates from sorted array
Given an integer sorted array in increasing order, remove the duplicate numbers such that each unique element appears only once. Make sure you keep the final order of the array the same.

It is impossible to change the length of the array in Python, so we will place the result in the first part of the array. After removing duplicates, we will have k elements, and the first k elements in the array should hold the results. 

Remove duplicates from sorted array

Image from LeetCode

Example 1: input array is [1,1,2,2], the function should return 2. 

Example 2: input array is [1,1,2,3,3], the function should return 3.

Solution:

Run the loop for the range of 1 to the size of the array.
Check if the previous number is unique or not. We are comparing previous elements with the current one.  
If it is unique, update the array using insertIndex, which is 1 at the start, and add +1 to the insertIndex. 
Return insertIndex as it is the k. 
This question is relatively straightforward once you know how. If you put more time into understanding the statement, you can easily come up with a solution. 
"""

def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
removeDuplicates(array_1)
# 4


array_2 = [1,1,3,4,5,6,6]
removeDuplicates(array_2)
# 5

"""
19. Find the maximum single sell profit
You are provided with the list of stock prices, and you have to return the buy and sell price to make the highest profit. 

Note: We have to make maximum profit from a single buy/sell, and if we can’t make a profit, we have to reduce our losses. 

Example 1: stock_price = [8, 4, 12, 9, 20, 1], buy = 4, and sell = 20. Maximizing the profit. 

Example 2: stock_price = [8, 6, 5, 4, 3, 2, 1], buy = 6, and sell = 5. Minimizing the loss.

Solution:

We will calculate the global profit by subtracting global sell (the first element in the list) from current buy (the second element in the list). 
Run the loop for the range of 1 to the length of the list. 
Within the loop, calculate the current profit using list elements and current buy value. 
If the current profit is greater than the global profit, change the global profit with the current profit and global sell to the i element of the list.
If the current buy is greater than the current element of the list, change the current buy with the current element of the list. 
In the end, we will return global buy and sell value. To get global buy value, we will subtract global sell from global profit.
The question is a bit tricky, and you can come up with your unique algorithm to solve the problems. 
"""

def buy_sell_stock_prices(stock_prices):
    current_buy = stock_prices[0]
    global_sell = stock_prices[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(stock_prices)):
        current_profit = stock_prices[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = stock_prices[i]

        if current_buy > stock_prices[i]:
            current_buy = stock_prices[i]

    return global_sell - global_profit, global_sell

stock_prices_1 = [10,9,16,17,19,23]
buy_sell_stock_prices(stock_prices_1)
# (9, 23)


stock_prices_2 = [8, 6, 5, 4, 3, 2, 1]
buy_sell_stock_prices(stock_prices_2)
# (6, 5)

"""
Amazon Python interview questions
Amazon Python interview questions can vary greatly but could include: 

20. Find the missing number in the array
You have been provided with the list of positive integers from 1 to n. All the numbers from 1 to n are present except x, and you must find x. 

Example:

4

5

3

2

8

1

6

n = 8 
missing number = 7
This question is a simple math problem.

Find the sum of all elements in the list.
By using arithmetic series sum formula, we will find the expected sum of the first n numbers. 
Return the difference between the expected sum and the sum of the elements.  
"""

def find_missing(input_list):

  sum_of_elements = sum(input_list)
 
  # There is exactly 1 number missing
  n = len(input_list) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
 
  return int(actual_sum - sum_of_elements)
list_1 = [1,5,6,3,4]


find_missing(list_1)
# 2

"""
21. Pythagorean Triplet in an array
Write a function that returns True if there is a Pythagorean triplet that satisfies a2+ b2 = c2

Example:

Input

Output

[3, 1, 4, 6, 5] 

True 

[10, 4, 6, 12, 5] 

False 

Solution:

Square all the elements in the array.
Sort the array in increasing order.
Run two loops. The outer loop starts from the last index of the array to 1 and the inner loop starts from (outer_loop_index -1) to the start.
Create set() to store the elements between outer loop index and inner loop index.
Check if there is a number present in the set which is equal to (array[outerLoopIndex] – array[innerLoopIndex]). If yes, return True, else False. 
"""

def checkTriplet(array):
    n = len(array)
    for i in range(n):
        array[i] = array[i]**2

    array.sort()

    for i in range(n - 1, 1, -1):
        s = set()
        for j in range(i - 1, -1, -1):
            if (array[i] - array[j]) in s:
                return True
            s.add(array[j])
    return False


arr = [3, 2, 4, 6, 5]
checkTriplet(arr)
# True

"""
22. How many ways can you make change with coins and a total amount?
We need to create a function that takes a list of coin denominations and total amounts and returns the number of ways we can make the change. 

In the example, we have provided coin denominations [1, 2, 5] and the total amount of 5. In return, we got five ways we can make the change. 

make change with coins

Image by Author

Solution:

We will create the list of size amount + 1. Additional spaces are added to store the solution for a zero amount.
We will initiate a solution list with 1.
We will run two loops. The outer loop will return the number of denominations, and the inner loop will run from the range of the outer loop index to the amount +1.
The results of different denominations are stored in the array solution. solution[i] = solution[i] + solution[i - den]
The process will be repeated for all the elements in the denomination list, and at the last element of the solution list, we will have our number.
"""

def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]

    return solution[len(solution) - 1]

denominations = [1,2,5]
amount = 5

solve_coin_change(denominations,amount)
# 4

"""
Google Python interview questions
As with the other companies mentioned, Google Python interview questions will depend on the role and level of experience. However, some common questions include:

23. Define a lambda function, an iterator, and a generator in Python.
The Lambda function is also known as an anonymous function. You can add any number of parameters but with only one statement. 

An iterator is an object that we can use to iterate over iterable objects like lists, dictionaries, tuples, and sets.

The generator is a function similar to a normal function, but it generates a value using the yield keyword instead of return. If the function body contains yield, it automatically becomes a generator.  

Read more about Python iterators and generators in our full tutorial. 

24. Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
This question is quite straightforward but requires special attention to detail. We are provided with an array of positive integers. We have to find the maximum difference between j-i where array[j] > array[i].

Examples:

Input: [20, 70, 40, 50, 12, 38, 98], Output: 6  (j = 6, i = 0)
Input: [10, 3, 2, 4, 5, 6, 7, 8, 18, 0], Output: 8 ( j = 8, i = 0)
Solution: 

Calculate the length of the array and initiate max difference with -1.
Run two loops. The outer loop picks elements from the left, and the inner loop compares the picked elements with elements starting from the right side. 
Stop the inner loop when the element is greater than the picked element and keep updating the maximum difference using j - I. 
"""

def max_index_diff(array):
    n = len(array)
    max_diff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if array[j] > array[i] and max_diff < (j - i):
                max_diff = j - i
            j -= 1

    return max_diff

array_1 = [20,70,40,50,12,38,98]

max_index_diff(array_1)
# 6

"""
25. How would you use the ternary operators in Python?
Ternary operators are also known as conditional expressions. They are operators that evaluate expression based on conditions being True and False.

You can write conditional expressions in a single line instead of writing using multiple lines of if-else statements. It allows you to write clean and compact code. 

For example, we can convert nested if-else statements into one line, as shown below. 

If-else statement
"""

score = 75

if score < 70:
    if score < 50:
        print('Fail')
    else:
        print('Merit')
else:
    print('Distinction')
# Distinction


#Nested Ternary Operator


print('Fail' if score < 50 else 'Merit' if score < 70 else 'Distinction')
# Distinction
