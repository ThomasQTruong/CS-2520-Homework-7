"""The cannon game.

Manages it's renderring, movement and striking.
"""

import numpy as np
import pygame as pg
import manager as Manager
from ball_projectile import BallProjectile
from square_projectile import SquareProjectile
from triangle_projectile import TriangleProjectile
from gameobject import GameObject
from color import Color

SCREEN_SIZE = (800, 600)
FRAME_RATE = 20

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
      self.coord = [30, SCREEN_SIZE[1]//2]
    self.angle = angle
    self.max_pow = max_pow
    self.min_pow = min_pow
    self.color = color
    self.active = False
    self.pow = min_pow

    # Projectile values.
    self.projectiles = [BallProjectile, SquareProjectile, TriangleProjectile]
    self.projectile_colors = [Color.RED, Color.GREEN, Color.BLUE]
    self.projectile = self.projectiles[0]
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
    ball = self.projectile(list(self.coord), [int(vel * np.cos(angle)),
                                    int(vel * np.sin(angle))])
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
                                % len(self.projectiles))
    # Change to PREVIOUS projectile.
    else:
      self.projectile_option = ((self.projectile_option - 1)
                                % len(self.projectiles))

    # Set projectile.
    self.projectile = self.projectiles[self.projectile_option]
    self.color = self.projectile_colors[self.projectile_option]

  def move_x(self, inc):
    """
    Changes horizonal position of the gun.
    """
    if (self.coord[0] > 30 or inc > 0) and (self.coord[0]
                        < SCREEN_SIZE[0] - 30 or inc < 0):
      self.coord[0] += inc

  def move_y(self, inc):
    """
    Changes vertical position of the gun.
    """
    if (self.coord[1] > 30 or inc > 0) and (self.coord[1]
                        < SCREEN_SIZE[1] - 30 or inc < 0):
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


if __name__ == "__main__":
  # Initialize game engine.
  pg.init()
  pg.font.init()

  screen = pg.display.set_mode(SCREEN_SIZE)
  pg.display.set_caption("The gun of Khiryanov")

  done = False
  clock = pg.time.Clock()

  mgr = Manager.Manager(n_targets=3)

  while not done:
    clock.tick(FRAME_RATE)
    screen.fill(Color.BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

  pg.quit()
