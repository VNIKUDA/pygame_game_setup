# Імпорт необхідних матеріалів з бібліотек/скриптів
from .game_config import GameConfig # Конфіг гри (для легшої роботи з розмірами вікна по всьому проекту)
from .user_interface import Image, Button # Клас картинки та кнопки
from abc import abstractmethod # декоратор для абстрактного метода
import pygame
pygame.init()

# Конфіг гри
config = GameConfig()

# Клас екрану (абстрактний/батьківський)
class Screen():
    # Конструктор класу. Приймає параметр window(вікно гри)
    def __init__(self, window):
        self.window = window # вікно гри
        self.window_surface = self.window.window_surface # pygame.Surface цього вікна 

        self.screen_changing = False

    # Встановлює себе як поточний екран вікна
    def set_screen(self):
        for button in Button.buttons:
            button.is_hovered = False
        self.screen_changing = True
        
        # Fade out
        fade = pygame.Surface(config.get_window_size(), flags=pygame.SRCALPHA)
        fade.fill((0,0,0))

        self.window.current_screen.draw()
        for alpha in range(0, 50):
            fade.set_alpha(alpha)
            self.window_surface.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(10)

        self.window.current_screen = self

        # fade in
        for alpha in reversed(range(0, 255, 5)):
            self.window.current_screen.update_screen()
            self.window.current_screen.draw()
            
            fade.set_alpha(alpha)

            self.window_surface.blit(fade, (0, 0))
            self.window.update_window()

        self.screen_changing = False

    # Абстрактні методи класу
    # Відмальовка всіх об'єктів екрану
    @abstractmethod
    def draw(self):
        pass

    # Обробник подій об'єктів екрану
    @abstractmethod
    def events(self, event):
        # event - об'єкт типу pygame.event.Event, потрібен для обробки подій
        pass