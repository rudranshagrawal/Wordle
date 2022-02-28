"""
Wordle in Python
Author: Rudransh Agrawal
"""
import pygame
import sys
import random
from collections import deque

# Define some colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

# This sets the margin between each cell
MARGIN = 0

# Set the COLUMNS and ROWS of the screen
COLUMNS, ROWS = 5, 6
# This sets the WIDTH and HEIGHT of each grid location
WINDOW_SIZE = [GAME_WIDTH, GAME_HEIGHT] = [500, 600]
WIDTH, HEIGHT = GAME_WIDTH // COLUMNS, GAME_HEIGHT // ROWS

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)


class Node:
    def __init__(self, i, j):
        self.row, self.column = i, j
        self.letter = None
        self.color = WHITE


grid = []

# Add a Node Object to eachpoint in grid
for row in range(ROWS):
    arr = []
    for column in range(COLUMNS):
        arr.append(Node(row, column))
    grid.append(arr)


# Initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("Wordle")

# Flag to Indicate Start of Implementation
checkWordFlag = False
waitForEnter = False
wordNotFinished = True

# Flag to Indicate Start of Completion
completionFlag = False
enteredWord = ""

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.SysFont('arial', 50)

# window.fill((255, 255, 255))
# window.blit(text, rect)

targetWord = ""
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    # print random string
    targetWord = random.choice(words)
    print(targetWord)

def wait_for_key_press():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_BACKSPACE:
                    wait = False
                    break

    return True


# Program Starts Running Here

grid_row = 0
grid_column = 0

while True:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            # done = True  # Flag that we are done so we exit this loop
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                checkWordFlag = True
            if event.key == pygame.K_BACKSPACE:
                if grid_column > 0:
                    grid_column -= 1
                    grid[grid_row][grid_column].letter = None
                if not wordNotFinished:
                    wordNotFinished = True
            elif pygame.key.name(event.key) and wordNotFinished:
                grid[grid_row][grid_column].letter = pygame.key.name(event.key).upper()
                enteredWord += pygame.key.name(event.key).upper()
                # grid_row += 1
                grid_column += 1

            # pygame.key.name(event.key)
            # if event.key == pygame.K_RETURN:
            #     startFlag = True
            # if event.key == pygame.K_q:
            #     screen.blit(companyLogo, (0, 0))
            #     pygame.display.update()  # needed to show the effect of the blit
            #     # Bunch of other code goes here, like changing the score, etc.
            #     wait_for_key_press()
            #     # new_game()

    # if waitForEnter:
    #     checkWordFlag = wait_for_key_press()
    #     waitForEnter = False

    if checkWordFlag:
        print(enteredWord)
        print(grid_row)
        print(grid_column)
        for columns_iterable in range(0, COLUMNS):

            if grid[grid_row][columns_iterable].letter in list(targetWord):
                grid[grid_row][columns_iterable].color = YELLOW

            if grid[grid_row][columns_iterable].letter == list(targetWord)[columns_iterable]:
                grid[grid_row][columns_iterable].color = GREEN

        grid_row += 1
        grid_column = 0
        enteredWord = ""
        checkWordFlag = False
        wordNotFinished = True



    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            pygame.draw.rect(screen, grid[row][column].color, [WIDTH * column, HEIGHT * row, WIDTH - 2, HEIGHT - 2])
            if grid[row][column].letter is not None:
                text = font.render(grid[row][column].letter, True, (0, 0, 0))
                rect = text.get_rect()
                rect = (100*column+25, 100*row+25)
                screen.blit(text, rect)

                # pygame.draw.circle(screen, WHITE, (coldumn * WIDTH + WIDTH // 2, row * HEIGHT + HEIGHT // 2), WIDTH // 3)

    pygame.display.flip()

    if grid_column == 5:
        wordNotFinished = False
        # waitForEnter = True

print("Could Not Find Shortest Path: Way is Blocked")
