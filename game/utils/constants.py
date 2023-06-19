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

SOUND_BULLET= os.path.join(IMG_DIR, ("Sounds/player-fighter.mp3"))

SOUND_LASER= os.path.join(IMG_DIR, ("Sounds/blaster.mp3"))

SOUND_HEART = os.path.join(IMG_DIR, ("Sounds/heart_power_up.mp3"))

SOUND_KABOOM = os.path.join(IMG_DIR, ("Sounds/kaboom.mp3"))

SHIELD_SOUND = os.path.join(IMG_DIR,("Sounds/shield.mp3"))

SOUND_GAMEOVER = os.path.join(IMG_DIR, ("Sounds/Gameover.wav"))

SOUND_DESTROY = os.path.join(IMG_DIR, ("Sounds/destroy.wav"))

SOUND_BOSS = os.path.join(IMG_DIR,("Sounds/duelo-boss.mp3"))

SOUND_FONT = os.path.join(IMG_DIR,("Sounds/imperial_march.mp3"))



EXPLOSION = os.path.join(IMG_DIR,("Explosion"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

MISILE = pygame.image.load(os.path.join(IMG_DIR, 'other/destroy.png'))

IMG_ST = pygame.image.load(os.path.join(IMG_DIR, 'other/IMG_START.png'))

IMG_SC = pygame.image.load(os.path.join(IMG_DIR, 'other/IMG_SCORE.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = os.path.join('C:/Users/JUANS_d1hqs9d/Documents/GitHub/Mod2Co5 Juan_pavas/Grupo2CO5Mod2/game/assets/nueva_fuente','8-BIT WONDER.TTF')

explosion_anim = []
for i in range(1, 13):
    file = 'Explosion/{}.png'.format(i)
    img = pygame.image.load(os.path.join(IMG_DIR, file))#.convert()
    img = pygame.transform.scale(img, (40, 40))
    explosion_anim.append(img)