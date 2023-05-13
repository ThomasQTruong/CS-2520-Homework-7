""" cannon.py """

import numpy as np
import pygame as pg
import shell as Shell
import manager as Manager
from gameobject import GameObject
from color import Color

SCREEN_SIZE = (800, 600)

class Cannon(GameObject):
  """
  Cannon class. Manages it's renderring, movement and striking.
  """
  def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0,
               max_pow=50, min_pow=10, color=Color.RED):
    """
    Constructor method. Sets coordinate, direction,
    minimum and maximum power and color of the gun.
    """
    self.coord = coord
    self.angle = angle
    self.max_pow = max_pow
    self.min_pow = min_pow
    self.color = color
    self.active = False
    self.pow = min_pow

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
    ball = Shell.Shell(list(self.coord), [int(vel * np.cos(angle)),
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

  def move(self, inc):
    """
    Changes vertical position of the gun.
    """
    if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < self.SCREEN_SIZE[1]
                                                              - 30 or inc < 0):
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
    clock.tick(15)
    screen.fill(Color.BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

  pg.quit()


