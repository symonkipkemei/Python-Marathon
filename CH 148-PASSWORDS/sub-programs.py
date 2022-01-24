# Go-getter

def user_data():
    """Get user ID and password"""
    user_id_list = []
    for x in range(0, 2):
        correct = True
        while correct:
            user_id = input("Insert User ID")
            if user_id in user_id_list:
                print("user id has been taken.Try another one")

            else:
                user_id_list.append(user_id)
                correct = False
        count = 0
        password = input("Insert password: ")
        for x in range(0, 5):
            #condition 1
            if len(password) >= 8:
                count += 1
            elif str.isupper(password):
                count += 1
            elif str.lower(password):
                count += 1



        str.isupper(password)





