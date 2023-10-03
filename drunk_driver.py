"""
trigonometry, the branch of mathematics concerned with specific
functions of angles and their application to calculations. There
are six functions of an angle commonly used in trigonometry.
Their names and abbreviations are sine (sin), cosine (cos),
tangent (tan), cotangent (cot), secant (sec), and cosecant (csc).
"""

import math


def determine_location(directions: list[(float, float)]) -> (float, float):
    """
    ---- 2.
    You have a car, with initial location (0.0, 0.0) in cartesian (x, y) coordinates.
    Given a list of moves in the form [(a1, m1), (a2, m2), ...] where
    a is an angle in degrees (from north) and m is a magnitude or distance, write
    a function that accepts this list and returns the final position. For simplicity
    the final position's x and y should be rounded to 1dp.

    Trig required:
    x = sin(angle) * magnitude
    y = cos(angle) * magnitude
    1. Move to point
    2. Add new coordinates to current point
    3. Rinse and repeat
    """
    current_x_y = (0, 0)
    for move in directions:
        # Angles must be in radians
        angle = math.radians(move[0])  # - quadrant_subtractor)
        magnitude = move[1]
        x = math.sin(angle) * magnitude
        y = math.cos(angle) * magnitude

        current_x_y = (current_x_y[0] + x, current_x_y[1] + y)

    return (round(current_x_y[0], 1), round(current_x_y[1], 1))


if __name__ == "__main__":
    """Application entry point."""

    # Random with some edge cases (45, 180, -300)
    directions = [(45, 10), (180, 25), (-300, 15), (135, -20), (45, 10)]
    print(determine_location(directions))
    # (13.0, 10.8)

    # A square. Should end (0, 0)
    directions = [
        (0, 10),
        (90, 10),
        (180, 10),
        (270, 10),
    ]
    print(determine_location(directions))
    # (0.0, -0.0)
