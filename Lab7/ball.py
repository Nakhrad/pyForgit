import pygame
pygame.init()

monic = pygame.display.set_mode((600,400))
pygame.display.set_caption("Japan")
x = 100
y = 100
c = True
while c:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            check = False
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and x > 25:
                x = x - 20
            if i.key == pygame.K_RIGHT and x > 570:
                x = x +20
            if i.key == pygame.K_UP and y > 25:
                y = y -20
            if i.key == pygame.K_DOWN and y > 370:
                y = y+20
    monic.fill((255, 255, 255)) # kраска
    circle = pygame.draw.circle(monic, "Red", (x, y), 25)
    monic.blit(monic, circle)
    pygame.display.update()
