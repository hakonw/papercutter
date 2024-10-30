import re

import keyboard
import time

# Something something non overlapping tokens?
def tokenize(keys: str, allowed: list[str]) -> list:
    if len(set("".join(allowed))) != len("".join(allowed)):
        raise ValueError("Tokens must be unique and non-overlapping")

    pattern = "|".join(re.escape(token) for token in sorted(allowed, key=len, reverse=True))

    # Use re.findall to directly get tokens from the keys string
    tokens = re.findall(pattern, keys)

    if "".join(tokens) != keys:
        raise ValueError(f"Invalid token sequence in '{keys}'")

    return tokens

class SimpleKeyboard:
    @staticmethod
    def press(key: str) -> None:
        time.sleep(10/1000)
        keyboard.press_and_release(key)

    @staticmethod
    def press_numpad(keys: str) -> None:
        allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "enter"]
        tokens = tokenize(keys, allowed)
        for token in tokens:
            SimpleKeyboard.press(f"num {token}")