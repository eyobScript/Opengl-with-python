import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_spinning_rectangle(angle):
    # Get the center of the screen
    center_x, center_y = 400, 300  # Assuming a window size of 800x600
    width, height = 200, 100  # Width and height of the rectangle

    # Set the color for the rectangle (RGB values between 0 and 1)
    glColor3f(0, 0, 1)  # Blue color

    # Apply rotation to the rectangle
    glPushMatrix()  # Save the current matrix
    glTranslatef(center_x, center_y, 0)  # Move to the center
    glRotatef(angle, 0, 0, 1)  # Rotate rectangle around Z-axis

    # Draw the rectangle
    glBegin(GL_QUADS)
    glVertex2f(-width / 2, -height / 2)  # Bottom-left
    glVertex2f(width / 2, -height / 2)  # Bottom-right
    glVertex2f(width / 2, height / 2)  # Top-right
    glVertex2f(-width / 2, height / 2)  # Top-left
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

        # Draw the rotating rectangle
        draw_spinning_rectangle(angle)

        # Increment the angle for the next frame
        angle += 1
        if angle >= 360:
            angle = 0  # Reset the angle after a full rotation

        # Swap the buffer to display the spinning rectangle
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
