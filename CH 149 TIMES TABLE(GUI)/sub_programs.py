def get_data():
    """get user data"""
    user_num = int(input("enter a number: "))
    return user_num


def times_table(user_num):
    """ prepare and display the time table"""

    # loop between user_num and 1
    for num in range(1,(user_num+1)):
        ans = num * user_num
        print(f"{num}*{user_num}={ans}")