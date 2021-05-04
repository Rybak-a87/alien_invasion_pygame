import sys    # для заверщения работы программы

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """ класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """ инициализируем игру и создаем игровые ресурсы """
        pygame.init()    # инициализирует настройки pygame, необходимые для нормальной работы
        self.settings = Settings()

        # оконный режим
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))    # прорисовка окна игрым (поверхность - surface)
        # полноэкранный режим
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")    # Заголовок окна

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # для задержки
        self.clock = pygame.time.Clock()

    def _check_events(self):
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # одно нажатие клавиши
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # elif event.type == pygame.MOUSEMOTION:
            #     self._check_move_mouse(event)

    def _check_keydown_events(self, event):
        """ реагирует на нажатие клавиши """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ реагирует на отпускание клавиш """
        pass

    def _check_move_mouse(self):
        if pygame.mouse.get_focused():
        # self.ship.moving_mouse(event.pos[0])
            self.ship.moving_mouse(pygame.mouse.get_pos())
        # pos = pygame.mouse.get_pos()
        # pre = pygame.mouse.get_pressed()
        # print(pre)

    def _check_continuous_move(self):
        """ неприрывное нажатие клавиш """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ship.moving_left()
        elif keys[pygame.K_RIGHT]:
            self.ship.moving_right()

    def _update_screen(self):
        # при каждом прохождении цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # отображение последнего прорисованного экрана
        pygame.display.update()
        # задержка
        self.clock.tick(self.settings.FPS)

    def _fire_bullet(self):
        """ создание нового  снаряда и включение его в группу bullets """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def run_game(self):
        """ запуск основного цикла игры """
        while True:
            self._check_events()    # одно нажатие клавиши
            self._check_continuous_move()    # неприрывное нажатие клавиш
            # self._check_move_mouse()    # движение курсора мышки
            self.bullets.update()
            # удаление снарядов вышедших за край экрана
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()    # при каждом прохождении цикла перерисовывается экран


if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
