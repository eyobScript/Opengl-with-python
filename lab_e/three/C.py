import pygame
import sys


def main():

    pygame.init()


    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Entangled Triangles")
    screen.fill((255, 255, 255))  # Fill the canvas with white color


    large_triangle_vertices = [(250, 50), (100, 400), (400, 400)]


    small_triangle_vertices = [(250, 400), (175, 225), (325, 225)]


    pygame.draw.polygon(screen, (0, 0, 255), large_triangle_vertices)


    pygame.draw.polygon(screen, (255, 255, 255), small_triangle_vertices)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):
                running = False
        pygame.display.flip()


    pygame.quit()
    sys.exit()


# Run the main function
main()
