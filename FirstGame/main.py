from turtle import back
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('Simple/images/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Simple/images/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Simple/images/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('Simple/audio/audio_jump.mp3')
        self.jump_sound.set_volume(0.01)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame1 = pygame.image.load('Simple/images/fly/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('Simple/images/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            enemy_frame_1 = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
            enemy_frame_2 = pygame.image.load('Simple/images/enemy/snail2.png').convert_alpha()
            self.frames = [enemy_frame_1, enemy_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def displayScore():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(enemy, obstacle_rect)
            else:
                screen.blit(fly, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player_sprite.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: 
        return True

#Play walking animation or
#Play jump animation
def player_animation():
    global player, player_index

    if player_rect.bottom < 300:
        player = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player = player_walk[int(player_index)]

pygame.init()   #Starts pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')    #Title of game
clock = pygame.time.Clock()
font = pygame.font.Font('Simple/font/DisposableDroidBB.ttf', 50)
game_active = True
start_time = 0
score = 0
background_music = pygame.mixer.Sound('Simple/audio/music.wav')
background_music.play(loops = -1)
background_music.set_volume(0.05)

#Groups
obstacle_group = pygame.sprite.Group()
 
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(Player())

sky = pygame.image.load('Simple/images/Sky.png').convert_alpha()
ground = pygame.image.load('Simple/images/Ground.png').convert_alpha()

# score = font.render('My Game', False, (64, 64, 64))
# score_rect = score.get_rect(center = (400, 50))

#Obstacles
enemy_frame_1 = pygame.image.load('Simple/images/enemy/snail1.png').convert_alpha()
enemy_frame_2 = pygame.image.load('Simple/images/enemy/snail2.png').convert_alpha()
enemy_frames = [enemy_frame_1, enemy_frame_2]
enemy_frame_index = 0
enemy = enemy_frames[enemy_frame_index]

fly_frame1 = pygame.image.load('Simple/images/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('Simple/images/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('Simple/images/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Simple/images/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('Simple/images/player/jump.png').convert_alpha()

player = player_walk[player_index]
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

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

enemy_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'enemy', 'enemy', 'enemy'])))
                # if randint(0, 2):
                #     obstacle_rect_list.append(enemy.get_rect(bottomright = (randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly.get_rect(bottomright = (randint(900, 1100), 210)))
            
            if event.type == enemy_animation_timer:
                if enemy_frame_index == 0:
                    enemy_frame_index = 1
                else:
                    enemy_frame_index = 0
                enemy = enemy_frames[enemy_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly = fly_frames[fly_frame_index]
                

    if game_active:
        #Setting Background with coordinates
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # screen.blit(score, score_rect)
        score = displayScore()

        # enemy_rect.x -= 4
        # if enemy_rect.right <= 0:
        #     enemy_rect.left = 800
        # screen.blit(enemy, enemy_rect)

        #Player
        # player_grav += 1
        # player_rect.y += player_grav
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player, player_rect)
        player_sprite.draw(screen)
        player_sprite.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        

        #Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collisions
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)

    else: #Game Over
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_grav = 0

        score_message = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_over, game_over_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)



    pygame.display.update()
    clock.tick(60)