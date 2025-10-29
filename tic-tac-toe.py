import pygame
pygame.init()

#Setting upm screen
HEIGHT, WIDTH = 900, 900
# (0, 0)      (900, 0)
# +-----------+
# |           |     The screen sizings
# |           |
# |           |
# +-----------+
# (0,900)     (900, 900)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic tac toe")

#RBG Code for colours
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

#images for x and o
X_IMG = pygame.image.load("cross.png")
O_IMG = pygame.image.load("letter-o.png")

#scale the images
X_IMG = pygame.transform.scale(X_IMG, (250, 250))
O_IMG = pygame.transform.scale(O_IMG, (250, 250))

#starting turn
turn = 'x'
#filling background
window.fill(WHITE)

#draw the columns and rows 
def draw_grid():
    # Draw vertical lines
    #pygame.draw.line(surface, colour, start_pos(x,y), end_pos(x,y), width/thickness)
    pygame.draw.line(window, BLACK, (300, 0), (300, 900), 5)
    pygame.draw.line(window, BLACK, (600, 0), (600, 900), 5)

    # Draw horizontal lines
    pygame.draw.line(window, BLACK, (0, 300), (900, 300), 5)
    pygame.draw.line(window, BLACK, (0, 600), (900, 600), 5)

    pygame.display.update()

#draw the X or the Y
def draw_xo(row, column):
    global turn #not to make a new local variable
    if turn == 'x':
        #blit draws an image onto another
        window.blit(X_IMG, (row * 300 + 20, column* 300 + 20))
        turn = 'o'
        taken_section[row][column] = 1

    else:
        window.blit(O_IMG, (row * 300 + 20, column * 300 + 20))
        taken_section[row][column] = 0
        turn = 'x'
        
    pygame.display.update()


def check_winner():
    #check a line
    for number in taken_section:
        print(number)



taken_section = [ [None, None, None], [None, None, None], [None, None, None] ]
#Keep the screen window open
running = True
while running:
    draw_grid()
    print(taken_section)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False       
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x_coordinate, y_coordinate) = pygame.mouse.get_pos()
            #finding which section we are in, screen is 900 x 900 so 
            #separating it into "9 quadrants" 
            row = x_coordinate // 300
            column = y_coordinate // 300 
            #making sure the x or o won't overlap when player is placing it
            if taken_section[row][column] is None:
                draw_xo(row, column)
    check_winner()


pygame.quit()


