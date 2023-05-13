""" target.py """

import pygame as pg
import cannon as Cannon
from random import randint
from gameobject import GameObject
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
      coord = [randint(rad, Cannon.SCREEN_SIZE[0] - rad),
                randint(rad, Cannon.SCREEN_SIZE[1] - rad)]
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
