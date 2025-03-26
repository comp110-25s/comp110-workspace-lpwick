"""Wordle emulation with variable number of turns and a word of variable lengths"""

__author__: str = "730621026"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn: int = 1  # Defines starting index of turn count
    max_turns: int = 6  # Defines chosen max number of turns
    win: bool = False  # Sets initial win condition to false

    while turn <= max_turns and not win:
        print(f" === Turn {turn}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        # Defines user guess as string value of length equal to secret
        print(emojified(guess, secret))

        if guess == secret:
            win = True
            print(f"You won in {turn}/{max_turns} turns!")
        else:
            turn += 1

    if not win:  # if max guesses reached, and win condition not met prints statement
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(string_search: str, char_search: str) -> bool:
    """Searches through string for specific character"""
    assert len(char_search) == 1, f"len('{char_search}') is not 1"

    idx: int = 0  # Begins starting index value at 0
    while idx < len(string_search):
        if string_search[idx] == char_search:
            # Determines if string at index value contains character
            return True
        idx += 1  # Adds to index count
    return False


# Constant emojis and color values
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Makes characters appear as emojis; correct char/correct char & pos/incorrect"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    idx: int = 0
    result: str = ""  # Variable equal to the emojified guess

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            # Determines if guess character and position = secret character and position
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            # Determines if secret contains guess character at index value
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
            # Determines if secret does not contain guess character
        idx += 1
    return result


def input_guess(length_expected: int) -> str:
    """Determines if guess is right number of characters"""
    guess: str = input(f"Enter a {length_expected} character word: ")
    # Prompts user with f-string stating expected guess length equal to secret

    while len(guess) != length_expected:
        guess = input(f"That wasn't {length_expected} chars! Try again: ")
        # If guess length and secret length dont match prompts f-string

    return guess  # If guess length matches secret length continues program


if __name__ == "__main__":
    main(secret="codes")
