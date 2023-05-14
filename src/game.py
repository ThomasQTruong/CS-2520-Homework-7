"""The tank shooting game: The gun of Khiryanov."""

import pygame as pg
import src.manager as Manager
import src.game_data as GameData
from src.color import Color

if __name__ == "__main__":
  # Initialize game engine.
  pg.init()
  pg.font.init()

  screen = pg.display.set_mode(GameData.SCREEN_SIZE)
  pg.display.set_caption("The gun of Khiryanov")

  done = False
  clock = pg.time.Clock()

  mgr = Manager.Manager(n_targets=3)

  while not done:
    clock.tick(GameData.FRAME_RATE)
    screen.fill(Color.BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

  pg.quit()
