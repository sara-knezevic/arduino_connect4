import pygame
import numpy as np

pygame.init()

width = 510
height = 510

field_size = 100
circle_size = 70

screen = pygame.display.set_mode((width, height))
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    # draws grid
    for h in range(height):
        for w in range(width):
            rect = pygame.Rect(w * (field_size + 2), h * (field_size + 2), 
                                field_size, field_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)

    # draws players

    pygame.display.flip()

pygame.quit()
