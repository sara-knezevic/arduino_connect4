import pygame
import numpy as np

pygame.init()

width = 510
height = 510

field_size = 100
circle_size = 40

screen = pygame.display.set_mode((width, height))
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    board = np.array([['_', '_', '_', ' ☀', '_'], ['_', ' ❄️', '_', '_', '_'], ['_', ' ❄️', '_', ' ☀', '_'], ['_', '_', '_', '_', '_'], [' ❄️', '_', '_', '_', '_']])

    # draws grid
    for h in range(int(height/5)):
        for w in range(int(width/5)):
            rect = pygame.Rect(w * (field_size + 2), h * (field_size + 2), field_size, field_size)

            pygame.draw.rect(screen, (255, 255, 255), rect)

    # draws player
    player_i, player_j = np.where(board == ' ❄️')

    for p in range(0, len(player_i)):
        player_circle = pygame.draw.circle(screen, (235, 55, 10), [player_j[p] * 102 + 51, player_i[p] * 102 + 51], circle_size)

    # draws algorithm
    algorithm_i, algorithm_j = np.where(board == ' ☀')

    for a in range(0, len(algorithm_i)):
        algorithm_circle = pygame.draw.circle(screen, (52, 55, 10), [algorithm_j[a] * 102 + 51, algorithm_i[a] * 102 + 51], circle_size)

    pygame.display.flip()

pygame.quit()
