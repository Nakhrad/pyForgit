import pygame
import datetime
pygame.init()
dt =datetime.datetime.today()
m = pygame.display.set_mode((400, 200))
pygame.display.set_caption("CLock")
clock = pygame.time.Clock()
hour = dt.hour
min = dt.minute
sec = dt.second

check = True

font = pygame.font.Font('font.ttf',50)
txt = font.render("{}:{}:{}".format(hour, min, sec), True, "Red")
txtrect = txt.get_rect()
sound = pygame.mixer.Sound('clock.mp3')
sound.play()
while check:
    clock.tick(1)
    sec +=1
    m.fill((177, 252, 3)) # kраска
    m.blit(txt, txtrect)  # установкатекста
    txt = font.render("{}:{}:{}".format(hour, min, sec), True, "Red")
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
    pygame.display.update()