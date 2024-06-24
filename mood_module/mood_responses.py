#Task 1: Your Mood Today

#Problem Statement: Create a Python program using a custom module holding a function that asks the user how they #are feeling today and responds with a custom message based on the mood entered. This function should then be #imported and used in another file "main.py".

def mood_responses(mood):
    if mood == "happy":
        return "It's great to see you happy!"
    elif mood == "sad":
        return "I'm sorry to hear that you are sad. Have you considered thinking about her to make it worse?"
    elif mood == "stressed":
        return "Take a deep breath and relax. Why not plan a deep state assassination?"
    elif mood == "excited":
        return "I'm glad you are excited! Did you finally get DeSantis?"
    elif mood == "relaxed":
        return "Enjoy your relaxation time."
    elif mood == "angry":
        return "Take a break and go scream at traffic. It's what I do."