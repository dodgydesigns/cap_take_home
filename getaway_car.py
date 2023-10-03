"""
In mathematics, the Pythagorean theorem or Pythagoras' theorem is a fundamental
relation in Euclidean geometry between the three sides of a right triangle. It
states that the area of the square whose side is the hypotenuse (the side opposite
the right angle) is equal to the sum of the areas of the squares on the other two sides.
The theorem can be written as an equation relating the lengths of the sides a, b and
the hypotenuse c, sometimes called the Pythagorean equation.
"""

from dataclasses import dataclass
import datetime
import math


@dataclass
class PointInTime:
    x: float
    y: float
    ts: datetime.datetime


def calculate_distance(point1: PointInTime, point2: PointInTime):
    """Use Pythagoras' theorem to determine the distance between 2 cartesian points."""
    return abs(math.sqrt(pow((point2.x - point1.x), 2) + pow((point2.y - point1.y), 2)))


def interpolate_speed(required_time, speed_dict):
    """
    The change in velocity at a time is given by:
    start_time_speed = Speed(node where node's ts>time)
    end_time_speed = Speed(node where node's ts<time)
    differential = end_time_speed - start_time_speed

    So speed at time 'time' is start_time_speed + (time - start_time) * speed differential
    """
    # Get list of closest values and pick lower and upper nodes
    closest_list = sorted(speed_dict.keys(), key=lambda x: abs(required_time - x))
    left_speed = speed_dict[closest_list[0]]
    right_speed = speed_dict[closest_list[1]]

    # As per above: start_time_speed + (time - start_time) * speed differential
    interpolate_speed = left_speed + (required_time - closest_list[0]) * (
        right_speed - left_speed
    )

    # Round for output
    return "%.2f" % round(interpolate_speed, 2)


def speed_at_time(at_time: float | int, path: list[PointInTime]) -> str:
    """
    ---- 3.
    Pretend there is a vehicle traveling along a path. The path is represented
    by a list of x, y points and a timestamp at that point. The vehicle travels
    in straight lines between those points and passes through each point at
    the corresponding timestamp. Given this list of points and timestamps,
    and a time seconds (relative to the first timestamp), write a function
    that returns the instantaneous speed at that timestamp. For simplicity
    return the speed as a string rounded and zero-padded to 2dp.

    E.g.
      10: location=(0,0)   speed=?
      20: location=(0,10)  speed=0.50

      distance = sqrt(sqr(dx) + sqr(dy)):
                  sqrt(sqr(0)) + sqr(10)) = 10
      time = 20 - 10 = 10
      speed = dd/dt
      So speed at time 20 is 1 (not 0.5 as the question stipulates)
    """
    previous_time = 0
    speed_dict = {}
    for counter, point_in_time in enumerate(path):
        if counter > 0:
            distance = calculate_distance(point_in_time, path[counter - 1])
            time_delta = point_in_time.ts - previous_time
            previous_time = point_in_time.ts
            speed = distance / time_delta
            speed_dict[point_in_time.ts] = speed

    return f"The speed at time {at_time} is {interpolate_speed(at_time, speed_dict)}."


if __name__ == "__main__":
    """Application entry point."""

    # Worked example:
    #   Node  d       t     dt    ds        Speed = ds/dt
    #   0     0,0     0     0     0         0
    #   1     0,10    10    10    10        1
    #   2     10,20   30    20    14.4      0.71
    #   3     20,5    55    25    18.03     0.72
    #   4     30,30   60    5     26.93     5.39
    print(
        "\n",
        speed_at_time(
            35,
            [
                PointInTime(0, 0, 0),
                PointInTime(0, 10, 10),
                PointInTime(10, 20, 30),
                PointInTime(20, 5, 55),
                PointInTime(30, 30, 60),
            ],
        ),
    )
