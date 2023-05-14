from target import Target
from random import randint

class TankAI(Target):
  def __init__(self, coord=None, color=None, rad=30):
    super().__init__(coord, color, rad)
    self.vy = randint(-2, +2)
