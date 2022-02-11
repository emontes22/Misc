from tkinter.filedialog import test
import pygame
from sys import exit

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)

sky = pygame.image.load('Simple/images/Sky.png').convert_alpha()
ground = pygame.image.load('Simple/images/Ground.png').convert_alpha()
text = font.render('My Game', False, 'Black')

enemy = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
enemy_rect = enemy.get_rect(bottomright = (600, 300))

player = pygame.image.load('Simple/images/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if event.type == pygame.MOUSEMOTION:
        #     event.pos
    
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (300, 50))

    enemy_rect.x -= 3
    if enemy_rect.right <= 0:
        enemy_rect.left = 800
    screen.blit(enemy, enemy_rect)
    screen.blit(player, player_rect)

    # if player_rect.colliderect(enemy_rect):
        # print("collision")
    
    # mouse_pos = pygame.mouse.get_pos()
    # if (player_rect.collidepoint((mouse_pos))):
    #     pygame.mouse.get_pressed()


    pygame.display.update()
    clock.tick(60)