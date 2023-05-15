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

  # If game ended because player died.
  player_quit = False
  if not GameData.MANAGER.player_alive:
    font = pg.font.SysFont("dejavusansmono", 50)
    # Set display to "Game Over!"
    screen.fill(Color.BLACK)
    text = font.render("Game Over!", True, Color.RED)
    text_rectangle = text.get_rect(center = (GameData.SCREEN_SIZE[0] // 2, 
                                   GameData.SCREEN_SIZE[1] // 2))
    screen.blit(text, text_rectangle)
    # Wait till user clicks X.
    while not player_quit:
      clock.tick(GameData.FRAME_RATE)
      events = pg.event.get()
      for event in events:
        if event.type == pg.QUIT:
          player_quit = True
      pg.display.flip()

  pg.quit()
