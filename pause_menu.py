from button import Button
from json import load


class PauseMenu:  # класс меню паузы
    def __init__(self, win_size):
        self.size = (200, 50)
        self.pos_x = win_size[0] // 2 - 100
        self.color = (0, 255, 0)
        self.button_continue = Button(*self.size, self.color)
        self.button_settings = Button(*self.size, self.color)
        self.button_exit = Button(*self.size, self.color)
        self.is_pause = True

        self.button_back = Button(*self.size, self.color)
        self.button_setting_mode = Button(*self.size, self.color)

        self.buttons_mode = [Button(*self.size, self.color) for _ in range(3)]
        self.is_settings = False

        with open('data/settings.json', 'r', encoding="utf-8") as f:
            self.game_mode = load(f)['game_mode']

    def render(self):  # рендер кнопок
        if self.is_settings:
            self.setting_buttons()
        else:
            self.pause_buttons()

    def pause_buttons(self):  # тут рисуются основные кнопки 
        self.button_continue.draw(self.pos_x, 250, 'Продолжить')
        if self.button_continue.action:
            self.is_pause = True
            self.button_continue.action = False

        self.button_continue.draw(self.pos_x, 350, 'Настройки')
        if self.button_continue.action:
            self.is_settings = True
            self.button_continue.action = False

        self.button_continue.draw(self.pos_x, 450, 'Выход')
        if self.button_continue.action:
            pass

    def setting_buttons(self): # тут рисуются кнопки ностроек
        self.button_back.draw(50, 100, 'Назад')
        if self.button_back.action:
            self.is_settings = False
            self.button_back.action = False

        self.button_setting_mode.draw(self.pos_x - 350, 200, 'Сложность')
        if self.button_setting_mode.action:
            for index, button in enumerate(self.buttons_mode):
                button.draw(self.pos_x + (250 * (index - 1)) + 150, 200, f"{index + 1}-я сложность")
                if button.action:
                    self.button_setting_mode.action = False
                    self.game_mode = index + 1
                    button.action = False
