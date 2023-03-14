import pygame
pygame.init()

monic = pygame.display.set_mode((100,100))
pygame.display.set_caption("MP3")
sound = pygame.mixer.Sound('clock.mp3')
c = True
e = False
while c:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_UP:
                sound.play()
            if action.key == pygame.K_DOWN:
                sound.stop()
            if action.key == pygame.K_LEFT:
                sound = pygame.mixer.Sound("Some.mp3")
            if action.key == pygame.K_LEFT:
                sound = pygame.mixer.Sound("Some.mp3")
    pygame.display.update()