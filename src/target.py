"""Shootable targets that are stationary.

Creates target, manages it's rendering and collision with a ball event.
"""

import pygame as pg
import game_data as GameData
from random import randint
from game_object import GameObject
from color import Color

class Target(GameObject):
  """
  Target class. Creates target, manages it's
  rendering and collision with a ball event.
  """
  def __init__(self, coord=None, color=None, rad=30):
    """
    Constructor method. Sets coordinate,
    color and radius of the target.
    """
    if coord is None:
      coord = [randint(rad, GameData.SCREEN_SIZE[0] - rad),
                randint(rad, GameData.SCREEN_SIZE[1] - rad)]
    self.coord = coord
    self.rad = rad

    if color is None:
      color = Color.rand_color()
    self.color = color

  def check_collision(self, ball):
    """
    Checks whether the ball bumps into target.
    """
    dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
    min_dist = self.rad + ball.rad
    return dist <= min_dist

  def drop_bomb(self, screen):
    """Drops a bomb on its current location."""
    pg.draw.circle(screen, Color.WHITE, self.coord, self.rad*2)

  def draw(self, screen):
    """
    Draws the target on the screen
    """
    pg.draw.circle(screen, self.color, self.coord, self.rad)

  def move(self):
    """
    This type of target can't move at all.
    :return: None
    """
    pass
