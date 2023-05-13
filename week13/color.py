""" color.py """

from random import randint

class Color:
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)

  @staticmethod
  def rand_color() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))
