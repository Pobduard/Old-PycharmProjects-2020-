import pygame
import math
import random
from pygame import mixer

# Initialize the pygame
pygame.init()
# Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.jpg")
# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)
# Bullet
bullet = pygame.image.load("bullet.png")
# Title and Icon
pygame.display.set_caption("Space Fuckers")
icon = pygame.image.load("puppy.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
# Ready  = You can't see the bullet on the screen
# Fire = The Bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

failure = True
running = True


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def IsCollision(enemyX, enemyY, bulletX, bulletY):
    # distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
    if distance < 27:
        return True
    else:
        return False


def game_Failure():
    Is_Failure: input(int("1 = Retry \n 2 = Give up : \n"))
    print(Is_Failure)
    if Is_Failure == 1:
        game()


def game():
    score_value = 0
    while running is True and failure is True:
        #   RGB =    Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If keystroke is pressed check whether is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        #   Boundaries - Player

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                failure = False
                game_Failure()
                # ##########################break
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = IsCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)
            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= -32:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()
