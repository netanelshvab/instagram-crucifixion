import instaloader
from func import *
import tkinter as tk

def main(args=None):
    # Creating an instance of the Instaloader class
    bot = instaloader.Instaloader()

    username = input("enter username")
    password = input("enter password")

    # Log in to the Instagram account
    profile = log_in_to_account(bot, username, password)
    
    #get the main account followers and the followers followers info
    followers_info = get_followers_of_main_account(profile=profile)
    
    # Print the list of followers
    print("Followers:")
    for follower in followers_info:
        print(follower)



if __name__ == "__main__":
    main()
