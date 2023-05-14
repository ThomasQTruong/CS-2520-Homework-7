"""The cannon game.

Manages it's renderring, movement and striking.
"""

import numpy as np
import pygame as pg
import game_data as GameData
from gameobject import GameObject
from color import Color

class Cannon(GameObject):
  """
  Cannon class. Manages it's renderring, movement and striking.
  """
  def __init__(self, coord=None, angle=0,
               max_pow=50, min_pow=10, color=Color.RED):
    """
    Constructor method. Sets coordinate, direction,
    minimum and maximum power and color of the gun.
    """
    self.coord = coord
    if self.coord is None:  # No coord was passed, set default.
      self.coord = [30, GameData.SCREEN_SIZE[1]//2]
    self.angle = angle
    self.max_pow = max_pow
    self.min_pow = min_pow
    self.color = color
    self.active = False
    self.pow = min_pow
    # Projectile values.
    self.projectile_option = 0

  def activate(self):
    """
    Activates gun's charge.
    """
    self.active = True

  def gain(self, inc=2):
    """
    Increases current gun charge power.
    """
    if self.active and self.pow < self.max_pow:
      self.pow += inc

  def strike(self):
    """
    Creates ball, according to gun's direction and current charge power.
    """
    vel = self.pow
    angle = self.angle
    ball = GameData.PROJECTILES[self.projectile_option](list(self.coord),
                    [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
    self.pow = self.min_pow
    self.active = False
    return ball

  def set_angle(self, target_pos):
    """
    Sets gun's direction to target position.
    """
    self.angle = np.arctan2(target_pos[1] - self.coord[1],
                            target_pos[0] - self.coord[0])

  def change_projectile(self, back):
    """
    Changes the projectile the cannon uses.
    """
    # Change to NEXT projectile.
    if not back:
      self.projectile_option = ((self.projectile_option + 1)
                                % len(GameData.PROJECTILES))
    # Change to PREVIOUS projectile.
    else:
      self.projectile_option = ((self.projectile_option - 1)
                                % len(GameData.PROJECTILES))
    # Change cannon color.
    self.color = GameData.PROJECTILE_COLORS[self.projectile_option]

  def move_x(self, inc):
    """
    Changes horizonal position of the gun.
    """
    if (self.coord[0] > 30 or inc > 0) and (self.coord[0]
                        < GameData.SCREEN_SIZE[0] - 30 or inc < 0):
      self.coord[0] += inc

  def move_y(self, inc):
    """
    Changes vertical position of the gun.
    """
    if (self.coord[1] > 30 or inc > 0) and (self.coord[1]
                        < GameData.SCREEN_SIZE[1] - 30 or inc < 0):
      self.coord[1] += inc

  def draw(self, screen):
    """
    Draws the gun on the screen.
    """
    gun_shape = []
    vec_1 = np.array([int(5 * np.cos(self.angle - np.pi / 2)),
                      int(5 * np.sin(self.angle - np.pi / 2))])
    vec_2 = np.array([int(self.pow * np.cos(self.angle)),
                      int(self.pow * np.sin(self.angle))])
    gun_pos = np.array(self.coord)
    gun_shape.append((gun_pos + vec_1).tolist())
    gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
    gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
    gun_shape.append((gun_pos - vec_1).tolist())
    pg.draw.polygon(screen, self.color, gun_shape)
