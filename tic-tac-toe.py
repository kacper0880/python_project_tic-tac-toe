import pygame
pygame.init()

#Setting up screen
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

#defining fonts
font = pygame.font.SysFont("arialblack", 50)

text_colour = WHITE


#images for x and o
X_IMG = pygame.image.load("cross.png")
O_IMG = pygame.image.load("letter-o.png")

#scale the images
X_IMG = pygame.transform.scale(X_IMG, (250, 250))
O_IMG = pygame.transform.scale(O_IMG, (250, 250))

#game variables
##starting turn
turn = 'x'
game_paused = False
#filling background
window.fill((52, 78, 91))

def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    window.blit(img, (x, y))



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
        window.blit(X_IMG, (row * 300 + 20, column * 300 + 20))
        turn = 'o'
        taken_section[row][column] = 1

    else:
        window.blit(O_IMG, (row * 300 + 20, column * 300 + 20))
        taken_section[row][column] = 0
        turn = 'x'
        
    pygame.display.update()

#function to check the winner
def check_winner():
    #check columns
    for column in taken_section:
        if column[0] is not None and column[0] == column[1] == column[2]:
            return column[0]
    
    #check rows
    for row in range(0,3):
        if taken_section[0][row] is not None and taken_section[0][row] == taken_section[1][row] == taken_section[2][row]:
            return taken_section[0][row]
        
    #check diagonals
    if taken_section[0][0] is not None and taken_section[0][0] == taken_section[1][1] == taken_section[2][2]:
        return taken_section[0][0]
    if taken_section[0][2] is not None and taken_section[0][2] == taken_section[1][1] == taken_section[2][0]:
        return taken_section[0][2]

#function to draw the winner screen/text
def draw_winner(winner):
    font = pygame.font.SysFont(None, 100)  # (font_name, size)
    if winner == 1:
        text = font.render("X Wins!", True, (255, 0, 0))  # red
    elif winner == 0:
        text = font.render("O Wins!", True, (0, 0, 255))  # blue
    else:
        text = font.render("Draw!", True, (0, 0, 0))      # black
    
    # Center the text
    text_rect = text.get_rect(center=(HEIGHT/2, WIDTH/2))  # center of the window
    window.blit(text, text_rect)
    pygame.display.update()


#                   column 1            column 2            column 3
taken_section = [ [None, None, None], [None, None, None], [None, None, None] ]

#Keep the screen window open
running = True
while running:
    draw_text("Press SPACE to pause", font, text_colour, 200, 450)
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when you click the x in top right it closes
            running = False       
        if event.type == pygame.KEYDOWN: #checking for key presses
            if event.key == pygame.K_SPACE: #checking if space_bar is pressed
                game_paused = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x_coordinate, y_coordinate) = pygame.mouse.get_pos()
            #finding which section we are in, screen is 900 x 900 so 
            #separating it into "9 quadrants" 
            row = x_coordinate // 300
            column = y_coordinate // 300 
            #making sure the x or o won't overlap when player is placing it
            if taken_section[row][column] is None:
                draw_xo(row, column)
    winner = check_winner()
    if winner != None:
        draw_winner(winner)



pygame.quit()


