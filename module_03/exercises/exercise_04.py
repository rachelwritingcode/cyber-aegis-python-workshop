'''
Instructions:

Create a new python script called exercise_04.py
Define a new function called subtract
Pass in one argument 
Inside the subtract function, define a variable called number_two and subtract 2674 from the argument variable passed into the subtract function
Return the remaining value of the subtraction
Outside of the subtract function, define a variable called number_one with the integer value of 4011
Pass the variable number_one into the function subtract.
Outside of the subtract function, assign the value of the subtract() function return value to a variable called flag
Cast (convert) the value of flag variable from integer to string 
Add a print statement with the following format “flag{+flag+_phishing}”
Run the python file and capture the flag
'''


# define subtract function
def subtract(number_one):
    number_two = number_one - 2674  
    # use the return keyword 
    return number_two

# define two integer variables
number_one = 4011

# call the add function and pass in two variables as arguments
flag = str(subtract(number_one))
# output the value
print("flag{"+str(flag)+"_phishing}")