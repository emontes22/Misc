from tkinter.filedialog import test
import pygame
from sys import exit

def displayScore():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)
game_active = True
start_time = 0

sky = pygame.image.load('Simple/images/Sky.png').convert_alpha()
ground = pygame.image.load('Simple/images/Ground.png').convert_alpha()

# score = font.render('My Game', False, (64, 64, 64))
# score_rect = score.get_rect(center = (400, 50))

enemy = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
enemy_rect = enemy.get_rect(bottomright = (600, 300))

player = pygame.image.load('Simple/images/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80, 300))
player_grav = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_grav = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_grav = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        #Setting Background with coordinates
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # screen.blit(score, score_rect)
        displayScore()

        enemy_rect.x -= 3
        if enemy_rect.right <= 0:
            enemy_rect.left = 800
        screen.blit(enemy, enemy_rect)

        #Player
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player, player_rect)

        #Collision
        if enemy_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)