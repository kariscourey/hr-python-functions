first = [2, 5, 4, 1]
second = [3, 5, 2, 1]

# # Combine the list into pairs
# pairs = zip(first, second)

# # Print out each pair
# for a, b in pairs:
#     print(a, b)


# Write the function count_exact_matches, here
#   It should have two parameters
#   It should return the number of exact matches between
#     the two lists
def count_exact_matches(list1, list2):

    matches = 0

    # for a, b in zip(list1, list2):
    for item in zip(list1, list2):
        if item[0] == item[1]:
            matches += 1

    print(matches)
    return matches

count_exact_matches(first, second)
