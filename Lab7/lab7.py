import pygame
import datetime
pygame.init()

m = pygame.display.set_mode((803, 800))
pygame.display.set_caption("CLock")
pygame.display.set_icon(pygame.image.load("mickeyclock.jpg"))
clock = pygame.time.Clock()

dt = datetime.datetime.today()
def blitRotate(surf, image1, image2, pos1, originPos, angle1, angle2):
    # offset from pivot to center
    image_rect1 = image1.get_rect(topleft=(100, 100))
    offset_center_to_pivot1 = pygame.math.Vector2(pos1) - image_rect1.center
    #2
    image_rect2 = image2.get_rect(topleft=(100, 100))
    offset_center_to_pivot2 = pygame.math.Vector2(pos1) - image_rect2.center

    # roatated offset from pivot to center
    rotated_offset1 = offset_center_to_pivot1.rotate(-angle1)
    #2
    rotated_offset2 = offset_center_to_pivot2.rotate(-angle2)

    # get a rotated image
    rotated_image1 = pygame.transform.rotate(image1, -angle1)
    rotated_image_rect1 = rotated_image1.get_rect(center=(401.5 , 400))
    #2
    rotated_image2 = pygame.transform.rotate(image2, -angle2)
    rotated_image_rect2 = rotated_image2.get_rect(center=(401.5, 400))

    # rotate and blit the image
    surf.blit(rotated_image1, rotated_image_rect1)
    surf.blit(rotated_image2, rotated_image_rect2)


check = True

#font = pygame.font.Font('font.ttf',50)
#text = font.render('Clock',True,'Red')
b = pygame.image.load("mickeyclock.jpg")
arr2 = pygame.image.load("arrow2.png")
arr1 = pygame.image.load("arrow1.png")
sound = pygame.mixer.Sound('clock.mp3')
sound.play()
angle1 = dt.second*6
angle2 = dt.minute*6
w, h = arr1.get_size()
while check:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
    clock.tick(1)
    m.blit(b, (0, 0))#image
    #m.blit(arr1, (90, 110))
    #m.blit(arr2, (200, 200))
    #m.fill((177, 252, 3)) # kраска
    #m.blit(text, (330, 50))  # установкатекста

    pos = (m.get_width() / 2, m.get_height() / 2)
    blitRotate(m, arr1, arr2, pos, (w / 2, h / 2), angle1, angle2)
    angle1 += 6
    angle2 += 0.1/5
    pygame.display.update()