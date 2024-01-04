import random

# List of jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "What do you call a fake noodle? An impasta.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
]


def prompt_dad_joke():
    # Choose a random joke from the list
    dad_joke = random.choice(jokes)
    return dad_joke


if __name__ == "__main__":
    print("Here's a random joke for you:")
    joke = prompt_dad_joke()
    print(joke)
