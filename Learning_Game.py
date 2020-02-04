import pygame
from pygame.locals import*
pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Kemi Fældningsreaktioner")
#laver billederne
ag = pygame.image.load("AgNO3.png").convert()
al = pygame.image.load("Al(SO4)3.png").convert()
ba = pygame.image.load("BaCl2.png").convert()
ca = pygame.image.load("CaCl2.png").convert()
k3 = pygame.image.load("K3PO4.png").convert()
ki = pygame.image.load("KI.png").convert()
ko = pygame.image.load("Kobbersulfat.png").convert()
na = pygame.image.load("NaCl.png").convert()

#vælger font til tekst
the_font = pygame.font.SysFont("Comic_Sans", 20)
nd_font = pygame.font.SysFont("Comic_Sans", 75)


#laver farver klar til knapperne
red = (255, 0, 0)
green = (0, 255, 0)


#tekst til knapperne
ag_tekst = the_font.render("AgNO3", True, (255, 255, 255))
al_tekst = the_font.render("Al(SO4)3", True, (255, 255, 255))
ba_tekst = the_font.render("BaCl2", True, (255, 255, 255))
ca_tekst = the_font.render("CaCl2", True, (255, 255, 255))
k3_tekst = the_font.render("K3PO4", True, (255, 255, 255))
ki_tekst = the_font.render("KI", True, (255, 255, 255))
cu_tekst = the_font.render("CuSO4", True, (255, 255, 255))
na_tekst = the_font.render("NaCl", True, (255, 255, 255))

#laver tekst til stor knap
prod_knap_tekst = nd_font.render("Bland!", True, (255, 255, 255))


#laver en funktion til knapperne
def button(tekst,x,y,wid,hei,ac,ic,tx,ty):
    if x+wid > mouse[0] > x and y+hei > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, wid, hei))
    else:
        pygame.draw.rect(window, ic, (x, y, wid, hei))
    window.blit(tekst, (tx,ty))



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

        #henter musens position
    mouse = pygame.mouse.get_pos()
    
    #laver knapper til række 1
    button(ag_tekst,10,80,60,30,green,red,15,86)

    button(al_tekst,110,80,60,30,green,red,115,86)

    button(ba_tekst,210,80,60,30,green,red,215,86)

    button(ca_tekst,310,80,60,30,green,red,315,86)

    button(k3_tekst,410,80,60,30,green,red,415,86)

    button(ki_tekst,510,80,60,30,green,red,515,86)

    button(cu_tekst,610,80,60,30,green,red,615,86)
    
    button(na_tekst,710,80,60,30,green,red,715,86)


    

    #laver knapper til række 2
    if 10+60 > mouse[0] > 10 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (10, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (10, 230, 60, 30))

    if 110+60 > mouse[0] > 110 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (110, 230, 60, 30))
    else:    
        pygame.draw.rect(window, red, (110, 230, 60, 30))

    if 210+60 > mouse[0] >210 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (210, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (210, 230, 60, 30))

    if 310+60 > mouse[0] > 310 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (310, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (310, 230, 60, 30))

    if 410+60 > mouse[0] > 410 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (410, 230, 60, 30))
    else:    
        pygame.draw.rect(window, red, (410, 230, 60, 30))

    if 510+60 > mouse[0] > 510 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (510, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (510, 230, 60, 30))

    if 610+60 > mouse[0] > 610 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (610, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (610, 230, 60, 30))

    if 710+60 > mouse[0] > 710 and 230+30 > mouse[1] > 230:
        pygame.draw.rect(window, green, (710, 230, 60, 30))
    else:
        pygame.draw.rect(window, red, (710, 230, 60, 30))

    #Laver blande knappen
    pygame.draw.rect(window, (220, 220, 220), (350, 370, 300, 150))

    window.blit(ag, (0,0)) #sætter billede ind i række 1
    window.blit(al, (100, 0))
    window.blit(ba, (200, 0))
    window.blit(ca, (300, 0))
    window.blit(k3, (400, 0))
    window.blit(ki, (500, 0))
    window.blit(ko, (600, 0))
    window.blit(na, (700, 0))

    window.blit(ag, (0,150)) #sætter billede ind i række 2
    window.blit(al, (100, 150))
    window.blit(ba, (200, 150))
    window.blit(ca, (300, 150))
    window.blit(k3, (400, 150))
    window.blit(ki, (500, 150))
    window.blit(ko, (600, 150))
    window.blit(na, (700, 150))


    #sætter tekst ind i den store grå kasse
    window.blit(prod_knap_tekst, (420, 425))
        

    #tekst sættes ind i øverste række
    window.blit(cu_tekst, (615, 86))
    window.blit(na_tekst, (715, 86))

    #tekst sættes ind i nederste række
    window.blit(ag_tekst, (15, 236))
    window.blit(al_tekst, (115, 236))
    window.blit(ba_tekst, (215, 236))
    window.blit(ca_tekst, (315, 236))
    window.blit(k3_tekst, (415, 236))
    window.blit(ki_tekst, (515, 236))
    window.blit(cu_tekst, (615, 236))
    window.blit(na_tekst, (715, 236))

    pygame.display.update()


pygame.quit()
