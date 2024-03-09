import instaloader

def login(username):
    InstaObject = instaloader.Instaloader()
    try:
        InstaObject.load_session_from_file(username)
    except FileNotFoundError:
        print("Session file does not exist yet - Logging in.")
        InstaObject.context.username = username
        InstaObject.interactive_login(username)  # Prompt for password interactively
    except instaloader.exceptions.BadCredentialsException:
        print("Login failed! Invalid username or password.")
        return None
    return InstaObject


if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    L = login(username)
