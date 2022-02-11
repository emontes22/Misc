from tkinter.filedialog import test
import pygame
from sys import exit

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)

sky = pygame.image.load('Simple/images/Sky.jpg').convert_alpha()
ground = pygame.image.load('Simple/images/Ground.jpg').convert_alpha()
text = font.render('My Game', False, 'Black')
enemy = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
enemy_xpos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (300, 50))
    enemy_xpos -= 3
    if enemy_xpos <= -100:
        enemy_xpos = 800
    screen.blit(enemy, (enemy_xpos, 265))

    pygame.display.update()
    clock.tick(60)