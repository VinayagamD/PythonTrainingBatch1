
def take_user_input():
    return int(input("Enter Number for rows for pattern:\n"))


def print_pattern(rows):
    """
    require 3 loops
    1) Row loop
    2) Space loop
    3) Column loop
    :param rows: Number of rows to print
    :return: none
    """

    for row in range(1, rows+1):
        temp_row = row
        first_value_printed = False
        dec_reached = False
        for space in range(0, (rows-row)):
            print(" ", end=" ")
        for _ in range(0, (2*row)-1):
            if not first_value_printed:
                print(temp_row, end=" ")
                first_value_printed = True
            else:
                if dec_reached:
                    temp_row += 1
                else:
                    temp_row -= 1
                print(temp_row, end=" ")
                if temp_row == 1:
                    dec_reached = True
        print()


def run_pattern_application():
    rows = take_user_input()
    print_pattern(rows)


if __name__ == '__main__':
    run_pattern_application()
