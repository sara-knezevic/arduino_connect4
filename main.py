import sys, pygame

from alphabeta import alphabeta
from connect4 import State, done, score, successor, draw
from constants import *

# ser = serial.Serial()
# ser.timeout = 1
# ser.port = '/dev/ttyACM0' 
# ser.open()

def get_play_options(state):
    options = []
    for j in range(0, state.width):
        for i in range(state.height - 1, -1, -1):
            if state.board[i][j] != EMPTY_SLOT: continue
            options.append((i, j))
            break
    return options

def end_game(status, current_state):
    if status == GAME_MIN_WINNER:
        sys.stdout.write('You win!\n')
    elif status == GAME_MAX_WINNER:
        sys.stdout.write('Algorithm wins!\n')
    elif status == GAME_DRAW:
        sys.stdout.write('It\s a draw!\n')

    input()
    sys.exit(1)
    
def update_game(current_state, screen):
    status = done(current_state)

    draw(current_state, screen, grid_width, grid_height,
         field_size, circle_size)
    pygame.display.flip()

    sys.stdout.write(str(current_state) + '\n')
    
    if status != GAME_NO_WINNER:
        end_game(status, current_state)

# pygame parameters
grid_width = 510
grid_height = 510

field_size = 100
circle_size = 40

def human_vs_computer():
    current_state = State(width = 5, height = 5)

    pygame.init()

    screen = pygame.display.set_mode((grid_width, grid_height))
    game_over = False

    while not game_over:

        draw(current_state, screen, grid_width, grid_height,
             field_size, circle_size)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Human Turn
        sys.stdout.write('\n')
        print(current_state)
        options = get_play_options(current_state)
        for i in range(0, current_state.width):
            sys.stdout.write(' ' + str(i + 1) + ' ')
        sys.stdout.write('\n ')

        # while True:
        #     ard = ser.readline().decode().strip('\r\n')

        #     if (ard != ''):
        #         break

        # col = int(ard) - 1
        col = int(input()) - 1 

        for i, j in options:
            if col != j: continue
            current_state.board[i][j] = MIN_PLAYER

        update_game(current_state, screen)
        
        # AI Turn
        current_state, _score = alphabeta(current_state, 5, MAX_PLAYER, score, done, successor)
        update_game(current_state, screen)

        #draw(current_state, screen, grid_width, grid_height,
        #     field_size, circle_size)

    pygame.quit()

    
if __name__ == '__main__':
    human_vs_computer()
