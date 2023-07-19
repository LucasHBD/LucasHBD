import sys
import time

import pygame

pygame.init()

tela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Hell")

background_img = pygame.image.load("Space.jpg")
ship = pygame.image.load("Nave.bmp")
ship.set_colorkey((255,0,255))
ship_rect = ship.get_rect()
ship_rect.y = 200
ship_rect.x = 320

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        ship_rect.x += 5
    if keys[pygame.K_a]:
        ship_rect.x -= 5
    if keys[pygame.K_w]:
        ship_rect.y -= 5
    if keys[pygame.K_s]:
        ship_rect.y +=5
    tela.blit(background_img, (0, 0))
    tela.blit(ship, ship_rect)
    pygame.display.flip()
    time.sleep(0.015)       