"""
In information theory and computer science, the Levenshtein distance is a
string metric for measuring the difference between two sequences. Informally,
the Levenshtein distance between two words is the minimum number of
single-character edits (i.e. insertions, deletions or substitutions)
required to change one word into the other.
 - https://en.wikipedia.org/wiki/Levenshtein_distance
"""

import operator
import nltk


class WhatDidYouSay:
    """
    Determine which word from a list is closest to the sample provided.

    ---- 2.
    Write a function that accepts a string as the first parameter, and a
    list of strings as the second parameter, and returns a string from the
    list that is "most like" the first string. There are some examples of
    what "most like" is below, but the choice of algorithm is yours.

    E.g.
    'potato' and ['potato', 'pumpkin'] is 'potato'
    'arakeat' and ['zzzzzzzz', 'parakeet'] is 'parakeet'
    """

    def closest_word(self, word: str, possibilities: list[str]):
        """
        Using the The Natural Language Toolkit, two words can be compared to
        see how different they are. If the difference is 0, the words are the
        same. The greater the number, the less similar the words are.
        1. Put each word in a dictionary with its NLTK score.
        2. Grab the lowest scoring word and present it.
        """

        if len(possibilities) == 0:
            print(f"\nCOME ON! I have to be able to compare {word} to something!")
            print("Try again with a list of actual possibilities.")
            return

        leader_board_dict = {}
        for possibility in possibilities:
            leader_board_dict[possibility] = nltk.edit_distance(word, possibility)

        print(
            "\n\nDon't argue (Science & Maths always wins),"
            f" the closest word to {word} from:"
        )
        print(possibilities)
        print("is...drum roll please...")
        print(f"   {min(leader_board_dict.items(), key=operator.itemgetter(1))[0]}")


if __name__ == "__main__":
    """Application entry point."""

    wdys = WhatDidYouSay()

    # Nice easy one
    wdys.closest_word("potato", ["potato", "pumpkin", "cat"])
    # Don't argue (Science & Maths always wins), the closest word to potato from:
    # ['potato', 'pumpkin', 'cat']
    # is...drum roll please...
    #    potato

    # Bit harder
    wdys.closest_word("potato", ["pot", "potash", "potassium"])
    # Don't argue (Science & Maths always wins), the closest word to potato from:
    # ['pot', 'potash', 'potassium']
    # is...drum roll please...
    #    potash

    # Closest to 'empty'
    wdys.closest_word("", ["pot", "potash", "potassium"])
    # Don't argue (Science & Maths always wins), the closest word to  from:
    # ['pot', 'potash', 'potassium']
    # is...drum roll please...
    #    pot

    # Empty list
    wdys.closest_word("*what*", [])
    # COME ON! I have to be able to compare *what* to something!
    # Try again with a list of actual possibilities.

    # Numbers
    wdys.closest_word("11", ["12345", "332211", "potassium"])
    # Don't argue (Science & Maths always wins), the closest word to 11 from:
    # ['12345', '332211', 'potassium']
    # is...drum roll please...
    #    12345

    # One for luck - and because it's good fun.
    wdys.closest_word("arakeat", ["zzzzzzzz", "parakeet", "potassium"])
    # Don't argue (Science & Maths always wins), the closest word to arakeat from:
    # ['zzzzzzzz', 'parakeet', 'potassium']
    # is...drum roll please...
    #    parakeet
