import pygame
import random

pygame.init()

window_widht=800
window_height=600
window=pygame.display.set_mode((window_widht,window_height))
pygame.display.set_caption("Snake Game")

game_over=False
score=0

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

snake_body=[]

lenght_of_snake=1

x1=window_widht/2

y1=window_height/2


x1_change=0
y1_change=0

foodx=round(random.randrange(0,window_widht-10)/10) * 10.0
foody=round(random.randrange(0,window_height-10)/10) * 10.0

clock=pygame.time.Clock()


# for the contniouse running the game window
while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            elif event.key == pygame.K_RIGHT:    
                x1_change=10
                y1_change=0
            elif event.key==pygame.K_UP:    
                x1_change=0
                y1_change=-10
            elif event.key== pygame.K_DOWN:    
                x1_change=0
                y1_change=10
    x1=x1 + x1_change        
    y1=y1 + y1_change
    window.fill(black)

    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)


    if x1>=window_widht or x1<0 or y1>=window_height or y1<0:
        game_over=True
        

    
    

    if len(snake_body)>lenght_of_snake:
        del snake_body[0]

    if x1==foodx and y1==foody:    
        foodx=round(random.randrange(0,window_widht-10)/10) * 10.0
        foody=round(random.randrange(0,window_height-10)/10) * 10.0
        lenght_of_snake+=1
        score+=1

    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over=True


    font_style = pygame.font.SysFont(None,50)        
    score_text=font_style.render("Score: "+ str(score),True,white)
    window.blit(score_text,(10,10))

# draw the snake
    pygame.draw.rect(window,red,[foodx,foody,10,10])
    # pygame.draw.rect(window,white,[x1,y1,10,10])
    for segment in snake_body:
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
    pygame.display.update()
    # clock.tick(30)
    clock.tick(30)