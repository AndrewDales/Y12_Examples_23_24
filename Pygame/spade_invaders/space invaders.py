import pygame
from itertools import cycle

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

NUM_ALIEN_ROWS = 5
NUM_ALIEN_COLS = 11

HORIZONTAL_UPDATE = 400

PLAYER_SPEED = 10
BULLET_SPEED = 15

SPRITE_DIR = 'Assets/Sprites/'

ALIEN_IMAGES = {alien_type: [f'{SPRITE_DIR}alien_{alien_type}1.png',
                             f'{SPRITE_DIR}alien_{alien_type}2.png',
                             ]
                for alien_type in 'ABC'}

ALIEN_VALUES = {'A': 40, 'B': 30, 'C': 10}
ALIEN_SPEED_UP = 0.85


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, alien_type='A'):
        super().__init__()
        images = [pygame.image.load(image_file) for image_file in ALIEN_IMAGES[alien_type]]
        self.images = cycle([pygame.transform.scale(img, (40, 35)) for img in images])
        self.image = self.change_image()
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        self.value = ALIEN_VALUES[alien_type]

    def update(self, direction, speed, vertical=False):
        if vertical:
            self.rect.move_ip((0, direction * speed))
        else:
            self.rect.move_ip((direction * speed, 0))
            self.image = self.change_image()

    def change_image(self):
        image = next(self.images)
        return image


class AlienBlock(pygame.sprite.Group):
    def __init__(self, rows=2, cols=2):
        super().__init__()
        self.left = SCREEN_WIDTH * 0.15
        self.right = SCREEN_WIDTH * 0.6
        self.bottom = SCREEN_HEIGHT * 0.45
        self.top = SCREEN_HEIGHT * 0.15
        self.direction = 1
        self.horizontal_speed = SCREEN_WIDTH * 0.03
        self.vertical_speed = SCREEN_HEIGHT * 0.05

        self.move_time = 400

        for j in range(rows):
            for i in range(cols):
                x_pos = self.left + i * (self.right - self.left) // (cols - 1)
                y_pos = self.top + j * (self.bottom - self.top) // (rows - 1)
                if j == 0:
                    alien = Alien(x_pos, y_pos, 'A')
                elif 1 <= j <= 3:
                    alien = Alien(x_pos, y_pos, 'B')
                else:
                    alien = Alien(x_pos, y_pos, 'C')

                self.add(alien)

    def update(self):
        if (self.direction == 1 and self.right >= SCREEN_WIDTH * 0.9 or
                self.direction == -1 and self.left <= SCREEN_WIDTH * 0.1):
            # The super().update() command runs .update() on all of the members of the sprite group
            super().update(1, self.vertical_speed, vertical=True)
            self.top += self.vertical_speed
            self.bottom += self.vertical_speed
            self.direction *= -1
            self.move_time = int(self.move_time * ALIEN_SPEED_UP)
        else:
            # The super().update() command runs .update() on all of the members of the sprite group
            super().update(self.direction, self.horizontal_speed)
            self.left += self.direction * self.horizontal_speed
            self.right += self.direction * self.horizontal_speed

    @property
    def lowest_alien(self):
        return max(alien.rect.bottom for alien in self)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the ship image
        self.image = pygame.image.load('Assets/Sprites/spaceship.png')
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.9)
        )
        self.speed = PLAYER_SPEED

    def shoot(self) -> pygame.sprite.Sprite:
        bullet = Bullet(self.rect.center)
        return bullet

    def update(self, direction):
        if direction == 1 and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip((self.speed, 0))
        if direction == -1 and (self.rect.left > 0):
            self.rect.move_ip((-1 * self.speed, 0))



class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((5, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)
        self.speed = BULLET_SPEED

    def update(self, alien_group=None):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 0:
            self.kill()


class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.font = pygame.font.Font("fonts/space_invaders.ttf", 36)

        self.clock = pygame.time.Clock()

        # Gives an event number to the move_side_event
        self.move_side_event = pygame.USEREVENT + 1

        self.alien_block = AlienBlock(NUM_ALIEN_ROWS, NUM_ALIEN_COLS)
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.running = True

        self.game_score = 0
        self.game_over = False

        # Set a timer so that the aliens move sideways after HORIZONTAL_UPDATE milliseconds
        pygame.time.set_timer(self.move_side_event, self.alien_block.move_time, 1)

    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            # Key press events
            if event.type == KEYDOWN:
                # Player shoot bullet
                if event.key == K_SPACE:
                    if len(self.bullets) < 3:
                        bullet = self.player.shoot()
                        self.bullets.add(bullet)

            # Checks if the timer for the move_side_event has elapsed
            if event.type == self.move_side_event:
                self.alien_block.update()
                pygame.time.set_timer(self.move_side_event, self.alien_block.move_time, 1)

        # update player on the basis of pressed keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.player.update(-1)
        if pressed_keys[K_RIGHT]:
            self.player.update(1)

    def _process_game_logic(self):
        self.clock.tick(60)
        if self.bullets:
            self.bullets.update()
            collision_dict = pygame.sprite.groupcollide(self.bullets, self.alien_block, dokilla=True, dokillb=True)
            if collision_dict:
                self.game_score += sum(alien.value for shot_aliens in collision_dict.values()
                                       for alien in shot_aliens)

        if self.alien_block.lowest_alien > SCREEN_HEIGHT * 0.9:
            self.game_over = True

    def _draw(self):
        self.screen.fill((0, 0, 0))

        # Show the score
        score_text = self.font.render(f'Score = {self.game_score}', True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.02))

        if self.game_over:
            game_over_text = self.font.render('Game Over', True, (255, 255, 255))
            self.screen.blit(game_over_text, (SCREEN_WIDTH * 0.5 - game_over_text.get_width() // 2,
                                              SCREEN_HEIGHT * 0.5 - game_over_text.get_height() // 2))
        else:
            for entity in self.alien_block:
                self.screen.blit(entity.image, entity.rect)
            for bullet in self.bullets:
                self.screen.blit(bullet.surf, bullet.rect)
            self.screen.blit(self.player.image, self.player.rect)

        pygame.display.flip()


if __name__ == "__main__":
    game = SpaceInvaders()
    game.main_loop()
