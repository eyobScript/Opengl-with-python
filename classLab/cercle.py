import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_spinning_circle(angle):
    # Get the center of the screen
    center_x, center_y = 400, 300  # Assuming a window size of 800x600
    radius = 100  # Radius of the circle

    # Set the color for the circle (RGB values between 0 and 1)
    glColor3f(0, 0, 1)  # Blue color

    # Apply rotation to the circle
    glPushMatrix()  # Save the current matrix
    glTranslatef(center_x, center_y, 0)  # Move to the center
    glRotatef(angle, 0, 0, 1)  # Rotate circle around Z-axis

    # Draw the circle
    glBegin(GL_POLYGON)
    for i in range(360):
        angle_rad = math.radians(i)  # Convert angle to radians
        x = radius * math.cos(angle_rad)  # Calculate x coordinate
        y = radius * math.sin(angle_rad)  # Calculate y coordinate
        glVertex2f(x, y)  # Set the vertex at (x, y)
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

        # Draw the rotating circle
        draw_spinning_circle(angle)

        # Increment the angle for the next frame
        angle += 1
        if angle >= 360:
            angle = 0  # Reset the angle after a full rotation

        # Swap the buffer to display the spinning circle
        pygame.display.flip()
        pygame.time.wait(10)


# Run the main function
main()
