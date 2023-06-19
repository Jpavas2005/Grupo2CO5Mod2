import pygame
import os

# Global Constants
TITLE = "Spaceships Wars Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SOUND_EXPLOSION = os.path.join(IMG_DIR, ("Sounds/explosion.wav"))

SOUND_BULLET= os.path.join(IMG_DIR, ("Sounds/Bullet.wav"))

SOUND_LASER= os.path.join(IMG_DIR, ("Sounds/Laser.wav"))

SOUND_GAMEOVER = os.path.join(IMG_DIR, ("Sounds/Gameover.wav"))

EXPLOSION = os.path.join(IMG_DIR,("Explosion"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

MISILE = pygame.image.load(os.path.join(IMG_DIR, 'other/destroy.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

explosion_anim = []
for i in range(1, 13):
    file = 'Explosion/{}.png'.format(i)
    img = pygame.image.load(os.path.join(IMG_DIR, file))#.convert()
    #img.set_colorkey((0, 0, 0))
    img = pygame.transform.scale(img, (40, 40))
    explosion_anim.append(img)