import pygame
import time
import random
pygame.init()

#Setting up screen
WIDTH, HEIGHT = 800, 800

# Define a fixed bar height for the messages for example player's turn
BAR_HEIGHT = 50 

# The grid must be square so max width is the window width.
# Its max height is the window height - the bar's height.
GRID_WIDTH = WIDTH
GRID_PLAY_HEIGHT = HEIGHT - BAR_HEIGHT

# The grid size is the smaller of these two dimensions to keep it square
GRID_SIZE = min(GRID_WIDTH, GRID_PLAY_HEIGHT)

# The size of one cell
CELL_SIZE = GRID_SIZE // 3

# X-offset to center the grid
GRID_OFFSET_X = (WIDTH - GRID_SIZE) // 2
# The grid is always at the top
GRID_OFFSET_Y = 0 

# Displays the game window with set width and height
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic tac toe")

# RBG Code for colours
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)

# Defining font
font = pygame.font.SysFont("arialblack", 40)

# Images for x and o
X_IMG = pygame.image.load("cross.png")
O_IMG = pygame.image.load("letter-o.png")

# Scale the images based off cell_size 
X_IMG = pygame.transform.scale(X_IMG, (CELL_SIZE * 0.8, CELL_SIZE * 0.8))
O_IMG = pygame.transform.scale(O_IMG, (CELL_SIZE * 0.8, CELL_SIZE * 0.8))

# Game variables
turn = 'x'
winner = None
draw = False
end_condition = False
start = True
vs_computer = False
taken_section = [ [None, None, None], [None, None, None], [None, None, None] ]
menu_lines = [   # To make them be written not in a single line
    "Player vs Player = Y",
    "End = Q",
    "Show Scoreboard = Spacebar",
    "Player vs Computer = A"
]
# Tracking wins
x_wins = 0
o_wins = 0
draws = 0

# Draw the columns and rows 
def draw_grid():
    # Draw vertical lines
    # pygame.draw.line(surface, colour, start_pos(x,y), end_pos(x,y), width/thickness)
    # Offset to not get onto the black box at the bottom
    pygame.draw.line(window, BLACK, (GRID_OFFSET_X + CELL_SIZE, 0), (GRID_OFFSET_X + CELL_SIZE, GRID_SIZE), 5)
    pygame.draw.line(window, BLACK, (GRID_OFFSET_X + CELL_SIZE * 2, 0), (GRID_OFFSET_X + CELL_SIZE * 2, GRID_SIZE), 5)

    # Draw horizontal lines
    pygame.draw.line(window, BLACK, (GRID_OFFSET_X, CELL_SIZE), (GRID_OFFSET_X + GRID_SIZE, CELL_SIZE), 5)
    pygame.draw.line(window, BLACK, (GRID_OFFSET_X, CELL_SIZE * 2), (GRID_OFFSET_X + GRID_SIZE, CELL_SIZE * 2), 5)


#draw the X or the Y
def draw_xo(row, column):
    global turn 

    # Calculate x and y coordinates based on cell size and offset
    # Adding a small padding to make the x and o's more in the middle of each cell
    padding = CELL_SIZE * 0.1
    x_pos = (row * CELL_SIZE) + GRID_OFFSET_X + padding
    y_pos = (column * CELL_SIZE) + GRID_OFFSET_Y + padding

    # Draws an 'x' or an 'o' depending on who's turn
    if turn == 'x':
        window.blit(X_IMG, (x_pos, y_pos))
        turn = 'o'
        taken_section[row][column] = 1
    else:
        window.blit(O_IMG, (x_pos, y_pos))
        taken_section[row][column] = 0
        turn = 'x'

