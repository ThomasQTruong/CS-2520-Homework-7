"""Mimics a score table.

Calculate and displays scores.
"""

import pygame as pg
import game_data as GameData
from color import Color

class ScoreTable:
  """
  Score table class.
  """
  def __init__(self, t_destr=0, b_used=0):
    self.t_destr = t_destr
    self.b_used = b_used
    self.font = pg.font.SysFont("dejavusansmono", 25)

  def score(self):
    """
    Score calculation method.
    """
    return self.t_destr - self.b_used

  def draw(self, screen):
    score_surf = []
    score_surf.append(self.font.render(f"Destroyed: {self.t_destr}",
                                       True, Color.WHITE))
    score_surf.append(self.font.render(f"Shots Fired: {self.b_used}",
                                       True, Color.WHITE))
    score_surf.append(self.font.render(f"Total: {self.score()}",
                                       True, Color.RED))
    score_surf.append(self.font.render(
          f"Health: {GameData.MANAGER.tank.health}", True, Color.GREEN))
    for i in range(len(score_surf)):
      screen.blit(score_surf[i], [10, 10 + 30 * i])
