import instaloader

def log_in_to_account(bot, username: str, password: str):
    """
    Log into an Instagram account using Instaloader.
    
    Args:
    - bot (Instaloader): An instance of Instaloader.
    - username (str): The username of the Instagram account.
    - password (str): The password of the Instagram account.
    
    Returns:
    - profile (Profile): An instance of Instaloader Profile representing the logged-in user's profile.
    """
    bot.login(username, password)  # Log in to the Instagram account using the provided username and password
    profile = instaloader.Profile.from_username(bot.context, username)  # Get the profile of the logged-in user
    
    print("Logged in successfully")
    
    return profile



def get_followers_of_main_account(profile):
    """
    Fetches information about the followers of a main Instagram account and their followers.

    Args:
    - profile: An Instaloader Profile object representing the main Instagram account.

    Returns:
    - followers_info: A list of dictionaries containing information about each follower and their followers. 
      Each dictionary includes:
      - 'user_name': Username of the follower.
      - 'profile_photo': URL of the follower's profile photo.
      - 'follower_followers': List of usernames of the followers of the follower.
    """

    followers_info = []
    for follower in profile.get_followees():
        print(follower.username)
        follower_info = {
            "user_name": follower.username,
            "profile_photo": follower.get_profile_pic_url
        }
    return followers_info



def get_follower_followers(follower):
    """
    Retrieves information about the followers of a given follower on a social media platform.

    Args:
    - follower: Object representing a follower on the social media platform.

    Returns:
    - follower_followers: A list of dictionaries containing information about each follower of the input follower.
      Each dictionary includes:
      - 'user_name': Username of the follower.
      - 'profile_photo': URL of the follower's profile photo.
    """
    follower_followers = []
    for follower_of_follower in follower.get_followees():
            follower_followers.append(
                {
                    "user_name": follower_of_follower.username,
                    "profile_photo": follower_of_follower.get_profile_pic_url,
                }
            )
    return follower_followers


def ask_for_followers_to_crucifixion(list_of_followers):
    """
    get a list of followers and ask the user for which usernames to crucifixion
    """
    is_user_done_entring_users = True
    user_names_list = []

    while is_user_done_entring_users:
        temp_user_name = input("enter user name to crucifixion, i done send 'done':\b")
        if  temp_user_name!="done":
            if any(x["user_name"]==temp_user_name for x in list_of_followers):
                user_names_list.append(temp_user_name)
            else:
                print("incorrect username")
        else:
            is_user_done_entring_users = False
    
    print("usernames to crucifixion:")
    for i in user_names_list:
        print(i)
    return user_names_list




