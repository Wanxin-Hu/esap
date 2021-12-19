#INIT
import pygame, math, sys
from pygame.locals import *


class BottleSprite(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.normal = pygame.image.load('pads_normal.jpg')
		self. hit = pygame.image.load('pads_hit.jpg')

		self.rect = pygame.Rect(self.normal.get_rect())
		self.rect.center = position

	def update(self, hit_list):
		if self in hit_list:
			self.image = self.hit
		else:
			self.image = self.normal

class CarSprite(pygame.sprite.Sprite):
	MAX_FORWARD_SPEED = 10
	MAX_REVERSE_SPEED = 10
	ACCELERATION = 2
	TURN_SPEED = 5

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load('car.png')
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())


	def update(self, dt):

		key_dict = pygame.key.get_pressed()
		if key_dict[pygame.K_LEFT]:
			self.rect.x -= 300 * dt
		if key_dict[pygame.K_RIGHT]:
			self.rect.x += 300 * dt
		if key_dict[pygame.K_UP]:
			self.rect.y -= 300 * dt
		if key_dict[pygame.K_DOWN]:
			self.rect.y += 300 * dt

class Game():

	def main(self, screen):
		clock = pygame.time.Clock()

		self.crash = pygame.mixer.Sound('crash.wav')

		#load background music
		pygame.mixer.music.load('f1.wav')
		#-1 for play this sound continuously
		pygame.mixer.music.play(-1)


		pygame.display.set_caption('Beer and Batman')

		rect = screen.get_rect()
		car = CarSprite('car.jpg', rect.center)
		#create a sprite group that contains just that image
		car_group = pygame.sprite.RenderPlain(car)

		pads = [BottleSprite((200, 200)), 
		BottleSprite((800, 200)),
		BottleSprite((200, 600)),
		BottleSprite((800, 600))
	    ]

		pad_group = pygame.sprite.RenderPlain(*pads)

		score = 300

		font = pygame.font.Font('freesansbold.ttf', 15) 
  

		while 1:
			deltat = clock.tick(500)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			#RENDERING
			screen.fill((255, 255, 255))

			# create a text suface object, 
			# on which text is drawn on it. 
			text = font.render('Score' + str(score), True, (0, 0, 0), (255, 255, 255)) 
  
			# create a rectangular object for the 
			# text surface object 
			textRect = text.get_rect()  
  
			# set the center of the rectangular object. 
			textRect.center = (120, 35) 


			screen.blit(text,textRect)

			car_group.update(deltat / 1000)

			#COLLISIONS
			#argument1 - sprite 
			#argument2 - sprite group
			#returns the sprites in argument2 that argument1 is colliding with
			collisions = pygame.sprite.spritecollide(car, pad_group, False)

			if len(collisions) > 0:
				score -= 1
				self.crash.play()


			pad_group.update(collisions)
			pad_group.draw(screen)
			car_group.draw(screen)
			pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1024, 768))
Game().main(screen)







