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
    large_triangle_vertices = [(250, 40), (100, 400), (400, 400)]

    # Define the vertices for the smaller inverted white triangle
    small_triangle_vertices = [(250, 395), (175, 225), (325, 225)]

    # Draw the large blue triangle
    pygame.draw.polygon(screen, (0, 0, 255), large_triangle_vertices)

    # Draw the smaller inverted white triangle
    pygame.draw.polygon(screen, (255, 255, 255), small_triangle_vertices)

    # Calculate the center of the large blue triangle using the average of the vertices
    center_x = (large_triangle_vertices[0][0] + large_triangle_vertices[1][0] + large_triangle_vertices[2][0]) // 3
    center_y = (large_triangle_vertices[0][1] + large_triangle_vertices[1][1] + large_triangle_vertices[2][1]) // 3

    # Draw the purple point at the center of the large triangle
    pygame.draw.circle(screen, (128, 0, 128), (center_x, center_y), 5)

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
