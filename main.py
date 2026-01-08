import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

VERSION = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(
        (
            SCREEN_WIDTH,
            SCREEN_HEIGHT
        ),
        pygame.RESIZABLE
    )
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(
            "black"
        )
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000


if __name__ == "__main__":
    main()
