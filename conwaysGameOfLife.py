'''
Created on Feb 18, 2018

@author: chris
'''
import sys, pygame
import copy


def setState(sum, state):
    if (state == 1):
        if (sum < 2) or (sum > 3):
            return 0
        else:
            return 1
    else:
        if (sum == 3):
            return 1
        else:
            return 0

def checkNeighbours(array, x, y):
    numNeighbours = array[y-1][x-1] + array[y-1][x] + array[y-1][x+1] + array[y][x-1] + array[y][x+1] + array[y+1][x-1] + array[y+1][x] + array[y+1][x+1]
    return numNeighbours

def genArray(width, height):
    array = []

    for y in range(0, height):
        array.append([])

    for y in range(0, height):
        for x in range(0, width):
            array[y].append(0)
            
    return array

def run(array, x, y):
    state = array[y][x]
    total = checkNeighbours(array, x, y)
    return setState(total, state)
    

def main():
    pygame.init()
    WIDTH = 1080
    HEIGHT = 720
    tile = 10

    clock = pygame.time.Clock()
    
    dead = pygame.image.load("white.png")
    alive = pygame.image.load("black.png")
    
    array = genArray(108, 72)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    running = False

    while True:
        temp = copy.deepcopy(array)
        for y in range(0, len(array) - 1):
            for x in range(0, len(array[y]) - 1):
                currTile = pygame.Rect((x*tile, y*tile), (tile, tile))
                if(running == True):
                    temp[y][x] = run(array, x, y)
                if(array[y][x] == 0):
                    window.blit(dead,currTile)
                elif(array[y][x] == 1):
                    window.blit(alive,currTile)
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(running == False):
                    if event.button == 1:
                        xpos = event.pos[0] // 10
                        ypos = event.pos[1] // 10

                        if(array[ypos][xpos] == 0):
                            array[ypos][xpos] = 1
                        elif(array[ypos][xpos] == 1):
                            array[ypos][xpos] = 0
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if running == False:
                        running = True
                    elif running == True:
                        running = False
                        
        if(running == True):
            array = copy.deepcopy(temp)
        
        pygame.display.update()
        clock.tick(15)
main()