import pygame 
import sys
from pygame.locals import *
from game_boardv2 import game_board

def main_menu():
	# initializing the constructor 
	pygame.init() 

	# set screen size
	screen = pygame.display.set_mode((800, 800))
	width = screen.get_width() 
	height = screen.get_height() 
	pygame.display.set_caption("Morgan's Connect4")

	# player name input areas
	p1_input_rect = pygame.Rect(200, 200, 140, 32)
	p2_input_rect = pygame.Rect(400, 200, 140, 32)
	title_banner_rect = pygame.Rect(20, 20, width-40, height/2-40)
	start_button_rect = pygame.Rect(10,height/2,width-20,40)

	# colours
	white = (255,255,255)
	blue = (0, 0, 255)
	color_light = (170,170,170) 
	color_dark = (100,100,100) 
	color_active = pygame.Color('lightskyblue3') 
	color_passive = pygame.Color('chartreuse4')

	# fonts for 'start' button, title and input boxes
	smallfont = pygame.font.SysFont('Corbel',35)
	bigfont = pygame.font.SysFont('Corbel',70)
	base_font = pygame.font.Font(None, 32)

	# texts
	welcome_text = bigfont.render('Welcome to Connect4!', True, white)
	start_text = smallfont.render('Start game!' , True , white) 
	p1_name = ''
	p2_name = ''

	p1_active = False
	p2_active = False

	# game loop
	while True: 
		# check the event queue
		for event in pygame.event.get(): 
			# exit game
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()

			# select player name input boxes
			if event.type == pygame.MOUSEBUTTONDOWN: 
				if p1_input_rect.collidepoint(event.pos): 
					p1_active = True
				else: 
					p1_active = False
			if event.type == pygame.MOUSEBUTTONDOWN: 
				if p2_input_rect.collidepoint(event.pos): 
					p2_active = True
				else: 
					p2_active = False

			# enter text into player name input boxes
			if p1_active and event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_BACKSPACE: 
					p1_name = p1_name[:-1] 
				else: 
					p1_name += event.unicode
			if p2_active and event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_BACKSPACE: 
					p2_name = p2_name[:-1] 
				else: 
					p2_name += event.unicode

			# exits the game (could be redundant)
			if event.type == pygame.QUIT: 
				pygame.quit() 
			
			# starts the game
			if event.type == pygame.MOUSEBUTTONDOWN: 				
				if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
					game_board(width, height, p1_name, p2_name)
					pygame.quit() 

		screen.fill((0, 0, 0)) 
		
		# indicates which input box is active
		p1_color = color_active if p1_active else color_passive
		p2_color = color_active if p2_active else color_passive
		
		# gets mouse position
		mouse = pygame.mouse.get_pos() 
		
		# draws title banner, input boxes, and start button
		pygame.draw.rect(screen, blue, title_banner_rect)
		pygame.draw.rect(screen, p1_color, p1_input_rect) 
		pygame.draw.rect(screen, p2_color, p2_input_rect) 
		if start_button_rect.collidepoint(mouse): 
			pygame.draw.rect(screen, color_light, start_button_rect)
		else: 
			pygame.draw.rect(screen, color_dark, start_button_rect)

		# creates text surfaces for inputted names
		p1_text_surface = base_font.render(p1_name, True, (255, 255, 255)) 
		p2_text_surface = base_font.render(p2_name, True, (255, 255, 255)) 
		
		# adds text surfaces onto screen
		screen.blit(p1_text_surface, (p1_input_rect.x+5, p1_input_rect.y+5))
		screen.blit(p2_text_surface, (p2_input_rect.x+5, p2_input_rect.y+5)) 
		screen.blit(welcome_text, (width/2-260, 100))
		screen.blit(start_text, (width/2-67,height/2+8)) 
		
		# updates the frames of the game 
		pygame.display.update() 

main_menu()