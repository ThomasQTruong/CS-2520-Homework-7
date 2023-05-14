"""Shootable targets that move around in the map.

Gives movement to the stationary targets.
"""

from game_data import GameData
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
    # Out of bounds, move opposite x direction.
    if (self.coord[0] < 0) or (self.coord[0] > GameData.SCREEN_SIZE[0]):
      self.vx *= -1
    self.coord[0] += self.vx

    # Out of bounds, move opposite y direction.
    if (self.coord[1] < 0) or (self.coord[1] > GameData.SCREEN_SIZE[1]):
      self.vy *= -1
    self.coord[1] += self.vy
