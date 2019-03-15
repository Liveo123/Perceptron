import pygame
import time
import random
import sys

WIDTH = 480
HEIGHT = 480
NO_OF_POINTS = 500

class Screen:
    """Test class for Perceptron
    """

    def __init__(self):
        print("Initializing...")
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))

    def draw_circle(self, coord, filled):
        print("Drawing circle")
        if filled:
            pygame.draw.circle(self.screen, (255, 255, 255), coord, 6, 6)
        else:
            pygame.draw.circle(self.screen, (255, 255, 255), coord, 6, 1)

    def update(self):
        print("Updating screen...")
        pygame.display.update()


class Point:
    def __init__(self):
        self.screen = Screen()
        self.x = random.randint(0, WIDTH-1)
        self.y = random.randint(0, HEIGHT-1)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self):
        if self.label == 1:
            self.screen.draw_circle((self.x, self.y), True)
        else:
            self.screen.draw_circle((self.x, self.y), False)
        self.screen.update()


if __name__ == "__main__":

    points = [Point() for i in range(NO_OF_POINTS)]
    #for point in points:
    for point in points:
        point.show()

    time.sleep(5)
