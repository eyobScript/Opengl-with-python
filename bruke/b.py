import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vertices and edges of the cube
cubeVertices = (
    (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
    (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1)
)

cubeEdges = (
    (0, 1), (0, 3), (0, 4), (1, 2),
    (1, 7), (2, 3), (2, 5), (3, 6),
    (4, 6), (4, 7), (5, 6), (5, 7)
)

# Initial rotation angles for the cube
angle_x = 0.0
angle_y = 0.0


# Function to draw the cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in cubeEdges:
        for vertex in edge:
            glVertex3fv(cubeVertices[vertex])
    glEnd()


# Function to handle keyboard events
def keyboard(key):
    global angle_x, angle_y
    if key == b'w':
        angle_x += 5.0
    elif key == b's':
        angle_x -= 5.0
    elif key == b'a':
        angle_y -= 5.0
    elif key == b'd':
        angle_y += 5.0


# Function to initialize OpenGL settings
def init():
    glEnable(GL_DEPTH_TEST)


# Main function to initialize the window and run the application
def main():
    global angle_x, angle_y

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Initialize OpenGL settings
    init()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Handle keyboard events
            if event.type == KEYDOWN:
                keyboard(event.unicode.encode())  # Convert the key to byte format

        # Apply rotations based on the keyboard input
        glRotatef(angle_x, 1, 0, 0)  # Rotate around X-axis
        glRotatef(angle_y, 0, 1, 0)  # Rotate around Y-axis

        # Clear the screen and redraw the cube
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()  # Update the display

        pygame.time.wait(10)  # Slow down the loop for better performance


# Ensure the program runs when executed
if __name__ == "__main__":
    main()
