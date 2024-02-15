import pygame,sys
from pygame import *
import math as mathe

def mainloop():
    while True:

        for eve in event.get():
            if eve.type == QUIT or eve.type == KEYDOWN:
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

    def blit_ellipse(self,surface,x,y,w,h,angle):
        self.x= x
        self.y = y
        self.w = w
        self.angle = angle
        self.h = h
        draw_ellipse_angle(surface,self.color,(self.x,self.y,self.w,self.h),self.angle)


def blits():
    ''' Contains all the blit calls '''

    draw.rect(root,BGCOLOR,(0,0,root.get_width(),root.get_height()))

    #  Tested with cicular eyes
    # e1.blit(root,0.3*root.get_width(),0.45*root.get_height(),0.2*root.get_height())
    # e2.blit(root,0.7*root.get_width(),0.45*root.get_height(),0.2*root.get_height())

    sW = root.get_width()
    sH = root.get_height()
    # e1.blit_ellipse(root,e1PosFacX*sW,e1PosFacY*sH,e1SizeFacW*sH,e1SizeFacH*sH,30)
    # e1.blit_ellipse(root,e2PosFacX*sW,e2PosFacY*sH,e2SizeFacW*sH,e2SizeFacH*sH,-30)
    a= 400
    x,y=20,20
    surf = Surface((1.5*a,1.5*a),SRCALPHA)
    arc(surf,EYECOLOR,(x+20,y+150,a,0.2*a),0,1.1*mathe.pi,1.9*mathe.pi,10)
    arc(surf,EYECOLOR,(x+0,y+5,0.2*a,0.5*a),0,0.75*mathe.pi,1.47*mathe.pi,9)
    arc(surf,EYECOLOR,(x-12,y+0,1.1*a,0.6*a),-15,-0.08*mathe.pi,0.93*mathe.pi,9)

    surf2 = transform.flip(surf,1,0)
    arc(surf,(200,202,0),(x+100,y+50,0.4*a,0.4*a),0,0,2*mathe.pi,200)
    root.blit(surf,(0,0))
    root.blit(surf2,(800,0))


    

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def arc(surface, color, rect, angle, start,end,width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.arc(shape_surf, color, (0, 0, *target_rect.size),start,end, width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))


if __name__ == "__main__":


    pygame.init()
    root = display.set_mode((0,0),pygame.FULLSCREEN)
    BGCOLOR = (0,0,0)
    EYECOLOR = (255,255,255)
    
    e1 = Eye()
    e2 = Eye()
    
    e1PosFacX = 0.2
    e1PosFacY = 0.3
    e1SizeFacW = 0.4
    e1SizeFacH = 0.45

    e2PosFacX = 0.6
    e2PosFacY = 0.3
    e2SizeFacW = 0.4
    e2SizeFacH = 0.45
    
    
    
    
    mainloop()
    
            