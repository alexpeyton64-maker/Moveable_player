# example file showing a circle moving on screen
import pygame, os


# pygame setup
pygame.init()
screen = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
image = pygame.image.load('slime.png')
scaled_image = pygame.transform.scale(image, (500, 500))
rect = image.get_rect()

while running:
    # poll for events
    # pygame.Quit means the user clicked the x to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill('purple')

    #draws circle
    # pygame.draw.circle(screen, "red", player_pos, 40)
  
   
    screen.blit(image,rect)

    #creates player movement based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        rect.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            rect.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            rect.x-= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            rect.x += 300 * dt

    #flip() the display to put your work on screen
    pygame.display.flip()

    #limits fps to 60
    dt = clock.tick(60) / 1000

pygame.quit()
