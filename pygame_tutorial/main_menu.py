import pygame 
import sys
from pygame.locals import *
from game_board import game_board

def main_menu():
	# initializing the constructor 
	pygame.init() 

	screen = pygame.display.set_mode((800, 800))

	pygame.display.set_caption("Morgan's Connect4")

	white = (255,255,255)
	blue = (0, 0, 255)
	color_light = (170,170,170) 
	color_dark = (100,100,100) 

	width = screen.get_width() 
	height = screen.get_height() 

	smallfont = pygame.font.SysFont('Corbel',35)
	welcome_text = smallfont.render('Welcome to Connect4!', True, white)
	start_text = smallfont.render('Start game!' , True , white) 

	while True: 
		
		for event in pygame.event.get(): 
			if event.type == KEYDOWN:
				if event.key == K_BACKSPACE:
					pygame.quit()

			if event.type == pygame.QUIT: 
				pygame.quit() 
				
			if event.type == pygame.MOUSEBUTTONDOWN: 				
				if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
					game_board(width, height)
					pygame.quit() 

		# fills the screen with a color 
		screen.fill((0, 0, 0)) 
		
		# stores the (x,y) coordinates into the variable as a tuple 
		
		pygame.draw.rect(screen, blue, [20, 20, width-40, height/2-40])
		
		mouse = pygame.mouse.get_pos() 
		
		# if mouse is hovered on a button it changes to lighter shade 
		if 10 <= mouse[0] <= width-20 and height/2 <= mouse[1] <= height/2+40: 
			pygame.draw.rect(screen,color_light,[10,height/2,width-20,40])
		else: 
			pygame.draw.rect(screen,color_dark,[10,height/2,width-20,40])
		
		# superimposing the text onto our button 
		screen.blit(welcome_text, (50, 50))
		screen.blit(start_text, (width/2-67,height/2+8)) 
		
		# updates the frames of the game 
		pygame.display.update() 

main_menu()