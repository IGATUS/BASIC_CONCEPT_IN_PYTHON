import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
#display color
orangecolor=(255,123,6)
blackcolor=(0,0,0)
redcolor=(196,125,9)
greencolor=(0,255,0)
bluecolor=(53,153,213)
#displays windows width and height
display_width=600
display_height=400
dis=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake game')
snake_block=10
snake_speed = 15
snake_list =[]
#defines the snake's structure and position
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orangecolor,[x[0],x[1],snake_block,snake_block])
#main function begins
def snakegame():
    game_over=False
    game_end=False
    #cordinate of the snake
    x1=display_width/2
    y1=display_height/2
    #when the snake moves
    x1_change=0
    y1_change=0
    #defines the length of the snake
    snake_list = []
    length_of_snake = 1
    #the cordinates of the food element
    foodx=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_end==True:
            dis.fill(bluecolor)
            font_style=pygame.font.SysFont('comicsansms',25)
            msg=font_style.render('You lost!wanna play again?press P',True,redcolor)
            dis.blit(msg,[display_width/6,display_height/3])
            #for displaying the score
            score = length_of_snake-1
            score_font=pygame.font.SysFont('comicsansms',35)
            value = score_font.render('Your score: '+str(score),True,greencolor)
            dis.blit(value,[display_width/3,display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        snakegame()
                if event.type==pygame.QUIT:
                    game_over=True #the game window is still open
                    game_end=False #game has been ended
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
        if x1>=display_width or x1 < 0 or y1 >= display_height or y1<0:
            game_end=True
        #updated cordinates with the change in position
        x1+=x1_change
        y1+=y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis,greencolor,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        #when the length of the snake exceeds,delete the snake list which will end the game
        if len(snake_list)>length_of_snake:
            del snake_list[0]
        #when snake hits itself,game ends
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end=True
        snake(snake_block,snake_list)
        pygame.display.update()
        #when the snake hits the food, the length of the snake is incremented by one
        if x1 == foodx and y1==foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foodx = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
#step two: draw the snake
snakegame()