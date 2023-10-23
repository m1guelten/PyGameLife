import pygame
from utils import func_next_step
from constants import SQUARE_WIDTH, SQUARE_HEIGHT
# from snake import Snake
# from snake_collision import apple_collision, wall_collision
# from utils import generate_position
#
#
running = True
status_game = False


def game_start_data():
    with open('input.txt', 'rb') as file:
        start_data = file.read().decode().replace("\r\n", " ").split(" ")
        step = int(start_data[0])
        width = int(start_data[1])
        height = int(start_data[2])
    return step, width, height


def draw_field_game(full_width, full_height, width, height):
    screen = pygame.display.set_mode((full_width, full_height))
    screen.fill('gray')
    pygame.display.set_caption("Conway's Game of Life")
    for i in range(width):
        for j in range(height):
            pygame.draw.line(screen, 'black', [i * SQUARE_WIDTH, 0], [i * SQUARE_WIDTH, full_height], 1)
            pygame.draw.line(screen, 'black', [0, j * SQUARE_HEIGHT], [full_width, j * SQUARE_HEIGHT], 1)
    return screen

def game_setup():
    pygame.init()
    step, width, height = game_start_data()
    full_width, full_height = SQUARE_WIDTH * width, SQUARE_HEIGHT * height
    screen = draw_field_game(full_width, full_height, width, height)
    arr_game = [[0]*width for i in range(height)]
    clock = pygame.time.Clock()
    return screen, clock, arr_game, step


def manage_keyboard(arr):
    global running, status_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            status_game = True

        if event.type == pygame.MOUSEBUTTONDOWN and status_game is False:
            (pos_x, pos_y) = pygame.mouse.get_pos()
            index_x, index_y = pos_x // SQUARE_WIDTH, pos_y // SQUARE_HEIGHT
            arr[index_y][index_x] = 1 if arr[index_y][index_x] == 0 else 0
    return arr


def draw_arr(arr, screen):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            color_rect = 'yellow' if arr[i][j] == 1 else 'grey'
            pygame.draw.rect(screen, color_rect, (j * SQUARE_WIDTH + 1, i * SQUARE_HEIGHT + 1,
                                                SQUARE_WIDTH - 2, SQUARE_HEIGHT - 2), 30, 1)
            pygame.display.update()


def game():
    global running, status_game
    screen, clock, arr_game, step = game_setup()

    while running:
        arr_game = manage_keyboard(arr_game)
        draw_arr(arr_game, screen)
        if status_game is True:
            step_temp = step

            while step_temp != 0:
                arr_game = func_next_step(arr_game)
                pygame.time.wait(1000)
                draw_arr(arr_game, screen)
                step_temp -= 1
            status_game = False


        pygame.display.flip()

        clock.tick(60)
game()
pygame.quit()
