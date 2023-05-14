"""Shootable targets that try to put bombs on the player.

Gives movement to the stationary targets.
"""

import src.game_data as GameData
from src.target import Target

class MovingTargets(Target):
  """ Shootable targets that move around in the map.
  
  Gives movement to the stationary targets.
  """
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vx = 2
    self.vy = 2

  def move(self):
    # Out of bounds, move opposite x direction.
    if (self.coord[0] < 0) or (self.coord[0] > GameData.SCREEN_SIZE[0]):
      self.vx *= -1
    self.coord[0] += self.vx

    # Out of bounds, move opposite y direction.
    if (self.coord[1] < 0) or (self.coord[1] > GameData.SCREEN_SIZE[1]):
      self.vy *= -1
    self.coord[1] += self.vy
