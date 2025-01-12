import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Function to draw a single triangle
def draw_triangle(vertices, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


def main():
    # Initialize Pygame and set up the OpenGL display
    pygame.init()
    display = (800, 800)  # Window size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 1, 0, 1)  # Set up the 2D orthographic projection

    # Center position and size
    center_x = 0.5
    center_y = 0.5
    size = 0.25  # Size of the triangles

    # Define the vertices for the three triangles
    # Flip the top triangle upside down
    top_triangle = [(center_x, center_y - size),
                    (center_x - size, center_y + size),
                    (center_x + size, center_y + size)]

    bottom_left_triangle = [(center_x - size, center_y - size),
                            (center_x - size * 2, center_y),
                            (center_x, center_y)]

    bottom_right_triangle = [(center_x + size, center_y - size),
                             (center_x + size * 2, center_y),
                             (center_x, center_y)]

    # Colors for the triangles
    top_color = (0, 1, 1)  # Cyan
    bottom_left_color = (0, 0, 1)  # Blue
    bottom_right_color = (0, 0, 0.5)  # Dark Blue

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the triangles
        draw_triangle(top_triangle, top_color)
        draw_triangle(bottom_left_triangle, bottom_left_color)
        draw_triangle(bottom_right_triangle, bottom_right_color)

        # Swap the buffers
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
