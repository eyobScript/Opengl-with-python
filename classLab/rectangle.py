import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_rectangle():
    # Get the center of the screen
    center_x, center_y = 400, 300  # Assuming a window size of 800x600
    width, height = 200, 100  # Width and height of the rectangle

    # Set the color for the rectangle (RGB values between 0 and 1)
    glColor3f(1, 0, 0)  # Red color

    # Draw the rectangle centered at (center_x, center_y)
    glBegin(GL_QUADS)
    glVertex2f(center_x - width / 2, center_y - height / 2)  # Bottom-left
    glVertex2f(center_x + width / 2, center_y - height / 2)  # Bottom-right
    glVertex2f(center_x + width / 2, center_y + height / 2)  # Top-right
    glVertex2f(center_x - width / 2, center_y + height / 2)  # Top-left
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
