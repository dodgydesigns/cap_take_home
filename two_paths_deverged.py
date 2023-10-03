"""
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;
 - Frost.
"""

import os
from pathlib import Path


class TwoPathsDiverged:
    """
    Present the separation between common and different routes of a path.

    ---- 1.
    Write a function that accepts two Paths and returns the portion of
    the first Path that is not common with the second, which is to say
    portion of the first path starting from where the two paths diverged.
    p.s. bonus points for thinking of a better name for this function and its
    parameters.

    E.g.
    '/home/daniel/git/ws/py311/test.yaml' AND
    '/home/daniel/git/slippers' RESULTS IN
    'ws/py311/test.yaml'
    """

    def present_path_divergence(self, path1: Path, path2: Path) -> Path:
        """
        1. Find the common route of the two paths.
        2. Subtract the common path from the first path.
        """

        if not path1 or not path2:
            print(
                "\nCOME ON! You have to provide 2 valid paths:\n"
                f"Path1 was {path1} and path2 was {path2}.\nTry again."
            )
            return

        try:
            common_route = os.path.commonpath([path1, path2])
            print(
                f"\nThe common route of paths:\n   {path1} and {path2} is: \
                                              \n   {common_route}"
            )
            difference_between_paths = str(path1).split(str(common_route))[1]
            print(f"Which leaves a difference of:\n   {difference_between_paths}")
        except Exception as e:
            print(f"\nGive me a break! {e}.\nTry again.\n")


if __name__ == "__main__":
    """Application entry point."""

    ptd = TwoPathsDiverged()

    # Normal execution
    ptd.present_path_divergence(
        Path("/home/daniel/git/ws/py311/test.yaml"), Path("/home/daniel/git/slippers")
    )

    # Missing a path
    ptd.present_path_divergence(None, Path("/home/daniel/git/slippers"))

    # Providing an invalid path
    ptd.present_path_divergence(
        Path("this path\\should / not work"), Path("/home/daniel/git/slippers")
    )
