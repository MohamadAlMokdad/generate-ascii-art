import random

def generate_ascii_art(width, height, characters=None):
    """
    Generates a random ASCII art grid.

    Parameters:
    - width (int): The width of the ASCII art.
    - height (int): The height of the ASCII art.
    - characters (str): A string of characters to use in the art. If None, defaults to a set of common ASCII characters.

    Returns:
    - str: A string representation of the ASCII art.
    """
    if characters is None:
        characters = "@#%&*+=-:. "  # Default character set for the art

    art = []
    for _ in range(height):
        line = ''.join(random.choice(characters) for _ in range(width))
        art.append(line)

    return '\n'.join(art)

# Example usage
if __name__ == "__main__":
    width = 40  # Width of the ASCII art
    height = 20  # Height of the ASCII art
    art = generate_ascii_art(width, height)
    print(art)