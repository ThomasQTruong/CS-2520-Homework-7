"""The cannon SQUARES!!!

Creates a square shaped projectile, controls
it's movement and implement it's rendering.
"""

import pygame as pg
import game_data as GameData
from gameobject import GameObject
from color import Color

class SquareProjectile(GameObject):
  """
  The square projectile class. Creates a square shaped projectile,
  controls it's movement and implement it's rendering.
  """
  def __init__(self, coord, vel, rad=20, color=None):
    """
    Constructor method. Initializes projectile's parameters and initial values.
    """
    self.coord = coord
    self.vel = vel
    if color is None:
      color = Color.rand_color()
    self.color = color
    # rad = length
    self.rad = rad
    self.is_alive = True

  def check_corners(self, refl_ort=0.8, refl_par=0.9):
    """
    Reflects projectile's velocity when projectile bumps into the
    screen corners. Implements inelastic rebounce.
    """
    for i in range(2):
      if self.coord[i] < self.rad:
        self.coord[i] = self.rad
        self.vel[i] = -int(self.vel[i] * refl_ort)
        self.vel[1-i] = int(self.vel[1-i] * refl_par)
      elif self.coord[i] > GameData.SCREEN_SIZE[i] - self.rad:
        self.coord[i] = GameData.SCREEN_SIZE[i] - self.rad
        self.vel[i] = -int(self.vel[i] * refl_ort)
        self.vel[1-i] = int(self.vel[1-i] * refl_par)

  def move(self, time=1, grav=0):
    """
    Moves the projectile according to it's velocity and time step.
    Changes the projectile's velocity due to gravitational force.
    """
    self.vel[1] += grav
    for i in range(2):
      self.coord[i] += time * self.vel[i]
    self.check_corners()
    if (self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1]
        > GameData.SCREEN_SIZE[1] - 2*self.rad):
      self.is_alive = False

  def draw(self, screen):
    """
    Draws the projectile on appropriate surface.
    """
    # Create square.
    square = pg.Rect(self.rad, self.rad, self.rad, self.rad)
    # Set coordinate.
    square.center = self.coord
    # Draw square.
    pg.draw.rect(screen, self.color, square)
