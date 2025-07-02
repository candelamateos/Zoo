from Controller import GameController
import pygame

def main():
    pygame.init()
    juego = GameController()
    juego.run()
    pygame.quit()

if __name__ == "__main__":
    main()
 