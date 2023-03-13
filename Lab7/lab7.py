import pygame
pygame.init()

m = pygame.display.set_mode((803, 800))
pygame.display.set_caption("PP2pygame")
pygame.display.set_icon(pygame.image.load("mickeyclock.jpg"))

check = True

font = pygame.font.Font('font.ttf',50)
text = font.render('Clock',True,'Red')
b = pygame.image.load("mickeyclock.jpg")
arr2 = pygame.image.load("arrow2.png")
arr1 = pygame.image.load("arrow.png")
sound = pygame.mixer.Sound('clock.mp3')
sound.play()
while check:
    m.blit(b, (0, 0))#image
    m.blit(arr1, (90, 110))
    m.blit(arr2, (200, 200))
    #m.fill((177, 252, 3)) # kраска
    #pygame.draw.circle(m, (0, 238, 255), (397, 400), 17)#circle
    m.blit(text, (330, 50))  # установкатекста



    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()