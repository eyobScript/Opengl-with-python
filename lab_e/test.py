import pygame
import sys


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the canvas
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Entangled Triangles")
    screen.fill((255, 255, 255))  # Fill the canvas with white color

    # Define the vertices for the large blue triangle
    large_triangle_vertices = [(250, 50), (100, 400), (400, 400)]

    # Define the vertices for the smaller inverted white triangle
    small_triangle_vertices = [(250, 396), (175, 225), (325, 225)]

    # Draw the large blue triangle
    pygame.draw.polygon(screen, (0, 0, 255), large_triangle_vertices)

    # Draw the smaller inverted white triangle
    pygame.draw.polygon(screen, (255, 255, 255), small_triangle_vertices)

    # Main loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):
                running = False
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Run the main function
main()
