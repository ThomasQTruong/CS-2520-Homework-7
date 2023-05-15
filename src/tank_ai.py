"""A tank bot that attacks the user."""

import math
import manager as Manager
import game_data as GameData
import pygame as pg
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
    self.tank_image = pg.image.load("../assets/Tank.png")
    self.tank_image = pg.transform.scale(self.tank_image, (rad * 2, rad))

  def move(self):
    pass

  def draw(self, screen):
    """
    Draws the gun on the screen.
    """
    # Credit to: https://gamedev.stackexchange.com/questions/132163/
    # how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d
    mx, my = GameData.MANAGER.tank.coord
    dx, dy = mx - self.coord[0], self.coord[1] - my
    new_angle = math.degrees(math.atan2(dy, dx)) - self.angle
    # Rotate tank by calculated angle.
    new_tank_image = pg.transform.rotate(self.tank_image, new_angle)
    # Get the rectangle of the rotated tank.
    new_tank_rectangle = new_tank_image.get_rect(center=self.coord)
    # Draw tank.
    screen.blit(new_tank_image, new_tank_rectangle)
