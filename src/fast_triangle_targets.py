"""Just like movingtargets, but moves 4x faster and is triangular!

Gives movement to the stationary targets.
"""

import pygame as pg
import game_data as GameData
from random import randint
from target import Target

class FastTriangleTargets(Target):
  """Just like movingtargets, but moves 4x faster and is triangular!
  
  Gives movement to the stationary targets.
  """
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vx = randint(-8, +8)
    self.vy = randint(-8, +8)

  def draw(self, screen):
    """Draws the triangle."""
    pg.draw.polygon(screen, self.color,
                    # Left point.
                    ((self.coord[0] - self.rad / 2, self.coord[1]),
                    # Height.
                    (self.coord[0], self.coord[1] - self.rad),
                    # Right point.
                    (self.coord[0] + self.rad / 2, self.coord[1])))

  def move(self):
    """Changes the position of the target."""
    # Out of bounds, move opposite x direction.
    if (self.coord[0] < 0) or (self.coord[0] > GameData.SCREEN_SIZE[0]):
      self.vx *= -1
    self.coord[0] += self.vx

    # Out of bounds, move opposite y direction.
    if (self.coord[1] < 0) or (self.coord[1] > GameData.SCREEN_SIZE[1]):
      self.vy *= -1
    self.coord[1] += self.vy
