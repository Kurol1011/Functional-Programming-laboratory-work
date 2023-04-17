
import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576
icon = pygame.image.load('assets/images/381603_pacman_icon.png')
def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    pygame.display.set_caption("PAC MAN")
    pygame.display.set_icon(icon)
    
    done = False
    
    clock = pygame.time.Clock()
    
    game = Game()
    
    while not done:
        
        done = game.process_events()
        
        game.run_logic()
        
        game.display_frame(screen)
        
        clock.tick(30)
         
    pygame.quit()

if __name__ == '__main__':
    main()
