import pygame
import sys
import math
import random
import time

def game_init(w, h):
    pygame.init()
    size = w, h
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Hell")
    return display

def draw_ship(ship, display):
    ship_copy = ship.copy()
    ship_copy_rect = ship_copy.get_rect()
    ship_copy_rect.y = 600
    ship_copy_rect.x = 800
    display.blit(ship_copy, ship_copy_rect)

def draw_boss(boss, display):
    boss_copy = boss.copy()
    boss_copy_rect = boss_copy.get_rect()
    boss_copy_rect.y = 600
    boss_copy_rect.x = 800
    display.blit(boss_copy, boss_copy_rect)

def move_player(keys, ship_rect):
    if keys[pygame.K_a]:
        ship_rect.x -= 10
    if keys[pygame.K_d]:
        ship_rect.x += 10
    if keys[pygame.K_w]:
        ship_rect.y -= 10
    if keys[pygame.K_s]:
        ship_rect.y += 10

display = game_init(800, 600)    

background_img = pygame.image.load("Space.jpg")


while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.blit(background_img, (0,0))
    pygame.display.flip()
    time.sleep(0.015)