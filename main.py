import instaloader
from func import *
import tkinter as tk

def main(args=None):
    # Creating an instance of the Instaloader class
    bot = instaloader.Instaloader()

    username = input("enter username:")
    password = input("enter password:")

    # Log in to the Instagram account
    didnt_pass_true = True
    while didnt_pass_true:
        try:
            profile = log_in_to_account(bot, username, password)
        except(instaloader.exceptions.ConnectionException):
            print("wrong password, enter again:")
            username = input()
            didnt_pass_true = True
        except(instaloader.exceptions.BadCredentialsException):
            print("wrong password, enter again:")
            username = input()
            didnt_pass_true = True
        else:
            didnt_pass_true = False

    #get the main account followers
    followers_info = get_followers_of_main_account(profile=profile)
    
    #ask which usernames to crucifixion
    user_name_list_to_crucifixion = ask_for_followers_to_crucifixion(followers_info)

    #get the users list before crufixion and return the mutual users
    mutual_users_list = crucifixion_in_order_to_find_mutual_users(user_name_list_to_crucifixion, profile)

    print(mutual_users_list)


if __name__ == "__main__":
    main()
