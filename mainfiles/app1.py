import pygame 
import time
import random
import sys

pygame.init()
display_width=800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake game')

white =(255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
block_size = 10

clock = pygame.time.Clock()

FPS=18
background_image = pygame.image.load("Desert.jpg")
icon = pygame.image.load("Desert.jpg")
pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 35)
lfont = pygame.font.SysFont(None, 80)

def Score(score):
	text = font.render("SCORE:"+str(score),True,green)
	gameDisplay.blit(text,[0,0])


def Intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					gameloop()
					intro = False
				if event.key == pygame.K_q:
					intro = False
					pygame.quit()
					quit()
		gameDisplay.blit(background_image, [0, 0])
		#gameDisplay.fill(white)
		message_to_screen("Welcome to snake game",green,-200,'L')
		message_to_screen("Press q for quit and p for play!                   ",green,-50,'s')
		pygame.display.update()


def text_objects(text,color,size):
	if size=="L":
		text_surface = lfont.render(text,True,color)
	else:
		text_surface = font.render(text,True,color)
	return text_surface, text_surface.get_rect()


def message_to_screen(msg,color,y_displace,size):
	textsurf,textrect = text_objects(msg, color,size)
	textrect.center=(display_width/2) , (display_height/2) + y_displace
	gameDisplay.blit(textsurf,textrect)

def snake_create(block_size,snakelist):
	for XY in snakelist:
		pygame.draw.rect(gameDisplay,black,[XY[0],XY[1],block_size,block_size])



def gameloop():
	gameExit = False
	gameOver = False
	lead_x = display_width/2
	lead_y = display_height/2
	snakelist = []
	snakelength = 1
	lead_x_change = 0
	lead_y_change = 0
	randappleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
	randappleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
	while not gameExit:
		while gameOver == True:
			gameDisplay.blit(background_image, [0, 0])
			#gameDisplay.fill(white)
			message_to_screen("Game over",red,-200,'L')
			message_to_screen("Press p for play again and q for quit!",green,-100,'s')
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = False
						gameExit = True
						
					if event.key == pygame.K_p:
						gameloop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					#print lead_x
					lead_y_change=0
					#lead_x -=10
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					#print lead_x
					lead_y_change = 0
					#lead_x += 10
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
					#lead_y -=10
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
					#lead_y += 10
		if lead_x<=0 or lead_y<=0 or lead_x>=display_width or lead_y>=display_height:
			gameOver = True
			
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		
		#gameDisplay.blit(background_image, [0, 0])
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay,red,[randappleX, randappleY, block_size, block_size])
		#print randappleX,randappleY,lead_x,lead_y
		snake_create(block_size,snakelist)
		Score(snakelength-1)
		pygame.display.update()
		
		snakehead=[]
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		if snakelength < len(snakelist):
			del(snakelist[0])
		
		if lead_x == randappleX and lead_y == randappleY:
			randappleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
			randappleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
			#print randappleY,randappleY + block_size,lead_y
			#print randappleX,randappleY,lead_x,lead_y
			snakelength += 1
		
		clock.tick(FPS)


	pygame.quit()
	quit()
Intro()



