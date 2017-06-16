#!/usr/bin/env python2


import random
import pygame


class Cell(object):
    def __init__(self, x, y, state=None):
        self.pos = (x, y)
        self.state = state if state is not None else not bool(int(random.random() * 5))

    def die(self):
        self.state = False

    def born(self):
        self.state = True

    def display(self, screen):
        col = (0, 0, 0)
        self.rect = pygame.draw.circle(screen, col, self.pos, 4, 0)

 
def main():
     #This is our main loop
     pygame.init()
     screen = pygame.display.set_mode((800, 800))
     pygame.display.set_caption('The Game of life')
     pygame.mouse.set_visible(1)

     background = pygame.Surface(screen.get_size())
     background = background.convert()
     background.fill((49, 79, 79))

     screen.blit(background, (0, 0))
     pygame.display.flip()

     random.seed()
     clock = pygame.time.Clock()
     board = Board(screen)

     while 1:
         clock.tick(80)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.set_cell(event.pos, True)

         board.update()

         screen.blit(background, (0, 0))
         board.display()
         pygame.display.flip()

if __name__ == '__main__':main()

