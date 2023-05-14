"""Contains the data of the game."""

from src.ball_projectile import BallProjectile
from src.square_projectile import SquareProjectile
from src.triangle_projectile import TriangleProjectile
from src.color import Color

SCREEN_SIZE = (800, 600)
FRAME_RATE = 20
PROJECTILES = [BallProjectile, SquareProjectile, TriangleProjectile]
PROJECTILE_COLORS = [Color.RED, Color.GREEN, Color.BLUE]
