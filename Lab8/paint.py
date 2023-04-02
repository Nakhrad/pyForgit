import pygame
import random

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the default values
brush_size = 10
brush_color = BLACK
eraser_size = 20

def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)


try :
    while True :
        e = pygame.event.wait()

        if e.type == pygame.QUIT :
            raise StopIteration

        if e.type == pygame.MOUSEBUTTONDOWN :
            # Selecting random Color Code
            color = (random.randrange(256), random.randrange(
                256), random.randrange(256))
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        pygame.display.flip()
        #circlrrectangleect
        if e.type == pygame.KEYDOWN:
            # Handle key down events
            if e.key == pygame.K_r:
                # Draw a rectangle
                rect_pos = pygame.mouse.get_pos()
                rect_width = 50
                rect_height = 50
                pygame.draw.rect(screen, brush_color, (rect_pos, (rect_width, rect_height)))
            elif e.key == pygame.K_c:
                # Draw a circle
                circle_pos = pygame.mouse.get_pos()
                circle_radius = 30
                pygame.draw.circle(screen, brush_color, circle_pos, circle_radius)
            elif e.key == pygame.K_e:
                # Use the eraser
                rect_pos = pygame.mouse.get_pos()
                rect_width = 80
                rect_height = 80
                pygame.draw.rect(screen, "white", (rect_pos, (rect_width, rect_height)))
            elif e.key == pygame.K_s:
                # Select a color
                brush_color = pygame.color.Color("red")
            elif e.key == pygame.K_a:
                # Select a color
                brush_color = pygame.color.Color("green")
            elif e.key == pygame.K_d:
                # Select a color
                brush_color = pygame.color.Color("white")
            elif e.key == pygame.K_f:
                # Select a color
                brush_color = pygame.color.Color("black")

except StopIteration :
    pass

# Quit
pygame.quit()

# r - rectangle
# c - circle
# s - red color
# a - green color
# d - white
# f - black