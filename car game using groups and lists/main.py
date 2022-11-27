import pygame
from random import randint, choice
from sys import exit
from player import Player
from settings import *
from obstacle import Obstacle

# boiler plate shit bruh
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('drive car. avoid rock!')

# main game
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,700)
# screen surfs
title_surf = pygame.image.load('graphics/title.png').convert_alpha()
bg_surf = pygame.image.load('graphics/background.png').convert_alpha()
end_surf = pygame.image.load('graphics/end_screen.png').convert_alpha()
won_surf = pygame.image.load('graphics/won_screen.png').convert_alpha()

# variables
game_state = 0
start_time = 0
test_font = pygame.font.Font('Pixeltype.ttf', 50)
won = False

# functions
def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(topleft = (50,50))
    screen.blit(score_surf,score_rect)
    return current_time

def collision_check():
    if pygame.sprite.spritecollide(player.sprite,obstacles,False):
        bg_music.stop()
        obstacles.empty()
        return True

# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacles = pygame.sprite.Group()
obstacles.add(Obstacle(game_state,player))

# sound
bg_music = pygame.mixer.Sound('music.wav')
bg_music.set_volume(0.07)
grandma_audio = pygame.mixer.Sound('grandma.wav')

# main loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state == 0:
            if event.type == pygame.KEYDOWN:
                bg_music.play()
                game_state = 1
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_state == 1:
            if event.type == obstacle_timer:
                obstacles.add(Obstacle(game_state,player))

        if game_state == 2 and won == False:
            if event.type == pygame.KEYDOWN:
                game_state = 0
                

    
    # game states
    # title screen
    if game_state == 0:
        screen.blit(title_surf,(0,0))

    # main game
    if game_state == 1:
        
        screen.blit(bg_surf,(0,0))
        
        player.update()
        player.draw(screen)
        obstacles.update()
        obstacles.draw(screen)
        
        score = display_score()

        if collision_check(): game_state = 2
        
        if current_time >= 50:
            game_state = 2
            grandma_audio.play()
            won = True
            bg_music.stop()
        
        
    # end screen
    if game_state == 2:
        if won == True:
            screen.blit(won_surf,(0,0))
        else:
            screen.blit(end_surf,(0,0))
            score_message = test_font.render(f'Your score: {score}',False,(0,0,0))
            score_message_rect = score_message.get_rect(topleft = (50,450))
            screen.blit(score_message,score_message_rect)


    
    pygame.display.update()
    clock.tick(60)
