import pygame

pygame.init()

display = pygame.display.set_mode((500, 400))

vertices = [(300, 150), (150, 375), (450, 375)]

midpoint = ((vertices[0][0] + vertices[1][0] + vertices[2][0]) // 3, (vertices[0][1] + vertices[1][1] + vertices[2][1]) // 3)

distances = [(vertex[0] - midpoint[0], vertex[1] - midpoint[1]) for vertex in vertices]

scaling_factor = 0.5
scaled_distances = [(distance[0] * scaling_factor, distance[1] * scaling_factor) for distance in distances]
inverted_vertices = [(midpoint[0] - scaled_distance[0], midpoint[1] - scaled_distance[1]) for scaled_distance in scaled_distances]

blue = (0, 0, 255)
white = (255, 255, 255)
purple = (255, 0, 255)

pygame.draw.polygon(display, blue, vertices)
pygame.draw.polygon(display, white, inverted_vertices)
pygame.draw.circle(display, purple, midpoint, 5)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f1:
                running = False
main()