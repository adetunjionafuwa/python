# --------Task--------
# Complete the code in the editor below. The variables i, d, and s are already declared 
# and initialized for you. You must:

# Declare 3 variables: one of type int, one of type double, and one of type String.
# Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the + operator to perform the following operations:
# Print the sum of i plus your int variable on a new line.
# Print the sum of d plus your double variable to a scale of one decimal place on a new line.
# Concatenate s with the string you read as input and print the result on a new line.
# Note: If you are using a language that doesn't support using + for string concatenation 
# (e.g.: C), you can just print one variable immediately 
# following the other on the same line. The string provided in your editor must be printed first, 
# immediately followed by the string you read as input.

#--------Solution---------
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
j = 0
k = 0.0
l = ""
# Read and save an integer, double, and String to your variables.
j = int(input())
k = float(input())
l = input()
# Print the sum of both integer variables on a new line.
print(i + j)
# Print the sum of the double variables on a new line.
print(d + k)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + l)

#----------Alternative---------
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
arrtye = [int, float, str]
# Read and save an integer, double, and String to your variables.
x = [x(input()) for x in arrtye]
# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

print('{0} \n{1}  \n{2}'.format(i + x[0], d + x[1], s + x[2]))

