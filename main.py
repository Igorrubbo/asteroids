import pygame
import constants

height = constants.SCREEN_HEIGHT
width = constants.SCREEN_WIDTH

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {width}")
  print(f"Screen height: {height}")
  screen = pygame.display.set_mode([width, height])
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      screen.fill("black")
      pygame.display.flip()

if __name__ == "__main__":
  main()