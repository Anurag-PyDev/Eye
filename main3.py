import pygame,sys,random
from pygame import *
import math as mathe

def mainloop():

    while True:

        clock.tick(60)
        for eve in event.get():
            if eve.type == QUIT :
                quit()
                sys.exit()
            if eve.type == KEYDOWN and eve.key == K_BACKSPACE:
                # e1.angle+=5
                exit()
        look()
        blits()
        
        display.flip()


class Eye:
    def __init__(self):
        self.x= 250
        self.y = 140
        self.rad = 0
        self.color = EYECOLOR
        self.w = eyeW
        self.angle = 0
        self.h = eyeH
    
    def blit(self,surface,rad):
        self.rad = rad
        draw.circle(surface,self.color,(self.x,self.y),self.rad)

    def blit_ellipse(self,surface,w,h):
        
        self.w = w
        self.h = h
        draw_ellipse_angle(surface,self.color,(self.x,self.y,self.w,self.h),self.angle)


def blits():
    ''' Contains all the blit calls '''

    draw.rect(root,BGCOLOR,(0,0,root.get_width(),root.get_height()))

    sW = root.get_width()
    sH = root.get_height()
    surfW =400+150*2
    surfH = 280+100*2
    
    surf = Surface((surfW,surfH),SRCALPHA)
    surf2 = Surface((surfW,surfH),SRCALPHA)

    draw.ellipse(surf,(255,230,220),(0,-15,surfW,surfH))
    draw.ellipse(surf2,(255,230,220),(0,-15,surfW,surfH))

    e1.blit_ellipse(surf,e1.w,e1.h)
    e2.blit_ellipse(surf2,e2.w,e2.h)
    # e1.blit(surf,100)
    # e2.blit(surf2,100)

    width = 100
    multiplier = 1.6
    draw_ellipse_angle(surf,BGCOLOR,(0-width,0-width,surfW+width*multiplier,surfH+width*multiplier),0,width)
    draw_ellipse_angle(surf2,BGCOLOR,(0-width,0-width,surfW+width*multiplier,surfH+width*multiplier),0,width)

    root.blit(surf,(0.03*sW,0.2*sH))
    root.blit(surf2,(0.53*sW,0.2*sH))


def look():
    squishX = 10
    squishY = 6
    stepX = 25
    stepY = 14
    keys = key.get_pressed()
    if e1.x>500+5*squishX:
        e1.x=500+5*squishX
        e1.w=eyeW-10*squishX
    elif e1.x<0:
        e1.x=0
        e1.w=eyeW-10*squishX

    if keys[K_LEFT]:
        if 0<=e1.x<250:
            e1.x-=stepX
            e1.w-=squishX   
        elif 250<=e1.x<=500+10*squishX:
            e1.x-=stepX+squishX
            e1.w+=squishX
    if keys[K_RIGHT]:
        if 0<=e1.x<250:
            e1.x+=stepX
            e1.w+=squishX  

        elif 250<=e1.x<=500+10*squishX:
            e1.x+=stepX+squishX
            e1.w-=squishX
    
    if e1.y>280:
        e1.y=280
        e1.h=eyeH-10*squishY
    elif e1.y<0:
        e1.y=0
        e1.h=eyeH-10*squishY

    if keys[K_UP]:
        if 0<=e1.y<140:
            e1.y-=stepY
            e1.h-=squishY
        elif 140<=e1.y<=280+10*squishY:
            e1.y-=stepY+squishY
            e1.h+=squishY
    if keys[K_DOWN]:
        if 0<=e1.y<140:
            e1.y+=stepY
            e1.h+=squishY
        elif 140<=e1.y<=280+10*squishY:
            e1.y+=stepY+squishY
            e1.h-=squishY
    

    # for e2
    if e2.x>500+5*squishX:
        e2.x=500+5*squishX
        e2.w=eyeW-10*squishX
    elif e2.x<0:
        e2.x=0
        e2.w=eyeW-10*squishX

    if keys[K_LEFT]:
        if 0<=e2.x<250:
            e2.x-=stepX
            e2.w-=squishX   
        elif 250<=e2.x<=500+10*squishX:
            e2.x-=stepX+squishX
            e2.w+=squishX
    if keys[K_RIGHT]:
        if 0<=e2.x<250:
            e2.x+=stepX
            e2.w+=squishX  

        elif 250<=e2.x<=500+10*squishX:
            e2.x+=stepX+squishX
            e2.w-=squishX
    
    if e2.y>280:
        e2.y=280
        e2.h=eyeH-10*squishY
    elif e2.y<0:
        e2.y=0
        e2.h=eyeH-10*squishY

    if keys[K_UP]:
        if 0<=e2.y<140:
            e2.y-=stepY
            e2.h-=squishY
        elif 140<=e2.y<=280+10*squishY:
            e2.y-=stepY+squishY
            e2.h+=squishY
    if keys[K_DOWN]:
        if 0<=e2.y<140:
            e2.y+=stepY
            e2.h+=squishY
        elif 140<=e2.y<=280+10*squishY:
            e2.y+=stepY+squishY
            e2.h-=squishY
  
    

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
    BGCOLOR = (220,180,180)
    EYECOLOR = (0,0,0)
    clock = time.Clock()
    
    eyeW=200
    eyeH=200

    e1 = Eye()
    e2 = Eye()
    
    
    
    
    mainloop()
    
            