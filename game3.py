import pygame
import sys
import math
 
pygame.init()

_ = False
MAP = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,_,_,_,1,1,_,1,1,_,_,_,1,1,_,_,_,_,_,_,1,1,_,1,1,_,_,_,1,1,_,1],
[1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1],
[1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1],
[1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1],
[1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1],
[1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1],
[1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1],
[1,_,_,_,1,1,_,_,_,_,_,_,1,1,_,1,1,_,_,_,1,1,_,1,_,_,_,_,1,1,_,1],
[1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1],
[1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1],
[1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,_,1],
[1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1,1,_,_,_,_,_,_,1,_,_,_,_,1,_,_,1],
[1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,1,_,_,_,_,_,_,_,1,_,_,_,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1],
[1,_,_,_,1,1,_,1,1,_,_,_,1,1,_,_,_,_,_,_,1,1,_,1,1,_,_,_,1,1,_,1],
[1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1],
[1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1],
[1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1],
[1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1],
[1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1],
[1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1],
[1,_,_,_,1,1,_,_,_,_,_,_,1,1,_,1,1,_,_,_,1,1,_,1,_,_,_,_,1,1,_,1],
[1,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1,2,_,_,_,_,_,_,1,1,_,_,_,_,_,_,1],
[1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1],
[1,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,1,1,1,1,1,1,1,1,_,_,_,_,1],
[1,_,_,_,1,_,_,1,_,_,_,_,1,_,_,1,1,_,_,_,_,_,_,1,_,_,_,_,1,_,_,1],
[1,_,_,_,1,_,_,1,1,_,_,_,1,_,_,1,1,_,_,1,_,_,_,_,_,_,_,1,_,_,_,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
 




 
SCREEN_HEIGHT = 600
SCREEN_WIDTH = SCREEN_HEIGHT 
TILE_SIZE_X = SCREEN_WIDTH / len(MAP[0])
TILE_SIZE_Y = SCREEN_WIDTH / len(MAP) 
MAX_DEPTH = 600
FOV = math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
SCALE = SCREEN_WIDTH  / CASTED_RAYS
 
 
player_x = TILE_SIZE_X * 5 
player_y = TILE_SIZE_Y * 5 
player_angle = math.pi
 
 
 
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
pygame.display.set_caption("Raycasting by Network Skeleton")
 
clock = pygame.time.Clock()
 
def draw_map():
    pygame.draw.rect(win,(0,0,0),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)) 
    p0 = 0
    p1 = 0
    for row in MAP:
        for col in row:
            
            if col:
                
                pygame.draw.rect(win,(200,200,200), (p0, p1, TILE_SIZE_X - 1, TILE_SIZE_Y - 1))      
            p0 += TILE_SIZE_X
            #print(p0)
        p1 += TILE_SIZE_Y
        p0 = 0
    pygame.draw.circle(win, (255, 0, 0), (int(player_x),int(player_y)), 8)
    pygame.draw.line(win, (0,255,0),(player_x,player_y),(player_x - math.sin(player_angle) * 50,player_y + math.cos(player_angle) * 50),3)
    pygame.draw.line(win, (0,255,0),(player_x,player_y),(player_x - math.sin(player_angle - HALF_FOV) * 50,player_y + math.cos(player_angle - HALF_FOV) * 50),3)
    pygame.draw.line(win, (0,255,0),(player_x,player_y),(player_x - math.sin(player_angle + HALF_FOV) * 50,player_y + math.cos(player_angle + HALF_FOV) * 50),3)
 
 
def cast_rays():
    start_angle = player_angle - HALF_FOV
    
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y + math.cos(start_angle) * depth
            col = int(target_x / TILE_SIZE_X)
            row = int(target_y / TILE_SIZE_Y)
 
           
            if MAP[row][col]:
                #pygame.draw.rect(win,(0,255,0),(col * TILE_SIZE,
                #                                row * TILE_SIZE,
                #                                TILE_SIZE - 2,
                #                                TILE_SIZE - 2))
                #pygame.draw.line(win, (255,255,0),(player_x,player_y),(target_x,target_y))
                if MAP[row][col] == 2:
                    color1 = 0
                    color2 = 255
                    color3 = 0
                else:
                    
                    color1 = 50 / (1 + depth * depth * 0.0001)
                    color2 = 50 / (1 + depth * depth * 0.0001)
                    color3 = 50 / (1 + depth * depth * 0.0001)
                
                depth *= math.cos(player_angle - start_angle)
                    
                wall_height = 21000 / (depth + 0.0001)
                
                if wall_height > SCREEN_HEIGHT: wall_height == SCREEN_HEIGHT
                
                pygame.draw.rect(win,(color1,color2,color3), (0 + ray * SCALE,SCREEN_HEIGHT/2  - wall_height/2 ,SCALE,wall_height))
                
                break
    
        start_angle += STEP_ANGLE
 
forward = True
 
 
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(0)
          
    col = int(player_x / TILE_SIZE_X)
    row = int(player_y / TILE_SIZE_Y)
    
    
    if MAP[row][col]:
            if forward == True:
                player_x -= -math.sin(player_angle) * 5
                player_y -= math.cos(player_angle) * 5
            else:
                player_x += -math.sin(player_angle) * 5
                player_y += math.cos(player_angle) * 5
 
     
          
    
    
    
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
       
        draw_map()
    else:
        pygame.draw.rect(win,(100,0,0),(0,SCREEN_HEIGHT /2,SCREEN_HEIGHT,SCREEN_HEIGHT))
        pygame.draw.rect(win,(100,100,0),(0,-SCREEN_HEIGHT / 2,SCREEN_HEIGHT,SCREEN_HEIGHT))      
        cast_rays()
        
        if keys[pygame.K_LEFT]: player_angle -= 0.1
        if keys[pygame.K_RIGHT]: player_angle += 0.1
        if keys[pygame.K_UP]:
            forward = True
            player_x += -math.sin(player_angle) * 5
            player_y += math.cos(player_angle) * 5
        if keys[pygame.K_DOWN]:
            forward = False
            player_x -= -math.sin(player_angle) * 5
            player_y -= math.cos(player_angle) * 5
    
    clock.tick(60)    
    
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Monospace Regular', 30)
    textsurface = font.render(fps, False, (255,255,255))
    win.blit(textsurface,(0,0))
    if MAP[row][col] == 2:
        pygame.draw.rect(win, 'black', (0,0,SCREEN_WIDTH, SCREEN_HEIGHT))
        font = pygame.font.SysFont(None, 50)
        text = font.render('Você Venceu!!', True, (255,255,255))
        win.blit(text, [250, 200])
        
    pygame.display.flip()