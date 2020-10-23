# Quick Sort algorithm

"""
Created: 05.07.20
Author: Bhaswar Chakraborty

Acknowledgements: The Coding Train, The Mango Tree

"""

import pygame, sys, random


# Change the dimension of window from here:
height = 300
width = 2*height

white = pygame.Color(120, 130, 120)
black = pygame.Color('black')
color1 = pygame.Color(200, 120, 200)
color2 = pygame.Color(255, 200, 40)
clock = pygame.time.Clock()
# Class
class Line:

    def __init__(self, x, length):
        self.x = x
        self.length = length

    def show(self, color):
        global screen, height
        pygame.draw.line(screen, color, (self.x, height), (self.x, self.length))


# Functions

def swap(i, j):
    lines[i].show(color1)
    lines[j].show(color2)
    lines[i].show(black)
    lines[j].show(black)
    lines[i], lines[j] = lines[j], lines[i]
    lines[i].x, lines[j].x = lines[j].x, lines[i].x
    pygame.time.delay(10)
    lines[j].show(color1)
    lines[i].show(color2)
    
    pygame.display.update()

def scramble():
    for i in range(len(lines) - 1):
        new_pos = random.randint(i, len(lines) - 1)
        lines[i], lines[new_pos] = lines[new_pos], lines[i]
        lines[i].x, lines[new_pos].x = lines[new_pos].x, lines[i].x
    return lines


def partion(arr, start, end):
    pivotIndex = start
    pivotValue = arr[end]
    for i in range(start, end):
        if arr[i].length < pivotValue.length:
            swap(i, pivotIndex)
            pivotIndex += 1
    swap(pivotIndex, end)
    return pivotIndex

def quick(arr, start, end):
    if start >= end:
        return
    index = partion(arr, start, end)
    
    quick(arr, start, index-1)
    quick(arr, index+1, end)


pygame.init()

screen = pygame.display.set_mode((width,height))

# line objects
lines = []

k = 0
for i in range(height):
    for j in range(1):
        lines.append(Line(i + k, i))
        k += 1

scramble()

# Main loop

background = screen.fill(black)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            quick(lines, 0, len(lines)-1)
            
    for line in lines:
        line.show(white)

    pygame.display.update()
