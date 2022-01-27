# Go-getter

import csv


def user_identification():
    """Get user ID """
    global user_id
    # USER_ID
    correct = True
    while correct:
        user_id = input("Insert User ID:")
        with open("user_data.csv", "r") as f:
            iterable = csv.reader(f)
            dd_list = list(iterable)
            loop = 0
            # manufactured loop
            for row in dd_list:
                if user_id in row:
                    loop += 1

            if loop != 0:
                print("user id has been taken.Try another one")
            else:
                correct = False
    return user_id


def user_password():
    """ Get user password"""
    global password
    # PASSWORD
    correct_password = True
    while correct_password:
        password = input("Insert password: ")
        count = 0

        # condition 1-8 characters
        if len(password) >= 8:
            count += 1
            print(f"password greater than 8, count {count}")
        else:
            count = count
            print(f"password less than 8, count {count}")

        # condition 2- uppercase letters
        loop = 0
        for letter in password:
            if letter.isupper():
                loop += 1

        if loop != 0:
            count += 1
            print(f"uppercase letters, count {count}")
        else:
            print(f"uppercase letters, count {count}")

        # condition 3- lowercase letters
        loop = 0
        for letter in password:
            if letter.islower():
                loop += 1
        if loop != 0:
            count += 1
            print(f"lowercase letters, count {count}")
        else:
            print(f"lowercase letters, count {count}")

        # condition 4- include numbers
        loop = 0
        for letter in password:
            if letter.isdigit():
                loop += 1
        if loop != 0:
            count += 1
            print(f"includes numbers, count {count}")
        else:
            print(f"includes numbers, count {count}")

        # condition 5- include  special characters
        loop = 0
        special_characters = ["!", "£", "$", "%", "&", "<", "*", "@"]
        list_password = list(password)
        for letter in list_password:
            if letter in special_characters:
                loop += 1
        if loop != 0:
            count += 1
            print(f"includes special characters, count {count}")

        # CHECKING IF PASSWORD HAS MET THE THRESHOLD
        if count <= 2:
            print("Sorry, this password is weak.")
            correct_password = True

        elif count == 3 or count == 4:
            print("This password can be improved\n")
            try_again = input("Do you want to try again (y/n): ")
            if try_again == "y":
                correct_password = True
            elif try_again == "n":
                correct_password = False

        elif count >= 5:
            print("You have selected a very strong password")
            correct_password = False

    return password


def add_to_csv(user_identity, user_pswd):
    """Adds user id and password to a csv file"""
    with open("user_data.csv", "a") as f:
        f.write(str(user_identity) + "," + str(user_pswd) + "\n")


def display_csv():
    """Adds user id and password to a csv file"""
    with open("user_data.csv", "r") as f:
        iterable = csv.reader(f)
        dd_list = list(iterable)
        for item in dd_list:
            print(item[0])


def change_password():
    """ Change password in csv and save it a csv"""
    global user_idt
    correct = True
    while correct:
        user_idt = input("Insert User ID:")
        with open("user_data.csv", "r") as f:
            iterable = csv.reader(f)
            dd_list = list(iterable)
            loop = 0
            for item in dd_list:
                if user_idt in item:
                    loop += 1
            if loop != 0:
                print("user id in list")
                correct = False
            else:
                print("User ID not in list."
                      "\ntry again")

    return user_idt


def save_to_csv(new_user_id, new_password):
    tmp = []
    with open("user_data.csv", "r") as f:
        iterable = csv.reader(f)
        dd_list = list(iterable)

        for item in dd_list:
            if item[0] == new_user_id:
                new_data = [item[0], new_password]
                tmp.append(new_data)
            else:
                data = [item[0], item[1]]
                tmp.append(data)
    with open("user_data.csv", "w") as f:
        for row in tmp:
            overwrite_data = row[0] + "," + row[1] + "\n"
            f.write(overwrite_data)








