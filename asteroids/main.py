import pygame
from constants import *
from logger import log_state
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        dt = clock.tick(60) / 1000      
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        updatable.update(dt)
        screen.fill("black")
        for da in drawable:
            da.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        print(dt)
        


if __name__ == "__main__":
    main()

