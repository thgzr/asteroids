import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():   
	black = (0, 0, 0)  # RGB tuple for black color
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player_x = SCREEN_WIDTH / 2
	player_y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)

	my_player = Player(player_x, player_y)

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable, )

	my_asteroid_field = AsteroidField()
  
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return		
		screen.fill(black)
		updatable.update(dt)

		for asteroid in asteroids:
			for shot in shots:
				if shot.detect_collision(asteroid):
					asteroid.split(dt, asteroids)
					pygame.sprite.Sprite.kill(shot)

			if my_player.detect_collision(asteroid):
				print("Game over")
				sys.exit()

		for item_to_draw in drawable:
			item_to_draw.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60) / 1000)
		
        

if __name__ == "__main__":
    main()
