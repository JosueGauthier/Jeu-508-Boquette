import pygame
import winsound
pygame.init()


clock = pygame.time.Clock()
def pause():
    loop = 1
    #screen.fill((255, 255, 255))
    textp= 'PAUSED'
    fontp = pygame.font.SysFont('Consolas', 120,)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((wid/2)-195, (hei/2)-200, 500, 120))
    screen.blit(fontp.render(textp, True, (0, 0, 0)), ((wid/2)-195, (hei/2)-200))
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        
        

wid = 1000
hei = 1000

screen = pygame.display.set_mode((wid, hei))

joueur = 1
j= 1

counter1 = 10
text1= '10'.rjust(3)

counter2 = 0
text2= ''.rjust(3)

pygame.time.set_timer(pygame.USEREVENT, 100)
font1 = pygame.font.SysFont('Consolas', 60,)
font2 = pygame.font.SysFont('Consolas', 60,)


chiffre = 4

pos4 = "gauche"
pos3 = "droite"
pos2 = "gauche"
pos1 = "droite"

sos4 = pos4
sos3 = pos3
sos2 = pos2
sos1 = pos1

dec4 = -74
dec3 = 5
dec2 =-74
dec1 = 5



start = True
while start:

    screen.fill((255, 255, 255))
    textp= 'Pret ? '
    fontp = pygame.font.SysFont('Consolas', 120,)
    screen.blit(fontp.render(textp, True, (0, 0, 0)), ((wid/2)-195, (hei/2)-200))
    pygame.display.flip()

    
    for e in pygame.event.get():

        if e.type == pygame.QUIT: 
            start = False

        if e.type == pygame.KEYDOWN: 
            if e.key == pygame.K_SPACE:

                screen.fill((255, 255, 255))
                
                pygame.draw.rect(screen, (230,230, 0), pygame.Rect(wid/2 +dec4,20, 70, 200))
                pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                fontt = pygame.font.SysFont('Consolas', 60,)
                screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))

                
                run = True
                while run:
                    
                    for e in pygame.event.get():
                        if e.type == pygame.USEREVENT:

                            if joueur == 1 :

                                counter1 -= 0.1
                                
                                if counter1 > 0 : 
                                    
                                    c1 = "{:.2f}".format(counter1)
                                    text1 = str(c1).rjust(3) 
                                                              
                                else :

                                    if chiffre > 1 : 

                                        chiffre = chiffre -1

                                        if chiffre == 3 : 
                                            counter2 = 7
                                            counter1 =0
                                            joueur = 2
                                            j = 2

                                            screen.fill((255, 255, 255))

                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  
                                        

                                        if chiffre ==2 : 
                                            counter1 = 5 
                                            counter2 =0
                                            joueur =1
                                            j=1

                                            screen.fill((255, 255, 255))

                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  
                                           
                                        

                                        if chiffre ==1 : 
                                            counter1 = 0 
                                            counter2 = 3
                                            joueur =2
                                            j=2

                                            screen.fill((255, 255, 255))
                                            
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  
                                        

                                    else: 

                                        text1= 'boom!'

                                        frequency = 400  # Set Frequency To 2500 Hertz
                                        duration = 1000  # Set Duration To 1000 ms == 1 second
                                        winsound.Beep(frequency, duration)
                                        run = False
                                        start = False


                                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0.75*(hei), wid/2, 0.25*hei))
                            
                            else : 
                                pygame.draw.rect(screen, (255,0, 0), pygame.Rect(0, 0.75*(hei), wid/2, 0.25*hei))
                        
                        if e.type == pygame.USEREVENT:

                            if joueur == 2 :

                                counter2 -= 0.1
                                
                                if counter2 > 0 :

                                    c2 = "{:.2f}".format(counter2)
                                    text2 = str(c2).rjust(3)

                                
                                else :

                                    if chiffre > 1 : 

                                        chiffre = chiffre -1
                                        if chiffre == 3 : 
                                            counter2 = 7
                                            counter1 =0
                                            joueur = 2
                                            j=2

                                            screen.fill((255, 255, 255))

                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  


                                        if chiffre ==2 : 
                                            counter1 = 5 
                                            counter2 =0
                                            joueur = 1
                                            j=1

                                            screen.fill((255, 255, 255))

                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  

                                        if chiffre ==1 : 
                                            counter1 = 0 
                                            counter2 = 3
                                            joueur = 2
                                            j=2

                                            screen.fill((255, 255, 255))

                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                            pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                            pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                            screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                            screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                            screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                            screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                            pygame.display.flip()  
                                                                                                
                                    else : 
                                        text2= 'boom!'
                                        
                                        frequency = 400  # Set Frequency To 2500 Hertz
                                        duration = 1000  # Set Duration To 1000 ms == 1 second
                                        winsound.Beep(frequency, duration)

                                        run = False
                                        start = False


                                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(wid/2, 0.75*(hei), wid/2, 0.25*hei))
                            else :
                                pygame.draw.rect(screen, (255,0, 0), pygame.Rect(wid/2, 0.75*(hei), wid/2, 0.25*hei))  


                        if e.type == pygame.QUIT: 
                            run = False
                            start = False


                        if e.type == pygame.KEYDOWN: 
                            if e.key == pygame.K_SPACE:

                            
                                pause()

                                if chiffre == 4 :

                                    if pos4 == "gauche" :

                                        
                                        dec4 = 5
                                        sos4 = "droite"

                                        j = j+1
                                        
                                        temps = counter1

                                        counter1 = 0

                                        counter2 = temps + counter2
                                        
                                        
                                        screen.fill((255, 255, 255))
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec4,20, 70, 200))

                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))



                                        pygame.display.flip()
                                    

                                    if pos4 == "droite" :
                                        
                                        sos4 = "gauche"

                                        dec4 = -74

                                        temps = counter2

                                        counter2 = 0

                                        counter1 = temps + counter1

                                        j = j+1
                                        
                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()                           
                                    

                                if chiffre == 3 : 

                                    if pos3 == "gauche" : 

                                        dec3 =5
                                        j = j+1

                                        temps = counter1

                                        counter1 = 0

                                        counter2 = temps + counter2


                                        sos3 = "droite"

                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()  
                                        


                                    if pos3 == "droite" :

                                        temps = counter2

                                        counter2 = 0

                                        counter1 = temps + counter1


                                        dec3 = -74 
                                        sos3 = "gauche"

                                        j = j+1

                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()  

                                
                                if chiffre == 2 : 

                                    if pos2 == "gauche" :

                                        temps = counter1

                                        counter1 = 0

                                        counter2 = temps + counter2 

                                        dec2 =5
                                        sos2 = "droite"

                                        j = j+1
                                        
                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()  
                                        
                                    if pos2 == "droite" :

                                        temps = counter2

                                        counter2 = 0

                                        counter1 = temps + counter1 

                                        dec2=-74

                                        j = j+1

                                        sos2 = "gauche"
                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (0,100, 200), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()  

                                if chiffre == 1 : 

                                    if pos1 == "gauche" : 

                                        temps = counter1

                                        counter1 = 0

                                        counter2 = temps + counter2

                                        sos1 = "droite"

                                        j = j+1

                                        dec1=5
                                        
                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()                                          

                                    if pos1 == "droite" :

                                        temps = counter2

                                        counter2 = 0

                                        counter1 = temps + counter1 

                                        sos1 = "gauche"

                                        j = j+1

                                        dec1=-74
                                        screen.fill((255, 255, 255))

                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec4,20, 70, 200))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec3,230, 70, 150))
                                        pygame.draw.rect(screen, (0,100,200), pygame.Rect(wid/2 +dec2,390, 70, 120)) 
                                        pygame.draw.rect(screen, (230,230,0), pygame.Rect(wid/2 +dec1,520, 70, 100))

                                        screen.blit(fontt.render("4", True, (0, 0, 0)), ((wid/2 +dec4 +20,80)))
                                        screen.blit(fontt.render("3", True, (0, 0, 0)), ((wid/2 +dec3 +20,260)))
                                        screen.blit(fontt.render("2", True, (0, 0, 0)), ((wid/2 +dec2 +20,410)))
                                        screen.blit(fontt.render("1", True, (0, 0, 0)), ((wid/2 +dec1 +20,550)))


                                        pygame.display.flip()                                          

                            
                    pos4 = sos4
                    pos3 = sos3
                    pos2 = sos2
                    pos1 = sos1

                    
                    if (j % 2) == 0:
                        joueur = 2
                    else:
                        joueur = 1

                    
                    if joueur == 1 : 
                        screen.blit(font1.render(text1, True, (0, 0, 0)), ((wid/4)-75, 9*(hei/10)-50))
                        screen.blit(font2.render("", True, (0, 0, 0)), (((3*wid)/4)-75, 9*(hei/10)-50))
                    
                    if joueur == 2 : 
                        screen.blit(font1.render("", True, (0, 0, 0)), ((wid/4)-75, 9*(hei/10)-50))
                        screen.blit(font2.render(text2, True, (0, 0, 0)), (((3*wid)/4)-75, 9*(hei/10)-50))



                    

                    pygame.draw.line(screen, (0, 0, 0), (wid/2,0), (wid/2,hei),10)
                    pygame.draw.line(screen, (0, 0, 0), (0,0.75*(hei)), (wid,0.75*(hei)),10)
                    
                    pygame.display.flip()
                    clock.tick(60)

                




