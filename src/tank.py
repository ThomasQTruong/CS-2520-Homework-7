"""The tank.

Manages it's renderring, movement and striking.
"""

import math
import numpy as np
import pygame as pg
import game_data as GameData
from game_object import GameObject
from color import Color

class Tank(GameObject):
  """
  Tank class. Manages it's renderring, movement and striking.
  """
  def __init__(self, coord=None, angle=0,
               max_pow=50, min_pow=10, color=Color.RED):
    """
    Constructor method. Sets coordinate, direction,
    minimum and maximum power and color of the tank.
    """
    self.max_health = 100
    self.health = self.max_health

    self.coord = coord
    if self.coord is None:  # No coord was passed, set default.
      self.coord = [30, GameData.SCREEN_SIZE[1]//2]

    self.rad = 30
    self.angle = angle
    self.max_pow = max_pow
    self.min_pow = min_pow
    self.color = color
    self.active = False
    self.pow = min_pow
    # Projectile values.
    self.projectile_option = 0
    # Tank image.
    self.tank_image = pg.image.load("../assets/Tank.png")
    self.tank_image = pg.transform.scale(self.tank_image,
                                         (self.rad * 2, self.rad))

  def activate(self):
    """
    Activates tank's charge.
    """
    self.active = True

  def gain(self, inc=2):
    """
    Increases current tank charge power.
    """
    if self.active and self.pow < self.max_pow:
      self.pow += inc

  def strike(self):
    """
    Creates projectile, according to tank's direction and current charge power.
    """
    vel = self.pow
    angle = self.angle
    projectile = GameData.PROJECTILES[self.projectile_option](list(self.coord),
                    [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
    self.pow = self.min_pow
    self.active = False
    return projectile

  def set_angle(self, target_pos):
    """
    Sets tank's direction to target position.
    """
    self.angle = np.arctan2(target_pos[1] - self.coord[1],
                            target_pos[0] - self.coord[0])

  def change_projectile(self, back):
    """
    Changes the projectile the tank uses.
    """
    # Change to NEXT projectile.
    if not back:
      self.projectile_option = ((self.projectile_option + 1)
                                % len(GameData.PROJECTILES))
    # Change to PREVIOUS projectile.
    else:
      self.projectile_option = ((self.projectile_option - 1)
                                % len(GameData.PROJECTILES))
    # Change tank color.
    self.color = GameData.PROJECTILE_COLORS[self.projectile_option]

  def check_collision(self, ball):
    """
    Checks if the tank got hit by an enemy.
    """
    dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
    min_dist = self.rad + ball.rad
    return dist <= min_dist

  def move_x(self, inc):
    """
    Changes horizonal position of the tank.
    """
    if (self.coord[0] > 30 or inc > 0) and (self.coord[0]
                        < GameData.SCREEN_SIZE[0] - 30 or inc < 0):
      self.coord[0] += inc

  def move_y(self, inc):
    """
    Changes vertical position of the tank.
    """
    if (self.coord[1] > 30 or inc > 0) and (self.coord[1]
                        < GameData.SCREEN_SIZE[1] - 30 or inc < 0):
      self.coord[1] += inc

  def draw(self, screen):
    """
    Draws the tank on the screen.
    """
    # Credit to: https://gamedev.stackexchange.com/questions/132163/
    # how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    mx, my = pg.mouse.get_pos()
    dx, dy = mx - self.coord[0], self.coord[1] - my
    new_angle = math.degrees(math.atan2(dy, dx)) - self.angle

    # Flip the image based on angle.
    new_tank_image = self.tank_image
    if new_angle < -90 or new_angle > 90:
      new_tank_image = pg.transform.flip(new_tank_image, False, True)

    # Rotate tank by calculated angle.
    new_tank_image = pg.transform.rotate(new_tank_image, new_angle)

    # Get the rectangle of the rotated tank.
    new_tank_rectangle = new_tank_image.get_rect(center=self.coord)

    # Draw tank.
    screen.blit(new_tank_image, new_tank_rectangle)

    # Power bar.
    rectangle = pg.Rect(self.pow, 10, self.pow, 10)
    rectangle.center = (self.coord[0], self.coord[1] - 20)
    pg.draw.rect(screen, self.color, rectangle)
