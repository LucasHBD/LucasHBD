import sys
import pygame
from pygame import mixer

def game_init(w, h):
    pygame.init()
    size = w, h
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Hell")
    return display

# Personagem
def draw_player(ship, ship_rect, display):
    ship_copy = ship.copy()
    display.blit(ship_copy, ship_rect)

def draw_boss(boss, boss_rect, display):
    boss_copy = boss.copy()
    display.blit(boss_copy, boss_rect)

# Disparos
def create_shot(x, y):
    shot = {'rect': pygame.Rect(x, y, 10, 10), 'color': (0, 255, 0, 0)}
    shots.append(shot)
    sound1.play()

def update_shots():
    for shot in shots:
        shot['rect'].y -= shot_speed

def draw_shots():
    for shot in shots:
        pygame.draw.rect(display, shot['color'], shot['rect'])
        

def create_boss_shot(x, y):
    bshot = {'rect': pygame.Rect(x, y, 10, 10), 'color': (255, 0, 0, 0)}
    boss_shots.append(bshot)
    sound1.play()

def update_boss_shots():
    for bshot in boss_shots:
        bshot['rect'].y += boss_shot_speed

def draw_boss_shots():
    for bshot in boss_shots:
        pygame.draw.rect(display, bshot['color'], bshot['rect'])
        

# Colisão
def collision_ship(ship_rect, boss_rect):
    if ship_rect.colliderect(boss_rect):
        pygame.quit()
        sys.exit()

def collision_boss(boss_rect, ship_rect):
    if boss_rect.colliderect(ship_rect):
        pygame.quit()
        sys.exit()

def collision_bullet():
    global current_health
    for shot in shots:
        if shot['rect'].colliderect(boss_rect):
            current_health -= 10
            shots.remove(shot)
            sound2.play()

def collision_boss_bullet():
    global current_health2
    for bshot in boss_shots:
        if bshot['rect'].colliderect(ship_rect):
            current_health2 -= 10
            boss_shots.remove(bshot)
            sound2.play()

# Health Bar
def health_bar():
    health_w = (current_health / max_health) * health_bar_w
    health_bar_rect = pygame.Rect(health_bar_x, health_bar_y, health_w, health_bar_h)
    pygame.draw.rect(display, health_bar_color, health_bar_rect)

def health_bar2():
    health_w2 = (current_health2 / max_health2) * health_bar_w2
    health_bar_rect2 = pygame.Rect(health_bar_x2, health_bar_y2, health_w2, health_bar_h2)
    pygame.draw.rect(display, health_bar_color2, health_bar_rect2)

# Movimentação
def move_player(keys, ship_rect):
    if keys[pygame.K_d]:
        ship_rect.x += 5
        if ship_rect.right > 800:
            ship_rect.right = 800
    if keys[pygame.K_a]:
        ship_rect.x -= 5
        if ship_rect.left < 0:
            ship_rect.left = 0
    if keys[pygame.K_w]:
        ship_rect.y -= 5
        if ship_rect.top < 0:
            ship_rect.top = 0
        if ship_rect.top < 300:
            ship_rect.top = 300
    if keys[pygame.K_s]:
        ship_rect.y += 5
        if ship_rect.bottom > 600:
            ship_rect.bottom = 600

def move_boss(keys, boss_rect):
    if keys[pygame.K_RIGHT]:
        boss_rect.x += 5
        if boss_rect.right > 800:
            boss_rect.right = 800
    if keys[pygame.K_LEFT]:
        boss_rect.x -= 5
        if boss_rect.left < 0:
            boss_rect.left = 0
    if keys[pygame.K_UP]:
        boss_rect.y -= 5
        if boss_rect.top < 0:
            boss_rect.top = 0
    if keys[pygame.K_DOWN]:
        boss_rect.y += 5
        if boss_rect.bottom > 600:
            boss_rect.bottom = 600
        if boss_rect.bottom > 300:
            boss_rect.bottom = 300

