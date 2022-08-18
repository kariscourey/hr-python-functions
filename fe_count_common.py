first = [2, 5, 4, 1]
second = [3, 5, 2, 1]

# Write the function count_common_entries, here
#   It should have two parameters
#   It should return the number of common entries
#     between the two lists

def count_common_entries(first, second):

    common = 0

    for i in first:
        if i in second:
            common += 1

    return common

count_common_entries(first, second)
