def print_names(first_name, last_name):
    print(first_name, last_name, sep="|")

print_names("Baz", "Sayid")



def is_too_fast(current_speed, max_speed):
    if current_speed <= max_speed:
        return False
    else:
        return True

is_too_fast(55, 55)



# Replace the line "# Write an if statement here"
# with an appropriate if statement

def test_list(term, items):
    for item in items:
        if term == items: # better: if term in items
            return True
    return False

# Test if 3 is in [1, 2, 3, 4]
test_list(3, [1, 2, 3, 4])  # Returns True

# Test if 0 is in [1, 2, 3, 4]
test_list(0, [1, 2, 3, 4])  # Returns False



# Write your function add_two_numbers here
def add_two_numbers(a,b):
    return a + b



def add(*numbers): # numbers = parameter
    print(numbers)

total = add(1, 2, 3, 4)
print(total)  # We expect 10



def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

total = add(1, 2, 3, 4, 3, 12)
print(total)  # We expect 10



def double_splat(**mystery):
    print(mystery)

double_splat()
double_splat(name="Noor")
double_splat(first_name="Baz", last_name="Sayid")



def function_name(parameter1, parameter2):
    do_stuff(parameter1)
    if parameters2 == parameter1:
        do_more_stuff()
    for item in parameter1:
        do_even_more_stuff(item)



def lots_of_arguments(*parameters): # any number of unnamed args
    do_stuff()
    for param in parameters:
        print(param)



def sum_of_squares(num1, num2):
    num1_squared = pow(num1, 2)
    num2_squared = pow(num2, 2)
    return num1_squared + num2_squared
