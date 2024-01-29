def greet_user():
    print("Welcome to the Greeting Program!")
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}!")

def ask_favorite_language():
    favorite_language = input("What is your favorite programming language? ")
    return favorite_language.lower()

def respond_to_language(language):
    if language == "python":
        return "Great choice! Python is a powerful and versatile language."
    elif language == "javascript":
        return "Nice! JavaScript is widely used for web development."
    elif language == "java":
        return "Excellent! Java is known for its portability and reliability."
    else:
        return f"Interesting choice! {language.capitalize()} is a cool language too."

if __name__ == "__main__":
    greet_user()
    favorite_language = ask_favorite_language()
    response = respond_to_language(favorite_language)
    print(response)

