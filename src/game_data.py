"""Contains the data of the game."""

from ball_projectile import BallProjectile
from square_projectile import SquareProjectile
from triangle_projectile import TriangleProjectile
from color import Color

SCREEN_SIZE = (800, 600)
FRAME_RATE = 20
PROJECTILES = [BallProjectile, SquareProjectile, TriangleProjectile]
PROJECTILE_COLORS = [Color.RED, Color.GREEN, Color.BLUE]
MANAGER = None
