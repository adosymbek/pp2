import pygame,random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


colors = {
        'white': WHITE, 
        'black': BLACK,
        'red': RED,
        'blue': BLUE,
        'green': GREEN
    }
mode = 'random'
radius = 10

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None


screen.fill(BLACK)

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mode = 'black' 
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_w:
                    mode = 'white'
                if event.key == pygame.K_UP:
                    radius += 5
                if event.key == pygame.K_DOWN:
                    radius -= 5
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
      if mode == 'random':
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
      else:
        color = colors[mode]
    if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev:
        pygame.draw.line(screen,color, prev, cur, radius)
        prev = cur
    if event.type == pygame.MOUSEBUTTONUP:
      prev = None

  pygame.display.flip()

  clock.tick(30)


pygame.quit()