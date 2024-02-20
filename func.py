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
        followers_info.append({
            "user_name": follower.username,
            "profile_photo": follower.get_profile_pic_url
        })
    return followers_info



def get_follower_followers(profile, username):
    """
    Retrieves information about the followers of a given follower on a social media platform.

    Args:
    - profile: Object representing the social media platform profile.
    - username: Username of the follower whose followers are to be retrieved.

    Returns:
    - follower_followers: A list of dictionaries containing information about each follower of the input follower.
      Each dictionary includes:
      - 'user_name': Username of the follower.
      - 'profile_photo': String indicating the function name to get the profile photo URL.
    """
    follower_followers = []
    for follower in profile.get_followers():
        if follower.username == username:
            for follower_of_follower in follower.get_followees():
                follower_followers.append(
                    {
                        "user_name": follower_of_follower.username,
                        "profile_photo": 'get_profile_pic_url()',
                    }
                )
            break  # Stop the loop once we found the follower
    return follower_followers



def ask_for_followers_to_crucifixion(list_of_followers):
    """
    Prompt the user to select followers from a list for "crucifixion".

    Args:
    - list_of_followers (list): A list of dictionaries containing information about each follower. 
      Each dictionary includes a 'user_name' key representing the follower's username.

    Returns:
    - user_names_list (list): A list of usernames selected by the user for "crucifixion".
    """
    user_names_list = []

    while True:
        temp_user_name = input("Enter a username to be crucified (type 'done' when finished): ").strip()
        if temp_user_name.lower() == "done":
            break

        found = False
        for follower in list_of_followers:
            if follower["user_name"] == temp_user_name:
                user_names_list.append(temp_user_name)
                found = True
                break

        if not found:
            print("Incorrect username. Please enter a valid username from the list.")

    print("Usernames to be crucified:")
    for username in user_names_list:
        print(username)
    return user_names_list


def crucifixion_in_order_to_find_mutual_users(users_list_to_crucifixion, profile):
    """
    Finds mutual followers among a list of users.

    Args:
    - users_list_to_crucifixion (list): A list of usernames to find mutual followers for.
    - profile: Profile object representing the social media platform profile.

    Returns:
    - mutual_followers (list): A list of dictionaries containing information about each mutual follower.
    """
    
    users_followed_by_all_users_list = []
    users_name_list = []
    mutual_followers = []
    return_mutual_followers_list = []

    for username in users_list_to_crucifixion:
        users_followed_by_all_users_list.append(get_follower_followers(profile=profile, username=username))
    
    for username_follower in users_followed_by_all_users_list:
        for username in username_follower:
            users_name_list.append(username["user_name"])

    set_user_name_list = set(users_name_list) 

    if len(set_user_name_list)==len(users_name_list):
        print("there are no mutual followers")
    else:
        for user_name_to_pop in set_user_name_list:
            users_name_list.pop(user_name_to_pop)
        
    for user_name in users_name_list:
        if users_name_list.count(user_name)==(len(users_list_to_crucifixion)-1):
            mutual_followers.append(user_name)

    for mutual_user_mame in mutual_followers:
        for username_follower in users_followed_by_all_users_list:
            for username in username_follower:
                if mutual_user_mame==username["user_name"]:
                    return_mutual_followers_list.append(username)

    return return_mutual_followers_list