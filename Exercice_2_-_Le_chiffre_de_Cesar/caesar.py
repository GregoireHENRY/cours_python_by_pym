#!/usr/bin/env python3
"""
Solution de l'exercice 2 tel que définit dans
[l'énoncé de l'exercice 2](README.md).
"""

import collections
import string
from typing import Dict

MOST_OCCURRENCE_GUESS = "E"


def shift(CONTAINER: str, AMOUNT: int) -> str:
    """Shift container by amount (put back at the start outside shifted elements from the end)."""
    NEW_START = AMOUNT % len(CONTAINER)
    return CONTAINER[NEW_START:] + CONTAINER[:NEW_START]


def do_cipher(PLAIN_TEXT: str, KEY: int) -> str:

    """
    Cipher plain text from caesar encryption key.
    Treat insensitive-case input plain text and output ciphered text upper cased.
    """
    plain_text_upper = PLAIN_TEXT.upper()
    # create intermediate cipher alphabet shifted with key
    CIPHER_ALBAPHET_UPPER = shift(string.ascii_uppercase, -KEY)
    # Translation table that map classic alphabet to cipher alphabet shifted with the key. In the
    # case of characters that are not in plain alphabet, they remain unchanged, such as spaces.
    TRANSLATION_TABLE = plain_text_upper.maketrans(string.ascii_uppercase, CIPHER_ALBAPHET_UPPER)
    # apply translation
    return plain_text_upper.translate(TRANSLATION_TABLE)


def do_decipher(CIPHER_TEXT: str, KEY: int) -> str:
    """
    Decipher encrypted text from caesar encryption key.
    Operations are symmetric to do_cipher, thus we call it with opposed key.
    """
    return do_cipher(CIPHER_TEXT, -KEY)


def exercise_2_1() -> None:
    """PYM git course: exercice 2.1 - Cipher and decipher from a caesar encryption key"""
    PLAIN_TEXT = "Ave Caesar morituri te salutant"
    KEY = 3

    print("************* Exercise  2.1 *************\n\n")
    print("************ Caesar's cypher ************\n\n")
    print("Plain text   :", PLAIN_TEXT)
    print("key          :", KEY)
    print()

    print("Let's cipher now!")
    CIPHER_TEXT = do_cipher(PLAIN_TEXT, KEY)
    print("Cipher text  :", CIPHER_TEXT)
    print()

    print("Let's decipher (will it work?!)")
    DECIPHER_TEXT = do_decipher(CIPHER_TEXT, KEY)
    print("Decipher text:", DECIPHER_TEXT)
    print()

    SUCCESS = PLAIN_TEXT.upper() == DECIPHER_TEXT
    print("Did it worked?", "OK :)" if SUCCESS else "Nope :(")


def get_letter_occurences(CYPHER_TEXT: str) -> Dict[str, int]:
    """Get occurences for each letters, ignoring characters not in the upper cased alphabet."""
    return dict(
        (LETTER, OCCURRENCE)
        for (LETTER, OCCURRENCE) in collections.Counter(CYPHER_TEXT).items()
        if LETTER in string.ascii_uppercase
    )


def crack_key(CYPHER_TEXT: str) -> int:
    """
    The key to decrypt the text is the distance from the unicode code point of the educated guess
    on the most probable most occurred letter of the context and the unicode code point of the most
    occurred letter of the text.
    """
    LETTER_OCCURRENCES = get_letter_occurences(CYPHER_TEXT)
    MOST_OCCURRENCE = max(LETTER_OCCURRENCES, key=lambda k: LETTER_OCCURRENCES[k])
    return ord(MOST_OCCURRENCE_GUESS) - ord(MOST_OCCURRENCE)


def exercise_2_2() -> None:
    """PYM git course: exercice 2.2 - Decrypt from an unknown caesar encryption key"""
    INTERCEPTED_TEXT = (
        "KPIVKM L'MABIQVO : "
        "RMCVM LMUWVMBBM, MTTM I CVM IXXIZMVKM PCUIQVM, UIQA LWBMM "
        "LM LMCF XMBQBMA KWZVMA ACZ TM NZWVB MB LM LMCF IQTMA LMUWVQIYCMA, "
        "BGXM KPICDM-AWCZQA, LIVA TM LWA. UITOZM AMA IQTMA, MTTM VM AIQB YCM "
        "XTIVMZ. LCZIVB TMCZA WXMZIBQWVA, MTTM I XWCZ VWU LM KWLM JTIKSJQZL."
    )

    EXPECTED_TEXT = (
        "Chance d'Estaing : "
        "Jeune demonette, elle a une apparence humaine, mais dotee "
        "de deux petites cornes sur le front et de deux ailes demoniaques, "
        "type chauve-souris, dans le dos. Malgre ses ailes, elle ne sait que "
        "planer. Durant leurs operations, elle a pour nom de code Blackbird."
    )

    print("************* Exercise  2.2 *************\n\n")
    print("****** Let's break Caesar's cypher ******\n\n")
    print("Intercepted text    :", INTERCEPTED_TEXT)
    print("Expacted clear text :", EXPECTED_TEXT)
    print("Key                 :", "???")
    print()

    print("Let's break it")
    CRACKED_KEY = crack_key(INTERCEPTED_TEXT)
    print("Cracked key      :", CRACKED_KEY)
    print()

    print("Let's use the cracked key (will it work?!)")
    CRACKED_TEXT = do_decipher(INTERCEPTED_TEXT, CRACKED_KEY)
    print("Cracked text:", CRACKED_TEXT)
    print()

    SUCCESS = EXPECTED_TEXT.upper() == CRACKED_TEXT
    print("Did it worked?", "OK :)" if SUCCESS else "Nope :(")


def main() -> None:
    exercise_2_1()

    print()
    print()

    exercise_2_2()


if __name__ == "__main__":
    main()
