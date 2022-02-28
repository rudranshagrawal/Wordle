import pygame, sys
pygame.init()#never forget this line
window=pygame.display.set_mode((100, 100))
font=pygame.font.SysFont('arial', 10)
text=font.render('A', True, (0, 0, 0))
rect=text.get_rect()
window.fill((255, 255, 255))
window.blit(text, rect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()