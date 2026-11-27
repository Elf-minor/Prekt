import pygame
from stats import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движущийся квадрат')
clock = pygame.time.Clock()

player_rect = pygame.Rect(
    (WIDTH - PLAYER_SIZE) // 2,
    (HEIGHT - PLAYER_SIZE) // 2,
    PLAYER_SIZE,
    PLAYER_SIZE
)

running = True
while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if keys[pygame.K_ESCAPE]:
            running = False
            print('EXIT')

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
    dy = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])

    player_rect.x += dx * PLAYER_SPEED * dt
    player_rect.y += dy * PLAYER_SPEED * dt

    if (player_rect.left < 0 or
        player_rect.x + PLAYER_SIZE > WIDTH or
        player_rect.y < 0 or 
        player_rect.y + PLAYER_SIZE > HEIGHT):
        running = False
        print('Game Over!')

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.display.flip()

pygame.quit()