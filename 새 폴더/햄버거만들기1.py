############빵과 재료의 스프라이트를 만들고
############스프라이트에 대한 좌표값도 지정 한 후
############재료를 선택하는 방법을 구현
############빵의 디스플레이를 먼저 임의로 구현 한 후
############방의 디스플레이를 랜덤 값으로 구현 하

import pygame,random,time,sys
from pygame.locals import *
from random import randint

BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GRAY = [195,195,195]

pygame.init()
pygame.font.init()
###############필요한 변수 및 배열 선언############################
UP_BREAD = 0
DOWN_BREAD = 0
BEAF = 0
CIZ = 0
YANGSANG = 0
TOMATO =0
CNT = 0
TIME = 0
NEW = 0
check = []
###############################햄버거 재료 클래스화########################
class Ingredient(pygame.sprite.Sprite):
    def __init__ (self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.x = 0
        self.rect.y = 0

    def update(self,change_y):
        self.rect.y += change_y

################################스크린과 여러 이미지 배경과 스프라이트 그룹생성################

screen_p_width = 699
screen_p_height = 507
screen = pygame.display.set_mode([screen_p_width,screen_p_height])
pygame.display.set_caption("버거킹")
background_image = pygame.image.load("back1.png").convert()
clock = pygame.time.Clock()

################이미지 생성 및 함수 선언##################

beaf = pygame.image.load("beaf.png").convert()
ciz = pygame.image.load("ciz.png").convert()
down_bread = pygame.image.load("down_bread.png").convert()
tomato = pygame.image.load("tomato.png").convert()
up_bread = pygame.image.load("up_bread.png").convert()
yangsang = pygame.image.load("yangsang.png").convert()

def image_load(filename,x,y): #이미지 로드 및 화면 빌드
    filename.set_colorkey(WHITE)
    screen.blit(filename,[x,y])

def rand_maker(index,c_height): #리스값과 비교
    if hamb[index] == 0:
        image_load(down_bread,c_width-5,c_height-5)
        DOWN_BREAD = 1
    elif hamb[index] == 1:
        image_load(beaf,c_width,c_height)
        BEAF = 1
        c_height = c_height - 20
    elif hamb[index] == 2:
        image_load(tomato,c_width,c_height)
        TOMATO = 1
        c_height = c_height - 20
    elif hamb[index] == 3: #양상추
        image_load(yangsang,c_width,c_height+3)
        YANGSANG = 1
        c_height = c_height - 20
    elif hamb[index] == 4:
        image_load(ciz,c_width-3,c_height)
        CIZ = 1
        c_height = c_height - 20
    elif hamb[index] == 5:
        image_load(up_bread,c_width-5,c_height-32)
        UP_BREAD = 1
            
def font(size,st,x,y): #폰트 객체 생성
    font = pygame.font.Font("hun.ttf",size)                        #폰트 객체생성
    text = font.render(st,True,BLACK)                         
    screen.blit(text,[x,y])

########################################################
screen.blit(background_image,[0,0])
#screen.blit(yap1_image,[429,250])
###################반복문 시작##########################
while 1:
    TIME = TIME + 0.1
    hamb = [0]
    next_stage = 0
    j = 5
    ########0 = down_bread , 1 = beaf , 2 = tomato , 3 = yangsang , 4 = ciz , 5 = up_bread###
    ##########햄버거 랜덤으로 생성#################
    for i in range(1,j):
        y = random.randint(1,4)
        hamb.append(y)
    hamb.append(5)
    print(str(hamb))
    while 1:
        check = []
        print(str(check))
        TIME = TIME + 0.1
        p_height = 428
        c_height = 428
        p_width = 98
        c_width = 446
        CNT = 0
        next_stage = 0
        if NEW == 1:
            NEW = 0
            time.sleep(1)
            screen.blit(background_image,[0,0])
            hamb = [0]
            for i in range(1,j):
                y = random.randint(1,4)
                hamb.append(y)
            hamb.append(5)
            print(str(hamb))
        if 1:
            rand_maker(0,c_height)
            c_height = c_height - 15
            if 1:
                rand_maker(1,c_height)
                c_height = c_height - 20
                print(c_height)
                if 1:
                    rand_maker(2,c_height)
                    c_height = c_height - 20
                    if 1:
                        rand_maker(3,c_height)
                        c_height = c_height - 20
                        if 1:
                            rand_maker(4,c_height)
                            c_height = c_height - 20
                            if 1:
                                rand_maker(5,c_height)
                                
                                
    ###########각자 알맞은 키값을 해당 하여 재료 스크린에 출력#############
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('d'): #고기
                        image_load(beaf,p_width,p_height)
                        p_height = p_height - 20
                        check.append(1)
                        CNT = CNT + 1
                    if event.key == ord('s'): #치즈
                        image_load(ciz,p_width-3,p_height)
                        CIZ = 1
                        p_height = p_height - 20
                        check.append(4)
                        CNT = CNT + 1
                    if event.key == ord('x'): #양상추
                        image_load(yangsang,p_width,p_height+3)
                        YANGSANG = 1
                        p_height = p_height - 20
                        check.append(3)
                        CNT = CNT + 1
                    if event.key == ord('c'): #토마토
                        image_load(tomato,p_width,p_height)
                        TOMATO = 1
                        p_height = p_height - 20
                        check.append(2)
                        CNT = CNT + 1
                    if event.key == ord('a'): #덮개빵
                        p_height = p_height - 30
                        image_load(up_bread,p_width-6,p_height)
                        UP_BREAD = 1
                        p_height = 428
                        check.append(5)
                        CNT = CNT + 1
                    if event.key == ord('z'): #밑빵
                        image_load(down_bread,p_width-5,p_height)
                        DOWN_BREAD = 1
                        p_height = p_height - 15
                        check.append(0)
                        CNT = CNT + 1

                if event.type == pygame.KEYUP:
                    if event.key == ord('z'):
                        None
                    if event.key == ord('x'):
                        None
                    if event.key == ord('c'):
                        None
                    if event.key == ord('a'):
                        None
                    if event.key == ord('s'):
                        None
                    if event.key == ord('d'):
                        None
        #######################재료 체크 하는 부분#####################3
            if CNT == 1:    #첫 번째
                if hamb[0] == check[0]:
                    next_stage = 0
                elif hamb[0] != check[0]:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                    
            if CNT == 2:    #두 번째
                if hamb[1] == check[1]:
                    next_stage = 0
                elif hamb[1] != check[1]:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                    
            if CNT == 3:    #세 번째
                if hamb[2] == check[2]:
                    next_stage = 0
                elif hamb[2] != check[2]:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                    
            if CNT == 4:    #네 번째
                if hamb[3] == check[3]:
                    next_stage = 0
                else:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                    
            if CNT == 5:    #다섯 번째
                if hamb[4] == check[4]:
                    next_stage = 0
                else:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
            if CNT == 6:    #여섯 번째
                if hamb[5] == check[5]:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                else:
                    NEW = 1
                    time.sleep(0.2)
                    next_stage = 1
                    
            font(20,str(TIME),20,20)
            clock.tick(2000)
            pygame.display.flip()
            if next_stage == 1:
                break
    
pygame.quit()
