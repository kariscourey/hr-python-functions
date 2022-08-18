# # Test if 3 is in [1, 2, 3, 4]
# test_list(3, [1, 2, 3, 4])  # Returns True

# # Test if 0 is in [1, 2, 3, 4]
# test_list(0, [1, 2, 3, 4])  # Returns False

# # Replace the line "# Write an if statement here"
# # with an appropriate if statement

# def test_list(term, items):
#     for item in items:
#         if term == item:
#             return True
#     return False


def count_vowels(word):

    num_vowels = 0

    for letter in word:
        if letter in ["a","e","i","o","u"]:
            num_vowels += 1

    return num_vowels
