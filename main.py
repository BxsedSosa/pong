import sys, pygame

pygame.init()

window = width, height = 1280, 720
screen = pygame.display.set_mode(size=window)
clock = pygame.time.Clock()
fps = 0

x = 6
y = 6
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Rect(20, screen.get_height() / 2, 10, 70)
cpu_pos = pygame.Rect(screen.get_width() - 30, screen.get_height() / 2, 10, 70)


def movement(object_position):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        object_position[1] -= 6
    if keys[pygame.K_DOWN]:
        object_position[1] += 6


def check_ball_collision(ball_pos):
    global x, y
    if ball_pos[1] > window[1]:
        y = -6
    if ball_pos[1] < 0:
        y = 6


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit")
            sys.exit()

    circle = pygame.draw.circle(screen, "white", ball_pos, 10)
    player = pygame.draw.rect(screen, "white", player_pos)
    cpu = pygame.draw.rect(screen, "white", cpu_pos)

    ball_pos[0] += x
    ball_pos[1] += y

    check_ball_collision(ball_pos)
    movement(player_pos)

    pygame.display.flip()
    screen.fill("black")
    clock.tick(60)
