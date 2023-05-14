"""Just like movingtargets, but moves 4x faster and is a square!

Gives movement to the stationary targets.
"""

import pygame as pg
import game_data as GameData
from random import randint
from target import Target

class FastSquareTargets(Target):
  """Just like movingtargets, but moves 4x faster and is a square!
  
  Gives movement to the stationary targets.
  """
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vx = randint(-8, +8)
    self.vy = randint(-8, +8)

  def draw(self, screen):
    """Draw square."""
    # Create square.
    square = pg.Rect(self.rad, self.rad, self.rad, self.rad)
    # Set coordinate.
    square.center = self.coord
    # Draw square.
    pg.draw.rect(screen, self.color, square)

  def move(self):
    # Out of bounds, move opposite x direction.
    if (self.coord[0] < 0) or (self.coord[0] > GameData.SCREEN_SIZE[0]):
      self.vx *= -1
    self.coord[0] += self.vx

    # Out of bounds, move opposite y direction.
    if (self.coord[1] < 0) or (self.coord[1] > GameData.SCREEN_SIZE[1]):
      self.vy *= -1
    self.coord[1] += self.vy
