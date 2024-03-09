import instaloader

def login(username):
    InstaObject = instaloader.Instaloader()
    try:
        InstaObject.load_session_from_file(username)
    except FileNotFoundError:
        print("Session file does not exist yet - Logging in.")
        InstaObject.context.username = username
        InstaObject.interactive_login(username)  
        print("Login Successfull!!")
    except instaloader.exceptions.BadCredentialsException:
        print("Login failed! Invalid username or password.")
        return None
    return InstaObject

def get_profile_info(username, L):
    if not L:
        print("Login failed. Exiting.")
        return
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        
        if not profile.is_private:
            print("Username:", profile.username)
            print("Full Name:", profile.full_name)
            print("Biography:", profile.biography)
            print("Followers Count:", profile.followers)
            print("Followees Count:", profile.followees)
            
            print("\nFollowers:")
            for follower in profile.get_followers():
                print(follower.username)
            
            print("\nFollowees (Following):")
            for follower in profile.get_followees():
                print(follower.username)
                
        else:
            print("This profile is private.")
                
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")
                

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    L = login(username)
    if L:
        target_username = input("Enter the Instagram username you want to investigate: ")
        get_profile_info(target_username, L)
