"""
Print number in following pattern
*
*	*
*	*	*
*	*	*	*
*	*	*	*	*

Steps
1) Create function for welcome message
2) Create function for asking the number
3) Create function for validating the number and converting or else stop
5) Create function to print pattern
6) Create function to ask user to continue
    a) True -> continue from step 2
    b) False -> print thank you message
7) Create function to thanks
8) Create main application function to above 1 to 7 steps in orders of application


Steps for pattern logics
1) Pattern 5 rows and 5 columns
2) Take two for loop
    a) first for loop for row
    b) second for loop for column
3) Column should print * upto row value
4) On end of each row add "\n"
"""


# 1) Create function for welcome message
def welcome_message():
    """
    Function helps to print welcome to user
    :return: None
    """
    print("Welcome to number pattern application")


# 2) Create function for asking the number
def user_input():
    """
    This function ask the user to enter positive number
    :return: User entered positive number
    """
    return input("Enter any number to print pattern\n")


# 3) Create function for validating the number and converting or else stop
def validate_input(user_data):
    """
    This function helps validate the user data
    :param user_data: number entered by user
    :return: converted number in case valid positive number else 0
    """
    if user_data.isdigit():
        return int(user_data)
    else:
        return 0


# 5) Create function to print pattern
def print_pattern(user_data):
    """
    This function helps to print patterns based on user data
    :param user_data: validated user input
    :return: None
    """
    #  Steps for pattern logics
    # 1) Pattern user data rows and user data columns

    # 2) Take two for loop
    #     a) first for loop for row
    for row in range(1, user_data + 1):
        #      b) second for loop for column
        # 3) Column should print * upto row value
        for col in range(1, row + 1):
            print("*\t", end="")
        # 4) On end of each row add "\n"
        print()


# 6) Create function to ask user to continue
#     a) True -> continue from step 2
#     b) False -> print thank you message
def continue_app():
    """
    This function ask user to continue the app or not
    :return: true in case user press 1 else false
    """
    return input("Enter 1 to continue application\n") == "1"


# 7) Create function to thanks
def thanks():
    """
    This function helps to print thank you message
    :return: None
    """
    print("Thanks for using pattern application")
    print("Please feel free to use our application again...")


# 8) Create main application function to above 1 to 7 steps in orders of application
def main_app():
    """
    This our main application for starting the app
    :return: None
    """
    # reuse = True
    welcome_message()
    while True:
        user_data = validate_input(user_input())
        if user_data:
            print_pattern(user_data)
        else:
            print("Invalid user input")
        if not continue_app():
            break
    thanks()


if __name__ == "__main__":
    main_app()
