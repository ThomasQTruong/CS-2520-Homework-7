"""Manages the many aspects of the game.

Manages events' handling, projectile's motion
and collision, target creation, etc.
"""

import pygame as pg
from random import randint
from tank import Tank
from score_table import ScoreTable
from moving_targets import MovingTargets
from fast_circle_targets import FastCircleTargets
from fast_square_targets import FastSquareTargets
from fast_triangle_targets import FastTriangleTargets
from tank_ai import TankAI
from target import Target

class Manager:
  """
  Class that manages events' handling, projectile's
  motion and collision, target creation, etc.
  """
  def __init__(self, n_targets=1):
    self.player_alive = True
    self.projectiles = []
    self.enemy_projectiles = []
    self.tank = Tank()
    self.targets = []
    self.enemy_tanks = []
    self.score_t = ScoreTable()
    self.n_targets = n_targets
    self.new_mission()
    self.screen = None

  def new_mission(self):
    """
    Adds new targets.
    """
    # Heals player's health by score.
    self.tank.health += max(15, self.score_t.score())
    if self.tank.health > self.tank.max_health:
      self.tank.health = self.tank.max_health

    # Random sizes based on score.
    rand_start = max(1, 30 - 2 * max(0, self.score_t.score()))
    rand_stop = max(1, 30 - max(0, self.score_t.score()))

    # Create targets.
    for _ in range(self.n_targets):
      self.targets.append(MovingTargets(rad =
                                        randint(rand_start, rand_stop)))
      self.targets.append(FastCircleTargets(rad =
                                            randint(rand_start, rand_stop)))
      self.targets.append(FastSquareTargets(rad =
                                            randint(rand_start, rand_stop)))
      self.targets.append(FastTriangleTargets(rad =
                                              randint(rand_start, rand_stop)))
      self.targets.append(Target(rad =
                                 randint(rand_start, rand_stop)))
      self.enemy_tanks.append(TankAI(rad =
                                 randint(rand_start, rand_stop)))
    # Add every enemy to the targets list too.
    for enemy in self.enemy_tanks:
      self.targets.append(enemy)

  def process(self, events, screen):
    """
    Runs all necessary method for each iteration.
    Adds new targets, if previous are destroyed.
    """
    self.screen = screen
    done = self.handle_events(events)

    if pg.mouse.get_focused():
      mouse_pos = pg.mouse.get_pos()
      self.tank.set_angle(mouse_pos)
      for enemy in self.enemy_tanks:
        enemy.set_angle(self.tank.coord)

    self.move()
    self.collide()
    self.draw(self.screen)

    # Map is blank, spawn new targets.
    if (len(self.targets) == 0 and len(self.projectiles) == 0
        and len(self.enemy_projectiles) == 0):
      self.new_mission()

    return done

  def handle_events(self, events):
    """
    Handles events from keyboard, mouse, etc.
    """
    done = False
    for event in events:
      # User clicked the X button.
      if event.type == pg.QUIT or not self.player_alive:
        done = True
      # Key was pressed.
      elif event.type == pg.KEYDOWN:
        # E key was pressed: next projectile.
        if event.key == pg.K_e:
          self.tank.change_projectile(False)
        # Q key was pressed: previous projectile.
        elif event.key == pg.K_q:
          self.tank.change_projectile(True)
      # User clicked.
      elif event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          self.tank.activate()
      # User lifted their click.
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          self.projectiles.append(self.tank.strike())
          self.score_t.b_used += 1
          for enemy in self.enemy_tanks:
            self.enemy_projectiles.append(enemy.strike())

    # If movement keys are held.
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
      self.tank.move_x(-5)
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      self.tank.move_x(5)
    if keys[pg.K_UP] or keys[pg.K_w]:
      self.tank.move_y(-5)
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      self.tank.move_y(5)

    return done

  def draw(self, screen):
    """
    Runs projectiles', tank's, targets' and score table's drawing method.
    """
    for projectile in self.projectiles:
      projectile.draw(screen)
    for projectile in self.enemy_projectiles:
      projectile.draw(screen)
    for target in self.targets:
      target.draw(screen)
    self.tank.draw(screen)
    self.score_t.draw(screen)

  def move(self):
    """
    Runs projectiles' and tank's movement method, removes dead projectiles.
    """
    # User's projectiles.
    dead_projectiles = []
    for i, projectile in enumerate(self.projectiles):
      projectile.move(grav=2)
      if not projectile.is_alive:
        dead_projectiles.append(i)
    for i in reversed(dead_projectiles):
      self.projectiles.pop(i)

    # Enemy projectiles.
    dead_enemy_projectiles = []
    for i, projectile in enumerate(self.enemy_projectiles):
      projectile.move(grav=2)
      if not projectile.is_alive:
        dead_enemy_projectiles.append(i)
    for i in reversed(dead_enemy_projectiles):
      self.enemy_projectiles.pop(i)

    # Make targets move.
    for i, target in enumerate(self.targets):
      target.move()
    self.tank.gain()

  def collide(self):
    """
    Checks whether projectiles bump into targets,
    sets projectiles' alive trigger.
    """
    collisions = []
    targets_c = []
    for i, projectile in enumerate(self.projectiles):
      for j, target in enumerate(self.targets):
        if target.check_collision(projectile):
          collisions.append([i, j])
          targets_c.append(j)
    targets_c.sort()
    for j in reversed(targets_c):
      self.score_t.t_destr += 1
      if len(self.enemy_tanks) > 0 and self.targets[j] in self.enemy_tanks:
        self.enemy_tanks.remove(self.targets[j])
      self.targets.pop(j)

    # Check for player collision with enemy's projectile.
    for projectile in self.enemy_projectiles:
      if self.tank.check_collision(projectile):
        self.tank.health -= 1
        if self.tank.health <= 0:
          self.player_alive = False

    # Drop a bomb if collide with target.
    for target in self.targets:
      if target.check_collision(self.tank):
        target.drop_bomb(self.screen)
        self.tank.health -= 2
        if self.tank.health <= 0:
          self.player_alive = False
