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


def interpolate_speed(time, speed_dict):
    """
    The change in velocity at a time is given by:
    start_time_speed = Speed(node where node's ts>time)
    end_time_speed = Speed(node where node's ts<time)
    differential = end_time_speed - start_time_speed

    So speed at time 'time' is start_time_speed + (time - start_time) * differential
    """


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

      Worked example:
        Node  d       dt    ds        Speed = ds/dt
        0     0,10    10    0         0
        1     10,20   30    14.4      0.47
        2     20,5    15    18.03     1.20
        3     30,30   5     26.93     5.39
    """

    speed_dict = []
    for counter, point_in_time in enumerate(path):
        if counter > 0:
            distance = calculate_distance(point_in_time, path[counter - 1])
            time = point_in_time.ts - path[counter - 1].ts
            speed = distance / time
            speed_dict[counter] = speed
    print(speed_dict)


if __name__ == "__main__":
    """Application entry point."""

    print(calculate_distance(PointInTime(0, 5, 0), PointInTime(5, 5, 0)))
