from tkinter.filedialog import test
import pygame
from sys import exit

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)

sky = pygame.image.load('Simple/images/Sky.jpg')
ground = pygame.image.load('Simple/images/Ground.jpg')
text = font.render('My Game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (300, 50))

    pygame.display.update()
    clock.tick(60)