#function for telling the user who's turn it is      
def draw_turn():
    global draw

    # Shows who's turn it is
    if winner is None:
        message = turn + "'s Turn"

    text = font.render(message, True, (255, 255, 255))

    # Text area at the bottom of the screen
    bar_y_start = HEIGHT - BAR_HEIGHT
    window.fill((0, 0, 0), (0, bar_y_start, WIDTH, BAR_HEIGHT))

    # Center the text horizontally and vertically in that bottom bar
    text_rect = text.get_rect(center=(WIDTH / 2, bar_y_start + BAR_HEIGHT // 2))

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
    # Without these, the previous round painting stays
    window.fill((52, 78, 91)) 
    window.fill(BLACK, (0, HEIGHT - BAR_HEIGHT, WIDTH, BAR_HEIGHT))

#function to check the winner
def check_winner():
    global draw, winner
    
    # check columns (vertical lines)
    for col in range(3):
        if taken_section[col][0] is not None and taken_section[col][0] == taken_section[col][1] == taken_section[col][2]:
            x = (col * CELL_SIZE) + CELL_SIZE // 2 #middle of each cell
            pygame.draw.line(window, RED, (GRID_OFFSET_X + x, 0), (GRID_OFFSET_X + x, GRID_SIZE), 6) 
            return taken_section[col][0]

    # check rows (horizontal lines)
    for row in range(3):
        if taken_section[0][row] is not None and taken_section[0][row] == taken_section[1][row] == taken_section[2][row]:
            y = (row * CELL_SIZE) + CELL_SIZE // 2 #middle of each cell
            pygame.draw.line(window, RED, (GRID_OFFSET_X, y), (GRID_OFFSET_X + GRID_SIZE, y), 6) 
            return taken_section[0][row]

    # check diagonals
    if taken_section[0][0] is not None and taken_section[0][0] == taken_section[1][1] == taken_section[2][2]:
        pygame.draw.line(window, RED, (GRID_OFFSET_X, 0), (GRID_OFFSET_X + GRID_SIZE, GRID_SIZE), 6)
        return taken_section[0][0]

    if taken_section[0][2] is not None and taken_section[0][2] == taken_section[1][1] == taken_section[2][0]:
        pygame.draw.line(window, RED, (GRID_OFFSET_X, GRID_SIZE), (GRID_OFFSET_X + GRID_SIZE, 0), 6)
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
    
    # Center the text in the middle of the screen
    text_rect = text.get_rect(center=(GRID_OFFSET_X + GRID_SIZE/2, GRID_SIZE/2)) 
    window.blit(text, text_rect)
    pygame.display.update()

# Function to draw the scoreboard 
def draw_scoreboard():
    score_text = f"X Wins: {x_wins}  O Wins: {o_wins}  Draws: {draws}"
    
    # Scale font size based on bar height
    score_font_size = int(BAR_HEIGHT * 0.6)
    score_font = pygame.font.SysFont("arialblack", score_font_size)
    text = score_font.render(score_text, True, WHITE)

    # Draw on bottom black area
    bar_y_start = HEIGHT - BAR_HEIGHT
    window.fill((0, 0, 0), (0, bar_y_start, WIDTH, BAR_HEIGHT))
    
    # Center the text in the bottom bar
    text_rect = text.get_rect(center=(WIDTH // 2, bar_y_start + BAR_HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.update()

# Function generating a random computer move
def computer_move():
    global turn
    empty_cells = [(row, column) for row in range(3) for column in range(3) if taken_section[row][column] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        draw_xo(row, col)

# Keep the screen window open
running = True
while running:
    if start == True:
    # Draw each line below the previous one
        for i, line in enumerate(menu_lines):
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50)) # 'i' needed so the messages don't overlap
            window.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    window.fill((52, 78, 91))
                    draw_grid()
                    start = False         
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    draw_scoreboard()
                    time.sleep(1.5) 
                elif event.key == pygame.K_a:
                    vs_computer = True
                    start = False
                    window.fill((52, 78, 91))
                    draw_grid()

    # "Play again" message
    elif end_condition == True:
        font_big = pygame.font.SysFont(None, 60)
        text = font_big.render("Play again? (Y = Yes / Q = Quit)", True, WHITE)
        
        # Using the bottom bar
        bar_y_start = HEIGHT - BAR_HEIGHT
        window.fill((0, 0, 0), (0, bar_y_start, WIDTH, BAR_HEIGHT)) 
        text_rect = text.get_rect(center=(WIDTH // 2, bar_y_start + BAR_HEIGHT // 2)) 
        window.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y: 
                    reset_game()            
                elif event.key == pygame.K_q: 
                    running = False
    #Main loop
    else:
        draw_grid() # Redraw grid every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_scoreboard()
                    time.sleep(1.5) # Scoreboard stays for 1.5s
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Checking for left clicks in specific
                (x_coordinate, y_coordinate) = pygame.mouse.get_pos()
                
                # Check if the click is within the grid's bounds
                if (x_coordinate > GRID_OFFSET_X and x_coordinate < GRID_OFFSET_X + GRID_SIZE and
                    y_coordinate > GRID_OFFSET_Y and y_coordinate < GRID_OFFSET_Y + GRID_SIZE):
                    
                    # Translate window coordinates to grid coordinates
                    row = (x_coordinate - GRID_OFFSET_X) // CELL_SIZE
                    column = (y_coordinate - GRID_OFFSET_Y) // CELL_SIZE
                    
                    if taken_section[row][column] is None:
                        draw_xo(row, column)
        
        if winner is None and not draw and turn == 'o' and vs_computer == True:
            computer_move()
        
        winner = check_winner()
        
        if winner != None or draw == True:
            draw_winner(winner)
        else:
            # Only draw 'turn' if the game isn't over
            draw_turn()
        
        pygame.display.update()

pygame.quit()