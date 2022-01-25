from sub_programs import *


def main():
    """Backbone"""
    user_ID = user_identification()
    password = user_password()
    print(user_ID, password)


main()
