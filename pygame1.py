
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
text = pygame.font.Font(None, 37).render("Hello World!", True, pygame.Color('Yellow'))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(text, (250, 250))
    pygame.display.flip()