# ask user to input name and age
    # if input is invalid
    # print error message
# set conditions for valid name and age
# store name and age into array
# enter prompt if user wants to enter another input
    # if yes, ask user again for input
    # if no, display name and age of oldest person

group_of_persons = {}

# Loop 1 - ask user to enter next name and age
while True:
    # Loop 2 - automatically retry if input has error
    while True:
        try:
            name = input("Please input a name: ")
            
            # Loop 3 - retry if age is not / exceed 2 digits
            while True:  