# Python Basics

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


user_input = input("Hey user, Enter  number of days and I Will convert it into days!\n")  # Keep in mind input()
# always returns a string
user_input_number = int(user_input)
calculation_answer = days_to_units(user_input_number)
print(calculation_answer)

USERNAME = "NELSON OTIENO" # constant notation. This is a variable whose value does not change throughout the life
# of a program
name = "nelson otieno"
print(name.title())
print(name.upper())
print(name.lower())

# its better to store values in a db as lowercase and then format them as needed for output
first_name = "nelson"
last_name = "otieno"
fullname = f"{first_name} {last_name}"
print(fullname)
print(fullname.title())
print(fullname.split())

#  In general when dealing with user input, its important to verify and filter the kind of values the user
#  gives to the system because users in most cases cannot be trusted to give in right input 100% of the time.
#  Failure to do this can lead to the program going Brrr!! because the code will be unable to understand
#  what the user is going on about. Thats the lesson here.


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # This is to convert positive integers only
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
