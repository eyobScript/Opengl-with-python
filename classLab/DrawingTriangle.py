import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangle():
    # Set the color for the triangle (RGB values between 0 and 1)
    glColor3f(0, 1, 0)  # Green color

    # Begin drawing the triangle with GL_TRIANGLES
    glBegin(GL_TRIANGLES)

    # Define the vertices for the triangle
    glVertex2f(400, 500)  # Top vertex
    glVertex2f(300, 300)  # Bottom-left vertex
    glVertex2f(500, 300)  # Bottom-right vertex

    # End drawing the triangle
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

        # Call the draw_triangle function
        draw_triangle()

        # Swap the buffer to display the triangle
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
