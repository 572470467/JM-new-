import threading
import time
import os
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Black=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
Red=[255,0,0]
Gray=[169,169,169]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=((width-67)/3-400)/2
text1=["mixer recption","circular screen","mixer relrase"]
button_text=["begin","begin","begin","begin","begin","begin","begin","begin","begin"]
line=['http://192.168.10.117:5000/mixer/000','http://192.168.10.117:5000/mixer/100','http://192.168.10.117:5000/mixer/200','http://192.168.10.117:5000/mixer/300','http://192.168.10.117:5000/mixer/400','http://192.168.10.117:5000/mixer/500','http://192.168.10.117:5000/mixer/600','http://192.168.10.117:5000/mixer/700','http://192.168.10.117:5000/mixer/800']
line0=['http://192.168.10.108:5000/carrier/moveto/0','http://192.168.10.108:5000/carrier/moveto/1','http://192.168.10.108:5000/carrier/moveto/2','http://192.168.10.108:5000/carrier/moveto/3','http://192.168.10.108:5000/carrier/moveto/4']
CGQ=[[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]]
list=[['0', '1', '1', '1', '1'],['1', '0', '1', '1', '1'],['1', '1', '0', '1', '1'],['1', '1', '1', '0', '1'],['1', '1', '1', '1', '0']]
color=[Green,Green,Green,Green,Green,Green,Green,Green,Green]
color0=[Green,Green,Green,Green,Green]
button_text0="manual:"
button_text1=["station0","station1","station2","station3","station4"]
Num=['0','1','2','3','4']
B0=[size+32,size+102,size+172,size+242,size+312]
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67+(width-67)/3*2,27)
screen = pygame.display.set_mode((int((width-67)/3),height))
screen.fill(Black)
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
    button=text_1.render(button_text,1,Black)
    screen.blit(button,(x+113,y+3))
    pygame.display.update()
def Station(num,x,y,a,color0):
    pygame.draw.rect(screen,color0,[x,y,65,28],0)
    button=text_2.render(button_text1[num],1,Black)
    screen.blit(button,(x+2,y+4))
    img=pygame.image.load('cgq.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(x,y+80))
    button=text_0.render((Num[a]),1,White)
    screen.blit(button,(x+20,668))
    pygame.display.update()
def State_A():
    response=urllib.request.urlopen(line[num])
    button_text[num]="begin"
    color[num]=Green
def State_B():
    for i in range(7):
        response=urllib.request.urlopen(line[i])
        button_text[i]="begin"
        button_text[i+1]="end"
    response=urllib.request.urlopen(line[7])
    button_text[7]="begin"
def State_C(num):
    pygame.draw.rect(screen,Black,[size,573,400,50],0)
    pygame.draw.rect(screen,Black,[size,667,400,25],0)
    img=pygame.image.load('car.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(B0[num],573))
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
    screen.blit(button,(size,690))
def Mixer(num,x,y,a):
    pygame.draw.rect(screen,Black,[x+20,y+80,25,25],0)
    button=text_2.render(text1[num],1,White)
    screen.blit(button,(x-30,y+4))
    img=pygame.image.load('cgq.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(x,y+30))
    button=text_0.render('{}'.format(a),1,White)
    screen.blit(button,(x+20,y+80))
    pygame.display.update()       
if __name__ == '__main__':
    while True:
        time.sleep(1.5)
        pygame.draw.rect(screen,Black,[size,690,460,30],0)
        pygame.draw.rect(screen,Black,[size+70,382,100,28],0)
        pygame.draw.rect(screen,Green,[size+177,384,62,25],0)
        button1=text_1.render("switch",1,Black)
        screen.blit(button1,(size+181,386))
        button=text_1.render(button_text0,1,White)
        screen.blit(button,(size+70,386))
        B=[[0,size+187,46,button_text[0],color[0]],[1,size+187,82,button_text[1],color[1]],[2,size+187,118,button_text[2],color[2]],[3,size+187,154,button_text[3],color[3]],[4,size+187,190,button_text[4],color[4]],[5,size+187,226,button_text[5],color[5]],[6,size+187,262,button_text[6],color[6]],[7,size+187,298,button_text[7],color[7]],[8,size+187,334,button_text[8],color[8]]]
        response=urllib.request.urlopen('http://192.168.10.117:5000/status')
        html=response.read().decode()
        z=(html[1:-1].split(': '))[1][1:-1].split(', ')
        D=[[0,size+52,420,z[0]],[1,size+177,420,z[1]],[2,size+302,420,z[2]]]
        if z[0]=='1':
            color=[Gray,Green,Green,Green,Gray,Green,Green,Green,Green]
        elif z[0]=='0':
            if z[1]=='1':
                color=[Green,Green,Green,Green,Green,Green,Green,Green,Green]
            elif z[1]=='0':
                color=[Green,Green,Green,Gray,Green,Green,Green,Green,Green]
        for k in D:
            Mixer(k[0],k[1],k[2],k[3])
        for i in B:
            Process(i[0],i[1],i[2],i[3],i[4])
        if color0==[Green,Green,Green,Green,Green]:
            if button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"]:
                response2=urllib.request.urlopen('http://192.168.10.108:5000/carrier/status')
                html2=response2.read().decode()
            a=(html2[1:-1].split(': '))[2][1:-1].split(', ')
            b=(html2[1:-1].split(', '))[0].split(': ')                
            if b[1]!='-1':
                State_C(int(b[1]))
                if a not in list:
                    GZ()
            elif b[1]=='-1':
                pygame.draw.rect(screen,Black,[size,573,400,50],0)
                pygame.draw.rect(screen,Black,[size,667,400,25],0)
                if a!=['1','1','1','1','1']:
                    GZ()
            C=[[0,size+32,538,int(a[0]),color0[0]],[1,size+102,538,int(a[1]),color0[1]],[2,size+172,538,int(a[2]),color0[2]],[3,size+242,538,int(a[3]),color0[3]],[4,size+312,538,int(a[4]),color0[4]]]
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
                            if size+177<=pos[0]<=size+242 and 384<=pos[1]<=409:
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
                                    if button_text==["begin","begin","begin","begin","begin","begin","begin","begin","begin"] and color[i[0]]==Green and button_text0=="manual:":
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
                                        C=[[0,size+32,538,CGQ[v[0]][0],color0[0]],[1,size+102,538,CGQ[v[0]][1],color0[1]],[2,size+172,538,CGQ[v[0]][2],color0[2]],[3,size+242,538,CGQ[v[0]][3],color0[3]],[4,size+312,538,CGQ[v[0]][4],color0[4]]]
                                        for f in C:
                                            Station(f[0],f[1],f[2],f[3],f[4])
        pygame.display.update()
