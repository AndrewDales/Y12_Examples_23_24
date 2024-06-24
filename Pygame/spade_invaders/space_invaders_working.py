import pygame

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
PLAYER_SPEED = 10


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.9)
        )
        self.speed = PLAYER_SPEED

    def update(self, direction):
        if direction == 1 and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip((self.speed, 0))
        if direction == -1 and (self.rect.left > 0):
            self.rect.move_ip((-1 * self.speed, 0))


class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

        self.player = Player()

        self.running = True

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

        # update player on the basis of pressed keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.player.update(-1)
        if pressed_keys[K_RIGHT]:
            self.player.update(1)

    def _process_game_logic(self):
        self.clock.tick(60)

    def _draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.surf, self.player.rect)
        pygame.display.flip()


if __name__ == "__main__":
    game = SpaceInvaders()
    game.main_loop()
