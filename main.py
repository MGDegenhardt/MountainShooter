import pygame

pygame.init()
window = pygame.display.set_mode(size=(600, 480))

while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # closes the game window
            quit()  # end pygame
