import pygame


class Car:
    def __init__(self,screen_width=800, screen_height=600,
                 car_width=30, car_height=30, color=(255, 255, 255)):
        self.x = screen_width//2
        self.y = screen_height//2
        self.width = car_width
        self.height = car_height
        self.color = color

    def draw(self, screen):
        rotated_car = pygame.transform.rotate(pygame.Surface(self.width, self.height))
        rotated_car.fill(self.color)
        screen.blit(rotated_car, (self.x, self.y))