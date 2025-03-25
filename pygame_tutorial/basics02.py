import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Morgan's Image")

# image = pygame.image.load("file_name_here")
exit = False

while not exit:
    canvas.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, red, pygame.Rect(30, 30, 60, 60))        
    pygame.display.update()