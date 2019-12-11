import pygame

class Car():
    def __init__(self, x, y, width, height, color,vel,pos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x,self.y,self.width,self.height)
        self.rectT  = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = vel
        self.pos = pos

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        if(self.pos == 1):
            if (self.x - self.vel)<=-20:
                self.x = 800
            self.x -= self.vel
        if(self.pos == 2):
            if (self.x - self.vel)>= 800:
                self.x = 0
            self.x += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.rectT  = pygame.Rect(self.x, self.y, self.width, self.height)