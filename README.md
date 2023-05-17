# Homework 7
- By Thomas Truong | Bronco ID: 014426906

# Tasks
1. ✅ Refactor the Codebase.
    - Divided code into separate modules that represent it.
2. ✅ Implement various types of projectiles.
    - Square projectile.
    - Triangle projectile.
3. ✅ Develop several target types with different movement patterns.
    - Fast Circle Targets.
    - Fast Triangle Targets.
    - Fast Square Targets.
4. ✅ Transform the cannon into a moving tank.
    - ```assets/Tank.png```.
5. ✅ Create "bombs" that will be dropped by targets onto the cannon.
    - ```target.py/draw_bomb()```.
6. ✅ Implement multiple cannons that can shoot at each other.
    - TankAIs.

# Required Installations
- Python3
- Pygame
- Numpy

# Usage Guide
- Navigate to ```src\``` folder.
  - Open ```game.py``` with Python.
    - ![image](https://github.com/ThomasQTruong/CS-2520-Homework-7/assets/58405482/ab6698a7-2d80-4107-896c-097f7e49b12c)

# Controls
- [RClick] - Shoot.
    - Hold to charge power.
- [W] / [Up Arrow] - Move up.
- [A] / [Left Arrow] - Move left.
- [S] / [Down Arrow] - Move down.
- [D] / [Right Arrow] - Move right.
- [E] - Next projectile.
- [Q] - Previous projectile.

# How To Play
- Kill enemies by shooting them.
    - Avoid being near enemies since they will drop bombs on you.
    - There are tanks that will shoot at you when you shoot too.
- Increase your score by killing more than shooting.
- A new round will start when there are no targets and projectiles on the map.
    - You will be healed [15 - 60] health every round based on your score.
    - You will die if your health hits 0.
