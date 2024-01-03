import pyjokes


def generate_dad_joke():
    joke = pyjokes.get_joke(category='all')
    return joke


if __name__ == "__main__":
    print("Here's a dad joke for you:")
    joke = generate_dad_joke()
    print(joke)
