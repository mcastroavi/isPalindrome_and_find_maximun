"""
QUESTION 1:
========================================================================================================
Given a list of numbers, write a function to find the maximum number in the list.
Do Not Use the built-in Python function max.
Note: For the purpose of this problem, we define that an empty list will return None.

NOTE: DO NOT USE THE PYTHON FUNCTION max. WRITE your program using a loop. 

Example 1:
========================================
Input: [10, 5, 20, 15, 25]
Output: 25

Example 2:
========================================
Input:[10,10,10]
Output: 10

Example 3:
========================================
Input: []
Output: None
"""

def find_maximum(numbers):
    length = len(numbers)
    if length == 0:
        return None
    elif length == 1:
        return numbers[0]; 
    else:    
        for i in range(0, length):
            for j in range(i+1, length):
                if numbers[i] >= numbers[j]:
                    numbers[i], numbers[j] = numbers[j],numbers[i]
                
            return numbers[j]



"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome. Write a function
named isPalindrome that takes a string as an input and returns a bool as an output.

Hint: refer to the following example on how to reverse a string.

>>> S = "abc"
>>> S[::-1]
'cba'


Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  amanaplanacanalPanama
which reads the same as backward and forward, so it is true.

Example 2:
=========================================
Input: "race a car"
Output: false

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  raceacar
which does not read the same as backward and forward, so it is false.
"""

def isPalindrome(x):
    strings = str(x)
    main =list(filter(lambda a: a.isalnum() , strings.lower()))
    reversed_main = main[::-1]
    if main == reversed_main:
        return True 
    else:
        return False
