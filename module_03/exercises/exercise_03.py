# define add function
def add(number_one, number_two):
    number_three = number_one + number_two 
    # use the return keyword 
    return number_three

# define two integer variables
number_one = 1
number_two = 2

# call the add function and pass in two variables as arguments
number_three = add(number_one, number_two)
# output the value
print("flag{add_"+str(number_three)+"_key}")