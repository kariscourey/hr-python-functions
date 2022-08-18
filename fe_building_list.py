# my_list = []
# while len(my_list) < 4:
#     # Get a random number
#     if random_number not in my_list:
#         # add it to the list

# 1 in [3, 1, 2, 1]  # True
# 9 in [3, 1, 2, 1]  # False

# 1 not in [3, 1, 2, 1]  # False
# 9 not in [3, 1, 2, 1]  # True


from random import randint

def create_list_of_four_unique_numbers():
    my_list = []

    while len(my_list) < 4:

        random_number = randint(1,9)

        if random_number not in my_list:
            my_list.append(random_number)

    return my_list

create_list_of_four_unique_numbers()
