import pygame
from random import randint
from sprites import Snake
from sprites import Food
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

snake = Snake(white, 15, 15)
snake.rect.x = 10
snake.rect.y = 10

food = Food(red, 15, 15)
food.rect.x = randint(0, 485)
food.rect.y = randint(0, 485)

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(snake)
all_sprites_list.add(food)

clock = pygame.time.Clock()

playing = True
udlr = [False, False, False, False]

while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				playing = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		udlr = [True, False, False, False]
	elif keys[pygame.K_DOWN]:
		udlr = [False, True, False, False]
	elif keys[pygame.K_LEFT]:
		udlr = [False, False, True, False]
	elif keys[pygame.K_RIGHT]:
		udlr = [False, False, False, True]

	if udlr[0]:
		snake.move(5,0,0,0)
	elif udlr[1]:
		snake.move(0,5,0,0)
	elif udlr[2]:
		snake.move(0,0,5,0)
	elif udlr[3]:
		snake.move(0,0,0,5)

	if pygame.sprite.collide_mask(food, snake):
		food.dinners_ready()

	all_sprites_list.update()

	screen.fill(black)

	all_sprites_list.draw(screen)

	pygame.display.flip()

	clock.tick(30)