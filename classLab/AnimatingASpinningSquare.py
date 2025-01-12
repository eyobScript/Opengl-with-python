import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_square(angle):
    # Get the center of the screen
    center_x, center_y = 400, 300  # Assuming a window size of 800x600

    # Set the color for the square (RGB values between 0 and 1)
    glColor3f(1, 1, 0)  # Yellow color

    # Apply rotation to the square
    glPushMatrix()  # Save the current matrix
    glTranslatef(center_x, center_y, 0)  # Move to the center
    glRotatef(angle, 0, 0, 1)  # Rotate square around Z-axis

    # Draw the square
    glBegin(GL_QUADS)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    glPopMatrix()  # Restore the matrix


def main():
    # Initialize Pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set the projection matrix for 2D rendering
    gluOrtho2D(0, display[0], 0, display[1])

    angle = 0  # Initial rotation angle

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the rotating square
        draw_square(angle)

        # Increment the angle for the next frame
        angle += 1
        if angle >= 360:
            angle = 0  # Reset the angle after a full rotation

        # Swap the buffer to display the spinning square
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
