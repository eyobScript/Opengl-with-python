import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Define the vertices of a cube
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
]

# Define the edges that connect the vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the surfaces of the cube (for coloring)
surfaces = [
    (0, 1, 2, 3),  # Front face
    (3, 2, 6, 7),  # Top face
    (7, 6, 5, 4),  # Back face
    (4, 5, 1, 0),  # Bottom face
    (1, 5, 6, 2),  # Right face
    (7, 3, 0, 4)  # Left face
]

# Define the colors for each surface (RGB)
colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (0, 1, 1),  # Cyan
    (1, 0, 1)  # Magenta
]


def draw_cube():
    # Draw the surfaces with colors
    for i, surface in enumerate(surfaces):
        glBegin(GL_QUADS)
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
        glEnd()

    # Draw the edges of the cube (wireframe)
    glColor3f(0, 0, 0)  # Black color for edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set the camera perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Rotation angles
    x_rotation = 0
    y_rotation = 0

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Rotate the cube around the X and Y axes
        glPushMatrix()
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        # Draw the cube
        draw_cube()

        glPopMatrix()

        # Update rotation angles
        x_rotation += 1
        y_rotation += 1

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main loop
main()
