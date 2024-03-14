import pygame
import random

# Játék ablak mérete
WIDTH = 800
HEIGHT = 600

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Játékosok paraméterei
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 100
PLAYER_SPEED = 5

# Labda paraméterei
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Játék inicializálása
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

# Játékosok
player1 = pygame.Rect(50, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Labda
ball = pygame.Rect(WIDTH/2 - BALL_SIZE/2, HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)

# Labdát kezdetben random irányba indítjuk
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Fő ciklus
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Játékosok mozgatása
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player1.y += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player2.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player2.y += PLAYER_SPEED

    # Labda mozgatása
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ütközések érzékelése
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ha valamelyik játékos eléri a képernyő szélét, újraindítjuk a labdát
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
        ball.x = WIDTH/2 - BALL_SIZE/2
        ball.y = HEIGHT/2 - BALL_SIZE/2

    # Képernyő törlése
    screen.fill(BLACK)

    # Játékosok és labda kirajzolása
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Képernyő frissítése
    pygame.display.flip()

    # FPS korlátozása
    clock.tick(60)

pygame.quit()
