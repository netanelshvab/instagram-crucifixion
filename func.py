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
    Fetch information about the followers of the main Instagram account and their followers.

    Args:
    - profile: Instaloader Profile object representing the main Instagram account.

    Returns:
    - followers_info: A list of dictionaries containing information about each follower and their followers. Each dictionary includes:
    - 'user_name': Username of the follower.
    - 'profile_photo': URL of the follower's profile photo.
    - 'follower_followers': List of usernames of the followers of the follower.
    """

    followers_info = []
    for follower in profile.get_followees():
        print(follower.username)
        follower_info = {
            "user_name": follower.username,
            "profile_photo": follower.get_profile_pic_url,
            "follower_followers": [],
        }
        
        # Fetch the follower's followers
        for follower_of_follower in follower.get_followees():
            print(follower_of_follower.username)
            follower_info["follower_followers"].append(
                {
                    "user_name": follower_of_follower.username,
                    "profile_photo": follower_of_follower.get_profile_pic_url,
                }
            )
        
        followers_info.append(follower_info)
    return followers_info
