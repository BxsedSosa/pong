import sys, pygame
from time import sleep

from pygame.cursors import ball

pygame.init()

window = width, height = 1280, 720
screen = pygame.display.set_mode(size=window)
clock = pygame.time.Clock()
fps = 0

x = 5
y = 5
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Rect(20, screen.get_height() / 2, 10, 70)
cpu_pos = pygame.Rect(screen.get_width() - 30, screen.get_height() / 2, 10, 70)


def movement(object_position):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        object_position[1] -= 5
    if keys[pygame.K_DOWN]:
        object_position[1] += 5


def check_ball_collision(ball_pos):
    global x, y
    if ball_pos[1] > window[1]:
        y *= -1
    if ball_pos[1] < 0:
        y *= -1


def check_for_winner():
    global x, y, ball_pos

    if ball_pos[0] > window[0]:
        x = -5
        y = 5
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    elif ball_pos[0] < 0:
        x = 5
        y = 5
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def bar_ball_collision(ball_pos, object_position):
    global x
    if ball_pos[0] < object_position[0] and ball_pos[1] in range(
        object_position[1], object_position[1] + object_position[3]
    ):
        x *= -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit")
            sys.exit()

    print(player_pos)

    circle = pygame.draw.circle(screen, "white", ball_pos, 5)
    player = pygame.draw.rect(screen, "white", player_pos)
    cpu = pygame.draw.rect(screen, "white", cpu_pos)

    ball_pos[0] += x
    ball_pos[1] += y

    check_ball_collision(ball_pos)
    movement(player_pos)
    bar_ball_collision(ball_pos, player_pos)
    check_for_winner()

    pygame.display.flip()
    screen.fill("black")
    clock.tick(60)
