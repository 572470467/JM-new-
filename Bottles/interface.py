import threading
import time
import os
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
Red=[255,0,0]
Gray=[169,169,169]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=((width-67)/3-400)/2
button_text=["begin","begin","begin","begin","begin","begin","begin","begin","begin"]
line=['http://192.168.10.117:5000/mixer/000','http://192.168.10.117:5000/mixer/100','http://192.168.10.117:5000/mixer/200','http://192.168.10.117:5000/mixer/300','http://192.168.10.117:5000/mixer/400','http://192.168.10.117:5000/mixer/500','http://192.168.10.117:5000/mixer/600','http://192.168.10.117:5000/mixer/700','http://192.168.10.117:5000/mixer/800']
line0=['http://192.168.10.108:5000/carrier/moveto/0','http://192.168.10.108:5000/carrier/moveto/1','http://192.168.10.108:5000/carrier/moveto/2','http://192.168.10.108:5000/carrier/moveto/3','http://192.168.10.108:5000/carrier/moveto/4']
CGQ=[[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]]
list=['[0,1,1,1,1]','[1,0,1,1,1]','[1,1,0,1,1]','[1,1,1,0,1]','[1,1,1,1,0]']
color=[Green,Green,Green,Green,Green,Green,Green,Green,Green]
color0=[Green,Green,Green,Green,Green]
button_text0="manual:"
button_text1=["station0","station1","station2","station3","station4"]
Num=['0','1','2','3','4']
B0=[size+32,size+102,size+172,size+242,size+312]
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67+(width-67)/3*2,27)
screen = pygame.display.set_mode((int((width-67)/3),height))
screen.fill(Brack)
text=["Power preparation:","Device reset:","Power tank open:","Power tank close:","Circular screen:","Stop and reset:","Grinding machine open:","Grinding machine close:","Order to test:"]
text_0=pygame.font.SysFont("arial",24)
text_1=pygame.font.SysFont("arial",20)
text_2=pygame.font.SysFont("arial",17)
text_fmt0=text_0.render("Operation  Interface",2,White)
screen.blit(text_fmt0,(size+106,10))
pygame.display.update()
def Process(num,x,y,button_text,color):
    text_fmt1=text_1.render(text[num],1,White)
    screen.blit(text_fmt1,(x-127,y))
    pygame.draw.rect(screen,color,[x+100,y,65,28],0)
    button=text_1.render(button_text,1,Brack)
    screen.blit(button,(x+113,y+3))
    pygame.display.update()
