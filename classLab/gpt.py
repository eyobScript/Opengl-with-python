import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_circle(radius):
    # Center of the screen
    center_x, center_y = 400, 300
    segments = 360  # Number of segments in the circle

    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = math.radians(i)
        x = center_x + math.cos(angle) * radius
        y = center_y + math.sin(angle) * radius
        glVertex2f(x, y)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, display[0], 0, display[1])

    radius = 50  # Initial radius
    growing = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the circle
        draw_circle(radius)

        # Animate circle's size (expand/shrink)
        if growing:
            radius += 1
            if radius > 100:
                growing = False
        else:
            radius -= 1
            if radius < 50:
                growing = True

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main loop
main()
