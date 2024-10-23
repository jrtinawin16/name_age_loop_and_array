# ask user to input name and age
# set conditions for valid name and age
    # full name must have 3 words
    # age should be 1-2 digits only
        # if input is invalid
            # print error message
# store name and age into array
# enter prompt if user wants to enter another input
    # if yes, ask user again for input
    # if no, calculate for oldest age
        # set oldest age to 0
        # set oldest entry to ages inside of array
        # if the inserted age is greater than oldest age
            # define new oldest_age to inserted age
            # define inserted age as oldest entry
        # return oldest entry
        # display name and age of oldest person

group_of_persons = {}

# Loop 1 - ask user to enter next name and age
while True:
    # Loop 2 - automatically retry if input has error
    while True:
        try:
            # Loop 3- retry if name is not 3 words
            while True:
                try:
                    person_name = input("Please input a full name: ")
                    if len(person_name.split()) == 3: 
                        # stops Loop 3
                        break
                except: 
                    continue         
            # Loop 4 - retry if age exceeds 2 digits
            while True: 
                person_age = int(input("Please input an age: "))

                if len(str(person_age)) <= 2:
                    # stops Loop 4
                    break
                    
            group_of_persons[person_name] = {
                "person_name" : person_name,
                "person_age" : person_age
            } 
            
            retry = input("Retry? (y/n): ")
            break
        except:
            print("Incorrect input, please try again.")
    
    if retry == "n":
        # stops Loop 1
        break
    elif retry != "y":
        print("Invalid answer, please try again.")

def find_highest(group_of_persons): 
    oldest_age = 0
    oldest_entry = {}
    for entry in group_of_persons.values():
        if entry ["person_age"] > oldest_age:
            oldest_age = entry["person_age"]
            oldest_entry = entry

    return oldest_entry

oldest_entry = find_highest(group_of_persons)
print("The oldest person is:")
print(oldest_entry["person_name"])
print("with an age of:")
print(oldest_entry["person_age"])