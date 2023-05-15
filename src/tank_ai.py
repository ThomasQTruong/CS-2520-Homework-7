"""A tank bot that attacks the user."""

import math
import pygame as pg
import numpy as np
import game_data as GameData
from random import randint
from target import Target

class TankAI(Target):
  """A tank bot that attacks the user."""
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.coord = [GameData.SCREEN_SIZE[0] - 30, GameData.SCREEN_SIZE[1]
                           - randint(30, GameData.SCREEN_SIZE[1] - 30)]
    self.angle = 0
    # Tank image.
    self.tank_image = pg.image.load("../assets/TankAI.png")
    self.tank_image = pg.transform.scale(self.tank_image, (rad * 2, rad))
    # Tank speed and direction.
    self.vx = randint(-4, +4)
    self.vy = randint(-4, +4)

  def move(self):
    # Out of bounds, move opposite x direction.
    if (self.coord[0] < 0) or (self.coord[0] > GameData.SCREEN_SIZE[0]):
      self.vx *= -1
    self.coord[0] += self.vx

    # Out of bounds, move opposite y direction.
    if (self.coord[1] < 0) or (self.coord[1] > GameData.SCREEN_SIZE[1]):
      self.vy *= -1
    self.coord[1] += self.vy

  def strike(self):
    """
    Creates projectile, according to tank's direction and current charge power.
    """
    vel = 50
    angle = self.angle
    projectile = GameData.PROJECTILES[0](list(self.coord),
                    [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
    return projectile

  def set_angle(self, target_pos):
    """
    Sets tank's direction to target position.
    """
    self.angle = np.arctan2(target_pos[1] - self.coord[1],
                            target_pos[0] - self.coord[0])

  def draw(self, screen):
    """
    Draws the gun on the screen.
    """
    # Credit to: https://gamedev.stackexchange.com/questions/132163/
    # how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    mx, my = GameData.MANAGER.tank.coord
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
