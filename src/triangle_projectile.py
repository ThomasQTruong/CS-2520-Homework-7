"""The cannon TRIANGLES!!!

Creates a triangle shaped projectile, controls
it's movement and implement it's rendering.
"""

import pygame as pg
import game_data as GameData
from game_object import GameObject
from color import Color

class TriangleProjectile(GameObject):
  """
  The triangle projectile class. Creates a triangle shaped projectile,
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
    pg.draw.polygon(screen, self.color,
                    # Left point.
                    ((self.coord[0] - self.rad / 2, self.coord[1]),
                    # Height.
                    (self.coord[0], self.coord[1] - self.rad),
                    # Right point.
                    (self.coord[0] + self.rad / 2, self.coord[1])))