def Station(num,x,y,a,color0):
    pygame.draw.rect(screen,color0,[x,y,65,28],0)
    button=text_2.render(button_text1[num],1,Brack)
    screen.blit(button,(x+2,y+4))
    img=pygame.image.load('cgq.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(x,y+80))
    button=text_0.render((Num[a]),1,White)
    screen.blit(button,(x+20,688))
    pygame.display.update()
def State_A():
    response=urllib.request.urlopen(line[num])
    button_text[num]="begin"
    color[num]=Green
def State_B():
    for i in range(6):
        response=urllib.request.urlopen(line[i])
        button_text[i]="begin"
        button_text[i+1]="end"
    response=urllib.request.urlopen(line[6])
    button_text[6]="begin"
def State_C(num):
    pygame.draw.rect(screen,Brack,[size,593,400,50],0)
    pygame.draw.rect(screen,Brack,[size,687,400,25],0)
    img=pygame.image.load('car.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(B0[num],593))
    pygame.display.update()
def State_D():
    response3=urllib.request.urlopen(line0[num])
    color0[num]=Green
def Manual(num):
    threads=[]
    threads.append(threading.Thread(target=State_A))
    for t in threads:
        t.start()
def Automatic():
    threads=[]
    threads.append(threading.Thread(target=State_B))
    for t in threads:
        t.start()
def Car(num):
    threads=[]
    threads.append(threading.Thread(target=State_D))
    for t in threads:
        t.start()
def GZ():
    button=text_0.render(('Prompt:fault,manual intervention is needed!'),1,Red)
    screen.blit(button,(size,720))        
if __name__ == '__main__':
    while True:
        pygame.draw.rect(screen,Brack,[size,720,460,30],0)        
        pygame.draw.rect(screen,Brack,[size+70,482,100,28],0)
        pygame.draw.rect(screen,Green,[size+177,484,62,25],0)
        button1=text_1.render("switch",1,Brack)
        screen.blit(button1,(size+181,486))
        button=text_1.render(button_text0,1,White)
        screen.blit(button,(size+70,486))
        B=[[0,size+187,66,button_text[0],color[0]],[1,size+187,112,button_text[1],color[1]],[2,size+187,158,button_text[2],color[2]],[3,size+187,204,button_text[3],color[3]],[4,size+187,250,button_text[4],color[4]],[5,size+187,296,button_text[5],color[5]],[6,size+187,342,button_text[6],color[6]],[7,size+187,388,button_text[7],color[7]],[8,size+187,434,button_text[8],color[8]]]
        for i in B:
            Process(i[0],i[1],i[2],i[3],i[4])
        if color0==[Green,Green,Green,Green,Green]:
            if button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"]:
                response2=urllib.request.urlopen('http://192.168.10.108:5000/carrier/status')
                html2=response2.read().decode()
            elif button_text!=["begin","begin","begin","begin","begin","begin","begin","begin","begin"]:
                html2=str({'pos':0,'sensors':[0,1,1,1,1]})
            if html2[7:9]!='-1':
                C=[[0,size+32,558,int(html2[23]),color0[0]],[1,size+102,558,int(html2[26]),color0[1]],[2,size+172,558,int(html2[29]),color0[2]],[3,size+242,558,int(html2[32]),color0[3]],[4,size+312,558,int(html2[35]),color0[4]]]
                State_C(int(html2[8]))
                if html2[22:37] not in list:
                    GZ()                
            elif html2[7:9]=='-1':
                C=[[0,size+32,558,int(html2[24]),color0[0]],[1,size+102,558,int(html2[27]),color0[1]],[2,size+172,558,int(html2[30]),color0[2]],[3,size+242,558,int(html2[33]),color0[3]],[4,size+312,558,int(html2[36]),color0[4]]]
                pygame.draw.rect(screen,Brack,[size,593,400,50],0)
                pygame.draw.rect(screen,Brack,[size,687,400,25],0)      
                if html2[23:38]!='[1,1,1,1,1]':
                    GZ()                
            for v in C:
                Station(v[0],v[1],v[2],v[3],v[4])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index==0:
                            if size+177<=pos[0]<=size+242 and 484<=pos[1]<=509:
                                if button_text0=="self-motion:" and button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"]:
                                    button_text0="manual:"
                                    color=[Green,Green,Green,Green,Green,Green,Green,Green,Green]
                                elif button_text0=="manual:" and button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"]:
                                    button_text0="self-motion:"
                                    button_text[0]="end"
                                    Automatic()
                                    color=[Gray,Gray,Gray,Gray,Gray,Gray,Gray,Gray,Gray]
                            for i in B:
                                if i[1]+100<=pos[0]<=i[1]+165 and i[2]<=pos[1]<=i[2]+28:
                                    if button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"] and button_text0=="manual:":
                                        color[i[0]]=Red
                                        num=i[0]
                                        button_text[i[0]]="end"
                                        if button_text[i[0]]=="end":
                                            Manual(num)
                            for v in C:
                                if v[1]<=pos[0]<=v[1]+65 and v[2]<=pos[1]<=v[2]+28 and color0==[Green,Green,Green,Green,Green]:
                                    color0[v[0]]=Red
                                    if color0[v[0]]==Red:
                                        num=v[0]
                                        State_C(num)
                                        Car(num)
                                        C=[[0,size+32,558,CGQ[v[0]][0],color0[0]],[1,size+102,558,CGQ[v[0]][1],color0[1]],[2,size+172,558,CGQ[v[0]][2],color0[2]],[3,size+242,558,CGQ[v[0]][3],color0[3]],[4,size+312,558,CGQ[v[0]][4],color0[4]]]
                                        for f in C:
                                            Station(f[0],f[1],f[2],f[3],f[4])
    pygame.display.update()
