import pygame
import sys

def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('My Canvas')

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

        # Fill the screen with white color
        screen.fill((255, 255, 255))

        # Update the display
        pygame.display.flip()

# Run the main function
if __name__ == "__main__":
    main()