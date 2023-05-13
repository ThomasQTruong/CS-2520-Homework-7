""" scoretable.py """

import pygame as pg
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
    score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr),
                                                          True, Color.WHITE))
    score_surf.append(self.font.render("Balls used: {}".format(self.b_used),
                                                          True, Color.WHITE))
    score_surf.append(self.font.render("Total: {}".format(self.score()),
                                                       True, Color.RED))
    for i in range(3):
      screen.blit(score_surf[i], [10, 10 + 30 * i])
