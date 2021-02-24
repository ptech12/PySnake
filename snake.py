import pygame
import time
import random
pygame.init()
#color dictionary
color = {
    'blue':(0,0,255), 
    'red': (255, 0, 0),
    'white': (255, 255, 255),
    'black': (0,0,0),
    'yellow': (255, 255, 102),
    'green': (0, 255, 0)
}
#Resolution
resolution, width, height = (800, 600), 800, 600
# creating window
window = pygame.display.set_mode(resolution)
# display update
pygame.display.update()
# Title Caption
pygame.display.set_caption('Snake Game by Prasanth(a.k.a ptech12)')



snake_block = 10 # size of snake
clock = pygame.time.Clock() # Frame rate of Window
snake_speed = 15

# font style
font  = pygame.font.SysFont('Oxygen-Bold', 25, bold=False, italic=False)
score_font = pygame.font.SysFont('BebasNeue Bold', 35, bold=False)
# display the message
def put_message(msg, color, posX, posY):
    message = font.render(msg, True, color)
    window.blit(message, [posX/2, posY/2])
# putting the snake
def ourSnake(snake_block, snake_list):
    for snake in snake_list:
        pygame.draw.rect(window, color.get('black'), [snake[0], snake[1], snake_block, snake_block])   

# displaying the score
def yourScore(score, col = 'yellow'):
    val = score_font.render("Score: " + str(score), True, color.get(col))
    window.blit(val, [0, 0])

def start_game():
    # for Game play
    isGameOver=False
    isGameClose= False

    x, y = resolution[0]/2, resolution[1]/2 # placeing snake in center 
    dx, dy = 0, 0 # snake position changes
    # making snake bigger
    snake_list = []
    Length_of_snake = 1

    # food position
    foodX = round(random.randrange(0, width - snake_block) / 10) * 10.0
    foodY = round(random.randrange(0, height - snake_block)/10) * 10.0


    # Start the GAME
    while not isGameOver:
        # for game is close
        while isGameClose == True:
            window.fill(color.get('white'))
            put_message("You Lost!", color.get('red'), width, height)
            put_message("Press C -> Play Again", color.get('red'), width+100, height+100)
            put_message("Q -> Quit the Game", color.get('red'), width+200, height+200)
            yourScore(Length_of_snake - 1, 'red')
            pygame.display.update()
            for event in pygame.event.get():
                # Key Down event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        isGameOver = True
                        isGameClose = False
                    elif event.key == pygame.K_c:
                        start_game()

        # pygame window event
        for e in pygame.event.get():
            # exit event 
            if e.type == pygame.QUIT:
                isGameOver = True
            # key press event
            if e.type == pygame.KEYDOWN:
                # key 'a'
                if e.key == 97:
                    dx, dy = -snake_block, 0
                # key 'd'
                elif e.key == 100:
                    dx, dy = snake_block, 0
                # key 'w'
                elif e.key == 119:
                    dx, dy = 0, -snake_block
                # key 's'
                elif e.key == 115:
                    dx, dy = 0, snake_block
            # print(e)
        # setting the boundries
        if x >= width or x < 0 or y >= height or y < 0:
            isGameClose = True
        # adding the difference to actual position
        x += dx
        y += dy
        window.fill(color['blue'])  # window color           
        pygame.draw.rect(window, color.get('green'), [foodX, foodY, snake_block, snake_block]) # createing food block
        
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
 
        for snake in snake_list[:-1]:
            if snake == snake_Head:
                game_close = True
        # putting our snake
        ourSnake(snake_block, snake_list)
        # displaying the score board
        yourScore(Length_of_snake-1)
        pygame.display.update() # window update
        # if snake buddy found and bites the food
        if x >= foodX  and y == foodY:
            # picking new food location
            foodX = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foodY = round(random.randrange(0, height - snake_block)/10.0) * 10.0
            # increasing size of tail
            Length_of_snake += 1
        pygame.display.update()
        
        clock.tick(snake_speed) # frame rate

    # # display game over message
    # window.fill(color['white'])
    # put_message("Game Over", color['yellow'])

    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit()

start_game()
