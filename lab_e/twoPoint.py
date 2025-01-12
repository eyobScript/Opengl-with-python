# Write a Python function that takes two points P1(x1, y1) and
# P2(x2, y2) to draw a line thru P1 and P2 using PyGame and
# OpenGL.
# HINT: Use GL_LINES, glVertex2f and glColor3f
# Syntax:
# def draw_line(x1, y1, x2, y2):
# glBegin(….)
# //your code here
# glEnd()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_line(x1, y1, x2, y2):
    # Set the color for the line (RGB values between 0 and 1)
    glColor3f(1, 0, 0)  # Red color

    # Begin drawing the line with GL_LINES
    glBegin(GL_LINES)

    # Define the coordinates for the two points
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    # End drawing the line
    glEnd()


def main():
    # Initialize Pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set the projection matrix for 2D rendering
    gluOrtho2D(0, display[0], 0, display[1])

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Call the draw_line function with two points
        draw_line(100, 100, 700, 500)

        # Swap the buffer to display the line
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()

