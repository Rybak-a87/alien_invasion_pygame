class Settings:
    """ клас для хранения всех настроек игры """

    def __init__(self):
        """ инициализирует настройки игры """
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_color = (230, 230, 230)

        # настройки карабля
        self.ship_speed = 5

        # параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)