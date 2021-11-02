#Not finish yet
import pygame
pygame.init()

Screen_w = 300
Screen_h = 300

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((Screen_w, Screen_h))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = Screen_w/2
lead_y = Screen_h/2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      gameExit = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        lead_x_change = -10
        lead_y_change = 0
      elif event.key == pygame.K_RIGHT:
        lead_x_change = 10
        lead_y_change = 0

      elif event.key == pygame.K_UP:
        lead_x_change = 0
        lead_y_change = -10
      elif event.key == pygame.K_DOWN:
        lead_x_change = 0
        lead_y_change = 10

#Click start
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
      if mouse_pos[0] < lead_x:
        lead_x -= 10
      else:
        lead_x += 10
      if mouse_pos[0] < lead_y:
        lead_y -= 10
      else:
        lead_y += 10
#Click end        

  lead_x += lead_x_change
  lead_y += lead_y_change
  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
  pygame.display.update()

  clock.tick(30)

pygame.quit()
quit