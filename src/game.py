"""The tank shooting game: The gun of Khiryanov."""

import pygame as pg
import manager as Manager
import game_data as GameData
from color import Color

if __name__ == "__main__":
  # Initialize game engine.
  pg.init()
  pg.font.init()

  screen = pg.display.set_mode(GameData.SCREEN_SIZE)
  pg.display.set_caption("The gun of Khiryanov")

  done = False
  clock = pg.time.Clock()

  GameData.MANAGER = Manager.Manager(n_targets=3)

  while not done:
    clock.tick(GameData.FRAME_RATE)
    screen.fill(Color.BLACK)

    done = GameData.MANAGER.process(pg.event.get(), screen)

    pg.display.flip()

  pg.quit()
