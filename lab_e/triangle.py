import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangle():
    # Define the vertices of the triangle
    vertices = [
        (0, 1),  # Top vertex
        (-1, -1),  # Bottom left vertex
        (1, -1)  # Bottom right vertex
    ]

    # Set the color to purple (RGB: 128, 0, 128)
    glColor3f(0.502, 0.0, 0.502)

    # Draw the triangle
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


def main():
    # Initialize Pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Set up the OpenGL projection
    gluOrtho2D(-2, 2, -2, 2)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with a black background
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the purple triangle
        draw_triangle()

        # Swap the buffers to display the rendered scene
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


# Run the main function
main()
