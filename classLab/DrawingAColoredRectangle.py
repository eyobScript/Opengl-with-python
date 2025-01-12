#Draw a red, green, blue colored rectangle (use the skeleton you used for triangle.)
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_rectangle():
    # Set the color for the rectangle (RGB values between 0 and 1)

    # Red rectangle
    glColor3f(1, 0, 0)  # Red color
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 300)
    glVertex2f(100, 300)
    glEnd()

    # Green rectangle
    glColor3f(0, 1, 0)  # Green color
    glBegin(GL_QUADS)
    glVertex2f(450, 100)
    glVertex2f(750, 100)
    glVertex2f(750, 300)
    glVertex2f(450, 300)
    glEnd()

    # Blue rectangle
    glColor3f(0, 0, 1)  # Blue color
    glBegin(GL_QUADS)
    glVertex2f(100, 350)
    glVertex2f(400, 350)
    glVertex2f(400, 550)
    glVertex2f(100, 550)
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

        # Call the draw_rectangle function
        draw_rectangle()

        # Swap the buffer to display the rectangle
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
