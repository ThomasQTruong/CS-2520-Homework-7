"""Shootable targets that move around in the map.

Gives movement to the stationary targets.
"""

from random import randint
from target import Target

class MovingTargets(Target):
  """ Shootable targets that move around in the map.
  
  Gives movement to the stationary targets.
  """
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vx = randint(-2, +2)
    self.vy = randint(-2, +2)

  def move(self):
    self.coord[0] += self.vx
    self.coord[1] += self.vy
