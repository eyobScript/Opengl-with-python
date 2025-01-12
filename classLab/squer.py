import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_square():
    # Get the center of the screen
    center_x, center_y = 400, 300  # Assuming a window size of 800x600
    size = 100  # Half of the square's side length (since we'll draw from the center)

    # Set the color for the square (RGB values between 0 and 1)
    glColor3f(1, 0, 0)  # Red color

    # Draw the square centered at (center_x, center_y)
    glBegin(GL_QUADS)
    glVertex2f(center_x - size, center_y - size)  # Bottom-left
    glVertex2f(center_x + size, center_y - size)  # Bottom-right
    glVertex2f(center_x + size, center_y + size)  # Top-right
    glVertex2f(center_x - size, center_y + size)  # Top-left
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

        # Call the draw_square function
        draw_square()

        # Swap the buffer to display the square
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
