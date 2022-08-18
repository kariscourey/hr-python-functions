# Define function
def change_name(player_name):  # player_name = parameter # "paren"
    player_name = str(player_name)
    message = "your name is: " + player_name
    print(message)
    new_name = input("what name do you want? ")
    new_name = str(new_name)
    print("name now set to " + new_name)
    return new_name

# "Call" or "invoke" function with given arg for param
change_name("Jay") # jay = argument (value parameter is going to hold)
change_name("Bart")
