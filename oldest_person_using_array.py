# ask user to input name and age
# set conditions for valid name and age
    # full name must have 3 words
    # age should be 1-2 digits only
        # if input is invalid
            # print error message
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
            # Loop 3- retry if name is not 3 words
            while True:
                person_name = input("Please input a full name: ")

                if str.len(person_name) == 3:
                # stops Loop 3
                    break
                # Loop 4 - retry if age exceeds 2 digits
                while True:    
            
        except:
            print("Incorrect input, please try again.")