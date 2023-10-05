""" First Reverse
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

Examples
Input: "coderbyte"
Output: etybredoc

Input: "I Love Code"
Output: edoC evoL I

Tags
string manipulation """

def FirstReverse(strParam):

  # code goes here
  # 1. in python [::-1] means reversing a string, list, or any iterable with an ordering.
  
  return strParam[::-1]

# keep this function call here 
print(FirstReverse(input()))
