"""Contains color related things.

Contains color RGB values and can generate random colors.
"""

from random import randint

class Color:
  """Contains color related things.

  Contains color RGB values and can generate random colors.
  """
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)

  @staticmethod
  def rand_color() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))
