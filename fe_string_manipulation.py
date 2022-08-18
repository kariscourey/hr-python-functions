# Write the function parse_numbers, here
#   It should have one parameter
#   It should return a list of the converted digits

# str_number = "0000"

def parse_numbers(string):

    parsed = []

    for i in string:
        parsed.append(int(i))

    return parsed

# parse_numbers(str_number)
