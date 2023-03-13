import pygame
pygame.init()

m = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PP2pygame")
pygame.display.set_icon(pygame.image.load("mickeyclock.jpg"))

check = True

font = pygame.font.Font('font.ttf',25)
text = font.render('Pp2game',False,'Red')
b = pygame.image.load("mickeyclock.jpg")

sound=pygame.mixer.Sound('clock.mp3')
sound.play()
while check:
    m.blit(b, (0, 0))
    pygame.draw.circle(m, 'Blue', (100, 100), 40)
    m.blit(text, (300, 100))  # установкатекста
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()