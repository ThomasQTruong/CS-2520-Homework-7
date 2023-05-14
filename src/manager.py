"""Manages the many aspects of the game.

Manages events' handling, ball's motion
and collision, target creation, etc.
"""

import pygame as pg
from tank import Tank
from random import randint
from scoretable import ScoreTable
from movingtargets import MovingTargets
from target import Target

class Manager:
  """
  Class that manages events' handling, ball's
  motion and collision, target creation, etc.
  """
  def __init__(self, n_targets=1):
    self.balls = []
    self.gun = Tank()
    self.targets = []
    self.score_t = ScoreTable()
    self.n_targets = n_targets
    self.new_mission()

  def new_mission(self):
    """
    Adds new targets.
    """

    # Random sizes based on score.
    rand_start = max(1, 30 - 2 * max(0, self.score_t.score()))
    rand_stop = max(1, 30 - max(0, self.score_t.score()))

    # Create targets.
    for _ in range(self.n_targets):
      self.targets.append(MovingTargets(rad = randint(rand_start, rand_stop)))
      self.targets.append(Target(rad=randint(rand_start, rand_stop)))

  def process(self, events, screen):
    """
    Runs all necessary method for each iteration.
    Adds new targets, if previous are destroyed.
    """
    done = self.handle_events(events)

    if pg.mouse.get_focused():
      mouse_pos = pg.mouse.get_pos()
      self.gun.set_angle(mouse_pos)

    self.move()
    self.collide()
    self.draw(screen)

    if len(self.targets) == 0 and len(self.balls) == 0:
      self.new_mission()

    return done

  def handle_events(self, events):
    """
    Handles events from keyboard, mouse, etc.
    """
    done = False
    for event in events:
      if event.type == pg.QUIT:
        done = True
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_e:
          self.gun.change_projectile(False)
        elif event.key == pg.K_q:
          self.gun.change_projectile(True)
      elif event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          self.gun.activate()
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          self.balls.append(self.gun.strike())
          self.score_t.b_used += 1

    # If movement keys are held.
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
      self.gun.move_x(-5)
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      self.gun.move_x(5)
    if keys[pg.K_UP] or keys[pg.K_w]:
      self.gun.move_y(-5)
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      self.gun.move_y(5)

    return done

  def draw(self, screen):
    """
    Runs balls', gun's, targets' and score table's drawing method.
    """
    for ball in self.balls:
      ball.draw(screen)
    for target in self.targets:
      target.draw(screen)
    self.gun.draw(screen)
    self.score_t.draw(screen)

  def move(self):
    """
    Runs balls' and gun's movement method, removes dead balls.
    """
    dead_balls = []
    for i, ball in enumerate(self.balls):
      ball.move(grav=2)
      if not ball.is_alive:
        dead_balls.append(i)
    for i in reversed(dead_balls):
      self.balls.pop(i)
    for i, target in enumerate(self.targets):
      target.move()
    self.gun.gain()

  def collide(self):
    """
    Checks whether balls bump into targets, sets balls' alive trigger.
    """
    collisions = []
    targets_c = []
    for i, ball in enumerate(self.balls):
      for j, target in enumerate(self.targets):
        if target.check_collision(ball):
          collisions.append([i, j])
          targets_c.append(j)
    targets_c.sort()
    for j in reversed(targets_c):
      self.score_t.t_destr += 1
      self.targets.pop(j)
