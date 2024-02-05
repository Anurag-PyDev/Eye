import pygame,sys
from pygame import *


def mainloop():
    while True:

        for eve in event.get():
            if eve.type == QUIT:
                quit()
                sys.exit()

        blits()
        
        display.flip()


class Eye:
    def __init__(self):
        self.x= 0
        self.y = 0
        self.rad = 0
        self.color = EYECOLOR
    
    def blit(self,surface,x,y,rad):
        self.x= x
        self.y = y
        self.rad = rad
        draw.circle(surface,self.color,(self.x,self.y),self.rad)




def blits():
    draw.rect(root,BGCOLOR,(0,0,root.get_width(),root.get_height()))
    e1.blit(root,0.3*root.get_width(),0.45*root.get_height(),0.2*root.get_height())
    e2.blit(root,0.7*root.get_width(),0.45*root.get_height(),0.2*root.get_height())



if __name__ == "__main__":


    pygame.init()
    root = display.set_mode((800,600),pygame.RESIZABLE)
    BGCOLOR = (255,190,175)
    EYECOLOR = (255,255,255)
    e1 = Eye()
    e2 = Eye()
    
    
    
    
    
    mainloop()
    
            