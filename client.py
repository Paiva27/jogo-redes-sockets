import pygame
from network import Network
from player import Player


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
BackGround = Background('background.png', [0,0])



def redrawWindow(win,player,player2,car1,car2,car3,car4):
    win.fill((255,255,255))
    win.blit(BackGround.image, BackGround.rect)
    
    car1.draw(win)
    car2.draw(win)
    car3.draw(win)
    car4.draw(win)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    
            try:
                if ((p.is_collided_with(n.cars[0]))or(p.is_collided_with(n.cars[1]))or(p.is_collided_with(n.cars[2]))or(p.is_collided_with(n.cars[3]))):
                    print("Você perdeu")
                    run = False
                elif ((p2.is_collided_with(n.cars[0]))or(p.is_collided_with(n.cars[1]))or(p.is_collided_with(n.cars[2]))or(p.is_collided_with(n.cars[3]))):
                    print("Você perdeu")
                    run = False
            except:
                print(":)")

        n.cars[0].move()
        n.cars[1].move()
        n.cars[2].move()
        n.cars[3].move()
        p.move()
        redrawWindow(win, p, p2,n.cars[0],n.cars[1],n.cars[2],n.cars[3])

main()