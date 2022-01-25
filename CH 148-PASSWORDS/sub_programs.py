# Go-getter

def user_identification():
    """Get user ID """
    global user_id
    # USER_ID
    user_id_list = []
    correct = True
    while correct:
        user_id = input("Insert User ID:")
        if user_id in user_id_list:
            print("user id has been taken.Try another one")

        else:
            user_id_list.append(user_id)
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
        correct = True
        while correct:
            loop = 0
            for letter in password:
                if letter.isupper():
                    loop += 1

            if loop != 0:
                count += 1
                print(f"uppercase letters, count {count}")
            else:
                print(f"uppercase letters, count {count}")

            correct = False

        # condition 3- lowercase letters

        correct = True
        while correct:
            loop = 0
            for letter in password:
                if letter.islower():
                    loop += 1
            if loop != 0:
                count += 1
                print(f"lowercase letters, count {count}")
            else:
                print(f"lowercase letters, count {count}")
            correct = False

        # condition 4- include numbers

        while correct:
            loop = 0
            for letter in password:
                if letter.isdigit():
                    loop += 1

            if loop != 0:
                count += 1
                print(f"includes numbers, count {count}")
            else:
                print(f"includes numbers, count {count}")

            correct = False

        # condition 5- include  special characters
        while correct:
            loop = 0
            special_characters = ["!", "£", "$", "%", "&", "<", "*", "@"]
            list_password = list(password)
            print(list_password)
            for letter in list_password:
                if letter in special_characters:
                    loop += 1
            if loop != 0:
                count += 1
                print(f"includes special characters, count {count}")
                count += 1

            correct = False

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

        elif count == 5:
            print("You have selected a very strong password")
            correct_password = False
        else:
            print("Try again")
            correct_password = True

    return password
