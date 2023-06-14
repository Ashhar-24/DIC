# Topics covered:

# Global variables, Functions
# Type conversion, input() function, print() function, concatenating strings, formatted strings
# While loop, for loop, if-else statements, 
# List[1-D array], Nested lists[2-D array], Dictionary
# Asterisk operator (*) for printing items of list




import random  # Random library/module to generate random no.s

MAX_LINES = 3  # Global variable (defined using all capital letters)
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {  # a dictionary
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {  # a dictionary
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# Dictionary and List:
# List: It is a collection of multiple values of different data types in a single variable. Defined by enclosing comma-separated values in square brackets [ ]
#       Eg: my_list = [1, 2, 3, "apple", "banana", True]
#       Lists are indexed (similar to arrays). Can access/modify using index. ie, print(my_list[0])    # Output: 1 ||
#       Also support negative indexing, where -1 refers to the last element. ie,  print(my_list[-1])   # Output: True
#       List are mutable (can be changed or modified after it is created ie, can alter its state, add or remove elements, or update its values without creating a
#       new instance of the object). Can assign a new value to a specific index or use methods like append(), insert(), remove(), and pop() to add or remove elements.
#       ie, my_list[2] = 5            # Modifying an element
#           my_list.append("pear")    # Appending a new element at the end of the object
#           my_list.remove("banana")  # Removing an element
#           my_list.pop(0)            # Removing an element by index
#

# Dictionary: It is a collection of key-value pairs. Defined by enclosing comma-separated key-value pairs in curly braces { }
#             Eg: my_dict = {"name": "John", "age": 25, "hobbies": ["reading", "music", "movies"]}
#             Dictionaries are indexed by keys (similar to associative arrays). Can access/modify using key. ie, print(my_dict["name"])    # Output: John ||
#             Dictionary are mutable (can be changed or modified after it is created ie, can alter its state, add or remove elements, or update its values without     creating a new instance of the object). Can assign a new value to a specific key or use methods like update() to add or remove elements.
#             ie, my_dict["age"] = 26            # Modifying an element
#                 my_dict.update({"hobbies": ["reading", "music", "movies"]})     # Adding an element
#                 my_dict.pop("age")              # Removing an element by key
#                 my_dict.popitem()               # Removing the last inserted key-value pair
#                 del my_dict["age"]              # Removing an element by key
#                 del my_dict                     # Deleting the dictionary
#                 my_dict.clear()                 # Removing all elements from the dictionary
#                 my_dict["address"] = "Dhaka"    # Adding an element
#                 my_dict.update({"age": 26})     # Adding an element

def check_winnings(columns,lines, bet, values):
    winnings=0
    winnigs_lines= []
    for line in range(lines):                     # checking each rows
        symbol = columns[0][line]                 # storing the first element of each row
        for column in columns:                    # looping through each column and check for the symbol
            symbols_to_check = column[line]       # checking the first symbol at each row 
            if symbols_to_check != symbol:        # if the first symbol is not equal to the symbol in the first row then break
                break
            else:                                   
                winnings += values[symbol] * bet
                winnigs_lines.append(lines + 1)

    return winnings, winnigs_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                                # defining a list
    for symbol, symbol_count in symbols.items():  # .item will give the key & item associated with the disctionary
        for _ in range(symbol_count):            # _ : anonymous variable defined
            all_symbols.append(symbol)

    columns = []                   # columns= [[], []] Nested list ie, a Matrix/ 2-D array with items in first list corresponds to first row and 2 list to 2nd row and  so on.
    for _ in range(cols):
        column = []
        cuurent_symbols = all_symbols[:]             # : helps to copy the elements
        for _ in range(rows):
            value = random.choice(cuurent_symbols)
            cuurent_symbols.remove(value)            # removing the first instance of the value from the list 'current_symbols'
            column.append(value)                     # adding value to the column list

        columns.append(column)

    return columns


def print_slot_machine(columns):                       # Printing the Transpose of the list
    for row in range(len(columns[0])):                 # len() returns the length of the object
        for i, column in enumerate(columns):           # prints the first row
            if i != len(columns) -1 :
                print(column[row], end=(" | "))        # As print() by default ends with a new line, hence to avoid new line we're ending with |
            else:
                print(column[row]) 

        print()                                       # Empty print() function will ouput a new line so that new row is printed on new line


def deposit():
    while True:
        # As python is Object-oriented language hence the VARIABLES defined are OBJECTS and the FUNCTIONS defined are METHODS
        amount = input("What would you like to deposit? Rs. ")
        if amount.isdigit():  # checking for users input to be a whole no. If it is not else statement will be executed & above print statement will be executed
            # converting into int data type as input() takes everything as string
            amount = int(amount)
            if amount > 0:
                break  # will cause the while loop to break and 'return amount'  will be executed
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_no_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on: (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  # checking for users input to be a whole no. If it is not else statement will be executed & above print statement will be executed
            # converting into int data type as input() takes everything as string
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break  # will cause the while loop to break and 'return amount'  will be executed
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? Rs. ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # formatted string, ie. used to concatenate two or more strings/values/functions/any expression
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have sufficient balance. Your current balance is Rs.{balance}")
        else:
            break

    print(
        f"You're betiing Rs.{bet} on {lines} lines. Total bet is equal to: Rs.{total_bet}.")
    
    slots=get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won Rs. {winnings}.")
    print(f"You won on lines: ", *winnings_lines)  
    #By using the asterisk (*) operator, the elements of the winnings_lines list will be printed as separate values, rather than as a single list. For example, if winnings_lines is [1, 2, 3], the elements will be unpacked as 1, 2, 3 and printed as separate values.
    return winnings - total_bet

# function execution
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: Rs. {balance} ")
        answer = input("Press enter to play (q to quit).")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with Rs. {balance}")

main()