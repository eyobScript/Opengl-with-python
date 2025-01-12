import pygame
import sys

def main():

    pygame.init()


    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Entangled Triangles")
    screen.fill((255, 255, 255))  # Fill the canvas with white color


    large_triangle_vertices = [(250, 40), (100, 400), (400, 400)]


    small_triangle_vertices = [(250, 395), (175, 225), (325, 225)]


    pygame.draw.polygon(screen, (0, 0, 255), large_triangle_vertices)


    pygame.draw.polygon(screen, (255, 255, 255), small_triangle_vertices)


    center_x = (large_triangle_vertices[0][0] + large_triangle_vertices[1][0] + large_triangle_vertices[2][0]) // 3
    center_y = (large_triangle_vertices[0][1] + large_triangle_vertices[1][1] + large_triangle_vertices[2][1]) // 3


    pygame.draw.circle(screen, (128, 0, 128), (center_x, center_y), 5)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):
                running = False
        pygame.display.flip()


    pygame.quit()
    sys.exit()



main()
