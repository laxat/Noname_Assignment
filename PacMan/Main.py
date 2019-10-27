
import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from ghosts import Ghost


class GameController:
    """
    This the class that controls our basic game loop, what this method does
    is update what happens in game based on other events, and what just keeps
    game running until we end it
    """

    def __init__(self):
        pygame.init()
        self.nodes = None
        self.pacman = None
        self.ghost = None
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.set_background()
        self.clock = pygame.time.Clock()


    def set_background(self):
        """
        We create a background and set it to the color BLACK that we defined in
        the constants.py file.
        """
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def start_game(self):

        self.nodes = NodeGroup("maze.txt")
        self.pacman = Pacman(self.nodes)
        self.ghost = Ghost(self.nodes)

    def update(self):
        """
        The update method is a method that we call once per frame of the game.
        It's basically our game loop
        """
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.ghost.update(dt, self.pacman)
        self.check_updater()
        self.render()

    def check_updater(self):
        """
        This method checks for certain events.
        Right now it is just checking to see when we exit out of the game.
        :return:
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        """
        The render method is the method we'll use to draw the images to the screen.
        it uses the update method, it is consistently running until the
        window is closed, right now it just keeps drawing what we want on screen
        """

        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        self.ghost.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.start_game()
    while True:
        game.update()
