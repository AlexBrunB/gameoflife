import random
import pygame


class Board(object):
    def __init__(self, screen, size=150):
        self.screen = screen
        self.size = size
        self.cells = [[Cell(x * 4 + 2, y * 4 + 2) for x in range(0, self.size)] for y in range(0, self.size)]
        
    def display(self):
        for cell_rows in self.cells:
            for cell in cell_rows:
                if cell.state:
                    cell.display(self.screen)
                        
    def get_neighbors(self, x, y):
        count = 0;
        if (y > 0):
            if x > 0 and self.cells[x - 1][y - 1].state:
                count += 1
            if self.cells[x][y - 1].state:
                count += 1
            if x < self.size - 1 and self.cells[x + 1][y - 1].state:
                count += 1
        if x > 0 and self.cells[x - 1][y].state:
            count += 1
        if x < self.size - 1 and self.cells[x + 1][y].state:
            count += 1
        if y < self.size - 1:
            if x > 0 and self.cells[x - 1][y + 1].state:
                count +=1
            if self.cells[x][y + 1].state:
                count += 1
            if x < self.size - 1 and self.cells[x + 1][y + 1].state:
                count += 1
        return count
    
    def update(self):
        next_board = [[Cell(x * 4 + 2, y * 4 + 2, False) for x in range(0, self.size)] for y in range(0, self.size)]
        for x in range(0, self.size):
            for y in range(0, self.size):
                n = self.get_neighbors(x, y)
                if self.cells[x][y].state and (n < 2 or n > 3):
                    next_board[x][y].state = False
                elif not self.cells[x][y].state and n == 3:
                    next_board[x][y].state = True
                else:
                    next_board[x][y].state = self.cells[x][y].state

        self.cells = next_board
        
    def set_cell(self, pos, state):
        print pos
        y = (pos[0] - 2) / 4
        x = (pos[1] - 2) / 4
        print x, y
        self.cells[x][y].state = state
        

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

