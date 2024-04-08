import pygame
import random

pygame.init()

#Creating colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

#Other Variables for use in the program
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
score = 0
level = 0
speed = 15
font = pygame.font.SysFont("Verdana", 20)

#Create a screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)




class Point:
  def __init__(self, _x: int, _y: int):
    self.x = _x
    self.y = _y
  

class Food:
  def __init__(self, *args, **kwargs):
    self.location = Point(0, 0)
    self.radius = 10
    self.set_random_position()
  
  @staticmethod
  def own_round(value, base = 10):
    return base * round(value / 10)

  def set_random_position(self):
    x = self.own_round(random.randint(20, WINDOW_WIDTH-20))
    y = self.own_round(random.randint(20, WINDOW_HEIGHT-20))
    self.location.x = x
    self.location.y = y
  
  def draw(self):
    pygame.draw.circle(screen, BLUE, (self.location.x, self.location.y), self.radius)

class BigFood:
  def __init__(self, *args, **kwargs):
    self.location = Point(0, 0)
    self.radius = 20
    self.set_random_position()
  
  @staticmethod
  def own_round(value, base = 10):
    return base * round(value / 10)

  def set_random_position(self):
    x = self.own_round(random.randint(40, WINDOW_WIDTH-40))
    y = self.own_round(random.randint(40, WINDOW_HEIGHT-40))
    self.location.x = x
    self.location.y = y
  
  def draw(self):
    pygame.draw.circle(screen, BLUE, (self.location.x, self.location.y), self.radius)


class Snake:
  def __init__(self, *args, **kwargs):
    self.radius = 10
    self.body = [Point(100, 100), Point(110, 100)]
    self.block = 15
    self.dx = self.block
    self.dy = 0
  
  def head(self):
    return self.body[0]
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i].x = self.body[i - 1].x
      self.body[i].y = self.body[i - 1].y

    self.head().x += self.dx
    self.head().y += self.dy
    
    # границы . если сталкивается с границей возвращать в противоположную сторону
    if self.head().x > WINDOW_WIDTH - 20:
      self.dx = - self.dx
    if self.head().x < 20:
      self.dx = - self.dx
    if self.head().y > WINDOW_HEIGHT - 20:
      self.dy = - self.dy
    if self.head().y < 20:
      self.dy = - self.dy

  def draw(self):
    for i, point in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.circle(screen, color, (point.x, point.y), self.radius)

  def add_tail(self):
    self.body.append(Point(0, 0))
    global score
    global level
    global speed
    if score % 3== 0 and score>= 3:
            speed += 1
            level += 1
  
  def eat(self, foodx, foody):
        x =  self.head().x
        y =  self.head().y
        
        if abs(x-foodx) <= 2*self.radius and abs(y-foody) <= 2*self.radius:
            global score 
            score += 1
            return True
        return False

snake = Snake()
food = Food()
big_food = BigFood()

timer = 0
time_on = False

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == INC_SPEED and time_on == True: 
         timer += 1
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        snake.dx, snake.dy = speed, 0
      if event.key == pygame.K_LEFT:
        snake.dx, snake.dy = -speed, 0
      if event.key == pygame.K_UP:
        snake.dx, snake.dy = 0, -speed
      if event.key == pygame.K_DOWN:
        snake.dx, snake.dy = 0, speed

  #   если змея сталкивается с едой 
  if snake.eat(food.location.x,food.location.y):
    snake.add_tail()
    food.set_random_position()
  
  #   если змея сталкивается с big едой 
  if snake.eat(big_food.location.x,big_food.location.y):
    time_on = False
    snake.add_tail()
    food.set_random_position()
  

  screen.fill(BLACK)

  # надпись баллов
  scores = font.render(str(score), True, WHITE) 
  scorestext = font.render('score:', True, WHITE)
  screen.blit(scores, (400,50))
  screen.blit(scorestext, (320,50))

  # надпись уровней
  levels = font.render(str(level), True, WHITE) 
  leveltext = font.render('level:', True, WHITE)
  screen.blit(levels, (100,50))
  screen.blit(leveltext, (30,50))


  snake.move()
  snake.draw()
  food.draw()

  if timer >= 7:
        time_on = False
        timer = 0
  if score >= 3 and score % 3 == 0 :
        time_on = True

  if time_on == True:
        big_food.draw()

  pygame.display.flip()

  clock.tick(5)

pygame.quit()