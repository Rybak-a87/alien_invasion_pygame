import pygame


class Ship:
    """ класс для управления караблем """

    def __init__(self, ai_game):
        """ инициализирует корабль и задает его начальную позицию """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загрузка изображения корабля
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # созранение вещественной координвты центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def moving_right(self):
        if self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self._move()

    def moving_left(self):
        if self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self._move()

    def moving_mouse(self, pos):
        self.rect.center = pos

    def _move(self):
        self.rect.x = self.x


    def blitme(self):
        """ рисует корабль в текущей позиции """
        self.screen.blit(self.image, self.rect)
