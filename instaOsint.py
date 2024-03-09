import instaloader

def login(username):
    InstaObject = instaloader.Instaloader()
    try:
        InstaObject.load_session_from_file(username)
    except FileNotFoundError:
        print("Session file does not exist yet - Logging in.")
        InstaObject.context.username = username
        InstaObject.interactive_login(username)  
    except instaloader.exceptions.BadCredentialsException:
        print("Login failed! Invalid username or password.")
        return None
    return InstaObject

def get_profile_info(username, L):
     if not L:
        print("Login failed. Exiting.")
        return

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    L = login(username)
    if L:
        target_username = input("Enter the Instagram username you want to investigate: ")
        get_profile_info(target_username, L)
