""" movingtargets.py """

from random import randint
from target import Target

class MovingTargets(Target):
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vx = randint(-2, +2)
    self.vy = randint(-2, +2)

  def move(self):
    self.coord[0] += self.vx
    self.coord[1] += self.vy
