import pygame
import time
pygame.init()

#Setting up screen
HEIGHT, WIDTH = 1000, 900
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
RED = (250, 0, 0)

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
winner = None
draw = False
end_condition = False
start = True

# tracks taken cells 
#                   column 1            column 2            column 3
taken_section = [ [None, None, None], [None, None, None], [None, None, None] ]

#tracking wins/losses/draws
x_wins = 0
o_wins = 0
draws = 0

#draw the columns and rows 
def draw_grid():
    # Draw vertical lines
    #pygame.draw.line(surface, colour, start_pos(x,y), end_pos(x,y), width/thickness)
    pygame.draw.line(window, BLACK, (300, 0), (300, 900), 5)
    pygame.draw.line(window, BLACK, (600, 0), (600, 900), 5)

    # Draw horizontal lines
    pygame.draw.line(window, BLACK, (0, 300), (900, 300), 5)
    pygame.draw.line(window, BLACK, (0, 600), (900, 600), 5)

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

#function for telling the user who's turn it is       
def draw_turn():
    global draw

    if winner is None:
        message = turn + "'s Turn"

    # Render the text
    text = font.render(message, True, (255, 255, 255))

    # Define text area (a black bar at the bottom)
    bar_height = 100
    window.fill((0, 0, 0), (0, HEIGHT - bar_height, WIDTH, bar_height))

    # Center the text horizontally and vertically in the bottom bar
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT - bar_height // 2))

    # Draw and update
    window.blit(text, text_rect)
    pygame.display.update()

#resets all the global variables and screen
def reset_game():
    global taken_section, turn, draw, winner, end_condition
    taken_section = [[None, None, None], [None, None, None], [None, None, None]]
    end_condition = False
    turn = 'x'
    draw = False
    winner = None
    window.fill((52, 78, 91)) #without this previous game is shown
    draw_scoreboard()

#function to check the winner
def check_winner():
    global draw, winner
    GRID_SIZE = 900   # playable area (not full window)
    CELL_SIZE = GRID_SIZE // 3

    # check columns (vertical lines)
    for col in range(3):
        if taken_section[col][0] is not None and taken_section[col][0] == taken_section[col][1] == taken_section[col][2]:
            x = (col * CELL_SIZE) + CELL_SIZE // 2 #middle of each cell
            pygame.draw.line(window, RED, (x, 0), (x, GRID_SIZE), 6)
            return taken_section[col][0]

    # check rows (horizontal lines)
    for row in range(3):
        if taken_section[0][row] is not None and taken_section[0][row] == taken_section[1][row] == taken_section[2][row]:
            y = (row * CELL_SIZE) + CELL_SIZE // 2 #middle of each cell
            pygame.draw.line(window, RED, (0, y), (GRID_SIZE, y), 6)
            return taken_section[0][row]

    # check diagonals
    if taken_section[0][0] is not None and taken_section[0][0] == taken_section[1][1] == taken_section[2][2]:
        pygame.draw.line(window, RED, (0, 0), (GRID_SIZE, GRID_SIZE), 6)
        return taken_section[0][0]

    if taken_section[0][2] is not None and taken_section[0][2] == taken_section[1][1] == taken_section[2][0]:
        pygame.draw.line(window, RED, (0, GRID_SIZE), (GRID_SIZE, 0), 6)
        return taken_section[0][2]

   #check draw (if no winner)
    if winner is None and all(all(cell is not None for cell in row) for row in taken_section):
        draw = True
        return None

#function to draw the winner screen/text
def draw_winner(winner):
    global end_condition, x_wins, o_wins, draws
    if winner == 1:
        text = font.render("X Wins!", True, WHITE) 
        x_wins += 1
        end_condition = True
    elif winner == 0:
        text = font.render("O Wins!", True, WHITE)
        o_wins += 1
        end_condition = True
    elif draw == True:
        text = font.render("Draw!", True, WHITE)
        draws += 1
        end_condition = True
    
    # Center the text
    text_rect = text.get_rect(center=(HEIGHT/2, WIDTH/2))  # center of the window
    window.blit(text, text_rect)
    pygame.display.update()

def draw_scoreboard():
    score_text = f"X Wins: {x_wins}    O Wins: {o_wins}    Draws: {draws}"
    text = font.render(score_text, True, WHITE)
    # Draw on bottom black area (like your turn display)
    window.fill((0, 0, 0), (0, 900, WIDTH, 100))
    text_rect = text.get_rect(center=(WIDTH // 2, 950))
    window.blit(text, text_rect)
    pygame.display.update()

#Keep the screen window open
running = True
while running:
    #for initial launch
    if start == True:
         # Display start message
        font_big = pygame.font.SysFont(None, 50)
        text = font_big.render("Start = Y, Q = End, Spacebar = Score", True, WHITE)
        window.fill((0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # restart if y is pressed
                    window.fill((52, 78, 91))
                    draw_grid()
                    start = False           
                elif event.key == pygame.K_q:  # quit if q is pressed
                    running = False
                elif event.key == pygame.K_SPACE:
                    draw_scoreboard()
                    time.sleep(1.5) #showing the scoreboard for 1.5 seconds
    #ending the game
    elif end_condition == True:
        # Display end message
        font_big = pygame.font.SysFont(None, 60)
        text = font_big.render("Play again? (Y = Yes / Q = Quit)", True, WHITE)
        window.fill((0, 0, 0), (0, 900, WIDTH, 100))  # refill the black bar underneath the board
        text_rect = text.get_rect(center=(WIDTH // 2, 950))  # Centered under grid
        window.blit(text, text_rect) #put the text onto the window
        pygame.display.update()

        # Wait for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # restart if y is pressed
                    reset_game()             
                elif event.key == pygame.K_q:  # quit if q is pressed
                    running = False
    #Main loop
    else:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when you click the x in top right it closes
                running = False       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_scoreboard()
                    time.sleep(1.5) #showing the scoreboard for 1.5 seconds
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x_coordinate, y_coordinate) = pygame.mouse.get_pos()
                #finding which section we are in, screen is 900 x 900 so separating it into "9 quadrants" 
                #setting bounds to avoid out of index error
                if x_coordinate < 900 and y_coordinate <900:
                    row = x_coordinate // 300
                    column = y_coordinate // 300 
                #making sure the x or o won't overlap when player is placing it
                    if taken_section[row][column] is None:
                        draw_xo(row, column)
        winner = check_winner()
        if winner != None or draw == True:
            draw_winner(winner)
        else:
            draw_turn()
        pygame.display.update()


pygame.quit()