#Condição
def reset_game():
    global current_health, current_health2, game_state, shots, boss_shots, last_shot_time

    current_health = 100
    current_health2 = 100
    game_state = "Jogando"
    shots = []
    boss_shots = []
    last_shot_time = 0

    # reiniciando as posições das coisas
    ship_rect.y = 545
    ship_rect.x = 400
    boss_rect.y = 5
    boss_rect.x = 400

    mixer.music.unpause()

display = game_init(800, 600)

# Background
background_img = pygame.image.load("Space.jpg")
# Personagens
ship = pygame.image.load("Nave.bmp")
ship.set_colorkey((255, 0, 255))
ship_rect = ship.get_rect()
boss = pygame.transform.flip(pygame.image.load("Boss.bmp"), False, True)
boss.set_colorkey((255, 0, 255))
boss_rect = boss.get_rect()
ship_rect.y = 545
ship_rect.x = 400
boss_rect.y = 5
boss_rect.x = 400
# Barra de Vida
max_health = 100
current_health = 100
health_bar_w = 200
health_bar_h = 10
health_bar_x = 0
health_bar_y = 10
health_bar_color = (0, 255, 0)
max_health2 = 100
current_health2 = 100
health_bar_w2 = 200
health_bar_h2 = 10
health_bar_x2 = 600
health_bar_y2 = 580
health_bar_color2 = (0, 255, 0)
# Disparos
shots = []
shot_speed = 8
boss_shots = []
boss_shot_speed = 8
shot_cooldown = 500
last_shot_time = 0
#Som
sound1 = pygame.mixer.Sound("shoot.mp3")
sound2 = pygame.mixer.Sound("hit.mp3")
sound3 = pygame.mixer.Sound("win.mp3")
aa = mixer.music.load("bg_music.mp3")
mixer.music.play(-1)
#Fonte
font = pygame.font.Font(None, 32)
text_color = (0, 200, 200)

game_state = "Jogando"
run = True
clock = pygame.time.Clock()

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if game_state == "Jogando":
        if keys[pygame.K_f]:
            current_time = pygame.time.get_ticks()
            if current_time - last_shot_time > shot_cooldown:
                create_shot(ship_rect.x, ship_rect.y)
                last_shot_time = current_time
        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            current_time = pygame.time.get_ticks()
            if current_time - last_shot_time > shot_cooldown:
                create_boss_shot(boss_rect.x, boss_rect.y + boss_rect.height)
                last_shot_time = current_time

        move_player(keys, ship_rect)
        move_boss(keys, boss_rect)

        display.blit(background_img, (0, 0))
        draw_player(ship, ship_rect, display)
        draw_boss(boss, boss_rect, display)
        update_shots()
        draw_shots()
        update_boss_shots()
        draw_boss_shots()
        health_bar()
        health_bar2()
        collision_ship(ship_rect, boss_rect)
        collision_boss(boss_rect, ship_rect)
        collision_bullet()
        collision_boss_bullet()
        if current_health == 0:
            game_state = "Vencedor 1"
        elif current_health2 == 0:
            game_state = "Vencedor 2"
    elif game_state == "Vencedor 1":
        display.blit(background_img, (0, 0))
        text_win = font.render("Jogador 1 Venceu! Aperte [R] Para Reiniciar Ou [Q] Para Sair", True, text_color)
        text_win_rect = text_win.get_rect()
        mixer.music.pause()
        if keys[pygame.K_q]:
            break
        if keys[pygame.K_r]:
            reset_game()
        text_win_rect.center = (display.get_width() // 2, display.get_height() // 2)
        display.blit(text_win, text_win_rect)
         
    elif game_state == "Vencedor 2":
        display.blit(background_img, (0, 0))
        text_win2 = font.render("Jogador 2 Venceu! Aperte [R] Para Reiniciar Ou [Q] Para Sair", True, text_color)
        text_win_rect2 = text_win2.get_rect()
        mixer.music.pause()
        if keys[pygame.K_q]:
            break
        if keys[pygame.K_r]:
            reset_game()
        text_win_rect2.center = (display.get_width() // 2, display.get_height() // 2)
        display.blit(text_win2, text_win_rect2)
    
    pygame.display.flip()
    clock.tick(60)
