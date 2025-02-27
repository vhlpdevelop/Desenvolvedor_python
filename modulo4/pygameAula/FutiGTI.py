# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:43:39 2025

@author: Vitão
"""


import pygame

pygame.init()

window = pygame.display.set_mode((1280, 720))
window_title = pygame.display.set_caption('Fute IGTI')

field = pygame.image.load('assets/field.png')
player1 = pygame.image.load('assets/player1.png')
player2 = pygame.image.load('assets/player2.png')
ball = pygame.image.load('assets/ball.png')

ball_x = 635
ball_y = 310
player1_y = 310
player1_moveup=False
player1_movedown=False
player2_y = 310
player2_moveup=False
player2_movedown=False


def move_player():
    global player1_y
    global player2_y
    
    if player1_moveup:
        player1_y -=5
    else:
        player1_y+=0
    
    if player1_movedown:
        player1_y+=5
    else:
        player1_y+=0
    
    if player1_y <=0:
        player1_y=0
    elif player >=575:
        player_y = 575


def move_ball():
    global ball_x 
    global ball_y 
    
    ball_x +=1

def draw():
    window.blit(field, (0,0))
    window.blit(player1, (50,310))
    window.blit(player2, (1150, 310))
    window.blit(ball, (ball_x,ball_y))

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_moveup = True
            if event.key == pygame.K_s:
                player1_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_moveup=False
            if event.key == pygame.K_s:
                player1_movedown = False
    
    draw()
    move_ball()
    pygame.display.update()
