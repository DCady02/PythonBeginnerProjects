import pygame
import time
from random import randint

black = (0,0,0)
moving = True

class Snake(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(black)
		self.image.set_colorkey(black)

		pygame.draw.rect(self.image, color, [0,0,width,height])

		self.rect = self.image.get_rect()

	def move(self, up_speed, down_speed, left_speed, right_speed):

		self.rect.y += down_speed
		self.rect.y -= up_speed
		self.rect.x += right_speed
		self.rect.x -= left_speed

		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= 485:
			self.rect.y = 485
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= 485:
			self.rect.x = 485

class Food(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(black)
		self.image.set_colorkey(black)

		pygame.draw.rect(self.image, color, [0,0,width,height])

		self.rect = self.image.get_rect()

	def dinners_ready(self):

		self.rect.y = randint(0, 485)
		self.rect.x = randint(0, 485)





