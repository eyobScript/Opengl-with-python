import pygame
import sys

def main():

    pygame.init()


    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('My Canvas')


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()


        screen.fill((255, 255, 255))


        pygame.draw.line(screen, (255, 0, 0), (50, 50), (50 + 200, 50), 3)


        pygame.display.flip()


if __name__ == "__main__":
    main()
