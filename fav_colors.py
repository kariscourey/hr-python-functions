
def get_num_colors(): # code organization; refactoring - organizing into functions without changing what the program is running
    num_colors_str = input("How many fav colors do you have? ")
    num_colors = int(num_colors_str)
    return num_colors

def get_color(color_number):
    num = str(color_number + 1)
    prompt = "What is your #" + num + " fav color? "
    color = input(prompt)
    return color

# Print a greeting
print("Hi, I'd like to ask about fav colors. ")

# # Ask for input
# num_colors_str = input("How many fav colors do you have? ")

# # Turn str input into int
# num_colors = int(num_colors_str)

# Invoke get_num_colors
num_colors = get_num_colors()

# Print thanks
print("Thanks! Now I'll ask for each of those. ")

# Create list
fav_colors = []

# Loop list
for color_num in range(num_colors):
    # # Remember range creates a list starting at 0, so add 1 to make more readable
    # num = str(color_num + 1)

    # # Create string prompt to ask
    # prompt = "What is your #" + num + " fav color? "

    # # Prompt for input
    # color = input(prompt)

    # Invoke get_color
    color = get_color(color_num)

    # Add color to list
    fav_colors.append(color)

# Sort colors
sorted_colors = sorted(fav_colors)

# Print thank you
print("Thank you! Your favs: ")

# Print colors
for color in sorted_colors:
    print(" ", color)
