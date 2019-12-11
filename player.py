import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x,self.y,self.width,self.height)
        self.rectT  = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 3
        self.pontuation = 0

    def is_collided_with(self, sprite):
        return self.rectT.colliderect(sprite.rectT)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            print(self.x)

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            print(self.x)

        if keys[pygame.K_UP]:
            self.y -= self.vel
            if ((self.y - self.vel) <= 70):
                if (self.pontuation + 1) == 3:
                    print("Você Ganhou")
                self.pontuation += 1
                self.y = 747

            print(self.y)

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            print(self.y)

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.rectT  = pygame.Rect(self.x, self.y, self.width, self.height)