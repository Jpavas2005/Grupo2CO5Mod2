import os.path
import random
import time
#from game.components.Explosion import Explosion
import pygame.mixer

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, SOUND_EXPLOSION
from game.components.explosion import Explosion

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()
        self.IMAGE_ENEMY = {0: ENEMY_1, 1: ENEMY_2}
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = self.IMAGE_ENEMY[random.randint(0, 1)]
        if enemy_type == ENEMY_1:
            speed_x = 3
            speed_y = 2
        else:
            speed_x = 5
            speed_y = 2
        if len(self.enemies) < 2 :#or time.time() - self.last_enemy_time >= 1:
            enemy = Enemy(self.IMAGE_ENEMY[random.randint(0, 1)], speed_x, speed_y)
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()

    def destroyEnemy(self, bullet, game):
        for enemy in self.enemies:
            if enemy.rect.colliderect(bullet.rect):
                #img_explode = Explosion(enemy.image)
                #img_explode.draw_explosion(game.screen)
                explote = Explosion(enemy.rect.center)
                game.all_sprites.add(explote)
                self.enemies.remove(enemy)
                explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                pygame.mixer.Sound.play(explosion)
                score = game.scoremanager.update_score()
                game.scoremanager.scorelist(score)
                return True

