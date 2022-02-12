from tkinter.filedialog import test
import pygame
from sys import exit

def displayScore():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)
    return current_time

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)
game_active = True
start_time = 0
score = 0

sky = pygame.image.load('Simple/images/Sky.png').convert_alpha()
ground = pygame.image.load('Simple/images/Ground.png').convert_alpha()

# score = font.render('My Game', False, (64, 64, 64))
# score_rect = score.get_rect(center = (400, 50))

enemy = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
enemy_rect = enemy.get_rect(bottomright = (600, 300))

player = pygame.image.load('Simple/images/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80, 300))
player_grav = 0

#Intro
player_stand = pygame.image.load('Simple/images/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_over = font.render('Game Over', False, (111, 196, 169))
game_over_rect = game_over.get_rect(center = (400, 80))

game_message = font.render('Press space to Retry', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

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
        score = displayScore()

        enemy_rect.x -= 4
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
    else: #Game Over
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_over, game_over_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)



    pygame.display.update()
    clock.tick(60)