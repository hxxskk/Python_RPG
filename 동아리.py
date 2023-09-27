from tkinter.tix import Balloon
import pygame
import os
import time

Width = 800
Height = 600

color = (135, 206, 235)
# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("RPG 게임")

# 색상
GREEN = (0, 255, 0)
RED = (255, 0, 0)
black = (0, 0, 0)

# 플레이어
player_size = 50
player_pos = [Width // 2, Height - player_size * 2]
player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

game = True
gravity = 0.5
jump_height = 200  # 점프 높이 조절
movement_speed = 0.7  # 이동 속도 조절

jump = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = player_rect.x - movement_speed
        player_rect.x = max(x, 0)
    if keys[pygame.K_RIGHT]:
        x = player_rect.x + movement_speed
        player_rect.x = min(x, Width - player_size)
    if keys[pygame.K_SPACE] and player_rect.y == Height - player_size:  # 점프 조건 추가
        player_rect.y -= jump_height
        jump= True
        
    if jump == True:
        time.sleep(0.05)
        jump = False
    # 중력 적용
    if player_rect.y < Height - player_size:
        player_rect.y += gravity
        time.sleep(0.001)

    
    screen.fill(black)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.display.flip()

pygame.quit()