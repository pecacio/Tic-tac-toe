import pygame as pg
import numpy as np
scr_width=700
scr_height=500

FPS=100

white=(255,255,255)
color_light=(170,170,170)
color_dark=(100,100,100)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)

data=np.load('ttt_data.npy')

def button(btn_loc,btn_side,btn_col,font,caption,text_col,text_loc,nxt=None,info=None,border_radius=20):
    btn={'btn':pg.rect.Rect(btn_loc,btn_side),
         'col':btn_col,
         'bdr':border_radius,
         'txt':font.render(caption,True,text_col),
         'loc':text_loc,
         'c2':nxt,
         'info':info}
    return btn.copy()
def caption(text,col,loc,font_size,font_style='comicsansms',flag=True,):
    font=pg.font.SysFont(font_style,font_size)
    cap={'txt':font.render(text,True,col),'loc':loc,'flag':flag}
    return cap
def game():
    global white,color_light,color_dark,black,red,green,blue,yellow
    pg.init()
    bkg=pg.display.set_mode((scr_width,scr_height))
    pg.display.set_caption('Tic Tac Toe')
    icon=pg.image.load('ttt_icon.jpg')
    pg.display.set_icon(icon)
    d={1:'X',0:'O'}
    all_={}
    scrs={}
    #screen 1
    all_['scr1']={}
    scrs['scr1']=pg.Surface((700,500),pg.SRCALPHA)
    #main text
    all_['scr1']['caps']=[caption('TIC-TAC-TOE',yellow,(10,10),100)]
    #buttons
    font=pg.font.SysFont('comicsansms',25)
    btn_side=(200,40)
    #button vs computer
    btn1=button((250,170),btn_side,color_light,
                font,'Vs Computer',black,(275,170),'scr12.1',info=0)
    #button 2players
    btn2=button((250,230),btn_side,color_light,
                font,'Two players',black,(275,233),'scr11.1',info=1)
    #exit
    quitb=button((250,290),btn_side,color_light,
                 font,'Quit',black,(320,293),'scr1')
    all_['scr1']['btns']=[btn1,btn2,quitb]
    #Font for subpages
    sfont=pg.font.SysFont('comicsansms',35)
    #screen 11.1
    all_['scr11.1']={}
    scrs['scr11.1']=pg.Surface((700,500),pg.SRCALPHA)
    #main text
    all_['scr11.1']['caps']=[caption('Choose for Player 1',yellow,(80,40),60)]
    #sub button11_1a
    sbtn11_1a=button((250,170),btn_side,color_light,
                sfont,'X',black,(338,165),'scr3',info='1')
    #sub button11_1b
    sbtn11_1b=button((250,230),btn_side,color_light,
                sfont,'O',black,(338,225),'scr3',info='0')
    #back button
    back11_1=button((550,420),(100,35),color_light,
                    font,'Back',black,(570,420),'scr1')
    all_['scr11.1']['btns']=[sbtn11_1a,sbtn11_1b,back11_1]
    #screen 12.1
    all_['scr12.1']={}
    scrs['scr12.1']=pg.Surface((700,500),pg.SRCALPHA)
    #main text
    all_['scr12.1']['caps']=[caption('Choose Difficulty',yellow,(100,40),60)]
    #sub button 12_1a
    sbtn12_1a=button((250,170),btn_side,color_light,
                sfont,'Easy',black,(305,164),'scr12.2',info=2)
    #sub button 12_1b
    sbtn12_1b=button((250,230),btn_side,color_light,
                sfont,'Medium',black,(280,225),'scr12.2',info=4)
    #sub button 12_1c
    sbtn12_1c=button((250,290),btn_side,color_light,
                sfont,'Impossible',black,(265,285),'scr12.2',info=6)
    #back button
    back12_1=button((550,420),(100,35),color_light,
                    font,'Back',black,(570,420),'scr1')
    all_['scr12.1']['btns']=[sbtn12_1a,sbtn12_1b,sbtn12_1c,back12_1]
    #screen 12.2
    all_['scr12.2']={}
    scrs['scr12.2']=pg.Surface((700,500),pg.SRCALPHA)
    #main text
    all_['scr12.2']['caps']=[caption('Choose',yellow,(245,40),60)]
    #sub button 12_2a
    sbtn12_2a=button((250,170),btn_side,color_light,
                sfont,'X',black,(338,165),'scr3',info='1')
    #sub button 12_2b
    sbtn12_2b=button((250,230),btn_side,color_light,
                sfont,'O',black,(338,225),'scr3',info='0')
    #back button
    back12_2=button((550,420),(100,35),color_light,
                    font,'Back',black,(570,420),'scr12.1')
    all_['scr12.2']['btns']=[sbtn12_2a,sbtn12_2b,back12_2]
    #screen 3
    scrs['scr3']=pg.Surface((700,500),pg.SRCALPHA)
    srf=pg.Surface((500,500))
    #board
    board=np.array([-1]*3*3).reshape(3,3)
    #tictactoe box
    b_side=150
    box_dim=140
    give=20
    box={}
    for i in range(3):
        for j in range(3):
            box['box'+str(i)+str(j)]=pg.rect.Rect((25+j*b_side,25+i*b_side),(box_dim,box_dim))
    #other
    caps=[caption('Scores',black,(525,10),45),
          caption('Player 1',black,(540,75),30),
          caption('Player 2',black,(540,225),30),
          caption('Your',black,(565,75),30,flag=False),
          caption('Computer',black,(530,225),30,flag=False),
          caption('DRAW',red,(60,150),120,flag=False),
          caption('Winner X',red,(30,150),100,flag=False),
          caption('Winner O',red,(30,150),100,flag=False)]
    
    btns=[button((520,25),(160,300),color_dark,sfont,'',color_dark,(520,25),border_radius=5),
          button((530,125),(140,40),white,font,'0',black,(540,127)),
          button((530,275),(140,40),white,font,'0',black,(540,277)),
          button((520,350),(160,40),color_light,font,'Again',black,(560,350)),
          button((520,420),(160,40),color_light,font,'Back',black,(565,420)),
          button((620,130),(30,30),color_light,font,'X',black,(625,126),border_radius=15),
          button((620,280),(30,30),color_light,font,'O',black,(625,276),border_radius=15)]
    #init
    playmode=0
    plrmv=1
    move_pos=None
    move=1
    #event loop
    clock=pg.time.Clock()
    screen='scr1'
    rec=[0,0]
    prev='scr1'
    alp=255
    alpha=255
    flg=True
    end=False
    running=True
    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    if screen!='scr3':
                        if screen=='scr1' and all_['scr1']['btns'][2]['btn'].collidepoint(event.pos):
                            running=False
                        for i in all_[screen]['btns']:
                            if i['btn'].collidepoint(event.pos):
                                i['col']=color_dark
                                screen=i['c2']
                                if i['info'] is not None:
                                    if type(i['info']) is str:
                                        plrmv=int(i['info'])
                                    else:
                                        playmode=i['info']
                    else:
                        if btns[3]['btn'].collidepoint(event.pos):#Again button
                            board[:,:]=-1
                            caps[5]['flag']=False
                            caps[6]['flag']=False
                            caps[7]['flag']=False
                            flg=True
                            end=False
                        elif btns[4]['btn'].collidepoint(event.pos):#Back button
                            screen='scr1'
                            board[:,:]=-1
                            caps[5]['flag']=False
                            end=False
                            flg=True
                            rec=[0,0]
                        elif btns[5]['btn'].collidepoint(event.pos) or btns[6]['btn'].collidepoint(event.pos):
                            if len(np.argwhere(board<0))==9 or end:
                                plrmv=(plrmv+1)%2
                        for i in range(3):
                            for j in range(3):
                                if box['box'+str(i)+str(j)].collidepoint(event.pos):
                                    if checkinvalid(board,i,j):
                                        move_pos=(i,j)
            elif event.type==pg.MOUSEBUTTONUP:
                for scrn in all_.keys():
                    for i in all_[scrn]['btns']:
                        i['col']=color_light
                for i in btns[3:]:
                    i['col']=color_light
        bkg.fill((0,0,0))
        srf.fill((60,25,60))
        scrs['scr1'].fill((60,25,60))
        scrs['scr11.1'].fill((60,25,60))
        scrs['scr12.1'].fill((60,25,60))
        scrs['scr12.2'].fill((60,25,60))
        scrs['scr3'].fill((60,25,60))
        if screen!='scr3':
            for i in all_[screen]['btns']:
                pg.draw.rect(scrs[screen],i['col'],i['btn'],border_radius=i['bdr'])
                scrs[screen].blit(i['txt'],i['loc'])
            for i in all_[screen]['caps']:
                scrs[screen].blit(i['txt'],i['loc'])
        else:
            btns[5]['txt']=font.render(d[plrmv],True,black)
            btns[6]['txt']=font.render(d[1-plrmv],True,black)
            for i in btns:
                pg.draw.rect(scrs['scr3'],i['col'],i['btn'],border_radius=i['bdr'])
                scrs['scr3'].blit(i['txt'],i['loc'])
            for i in range(3):
                for j in range(3):
                    pg.draw.rect(srf,white,box['box'+str(i)+str(j)],border_radius=10)
                    if board[i,j]==1:
                        pg.draw.lines(srf,green,True,points=[(25+j*b_side+give,25+i*b_side+give),
                                       (25+box_dim+j*b_side-give,25+box_dim+i*b_side-give)],
                                       width=10)
                        pg.draw.lines(srf,green,True,points=[(25+j*b_side+give,25+box_dim+i*b_side-give),
                                       (25+box_dim+j*b_side-give,25+i*b_side+give)],
                                       width=10)
                    elif board[i,j]==0:
                        pg.draw.circle(srf,blue,(25+box_dim//2+j*b_side,25+box_dim//2+i*b_side)
                                       ,box_dim//2-give,width=10)
            if end==False:
                alpha=255
                move=(len(np.argwhere(board<0)))%2
                if playmode%2==0:
                    caps[3]['flag']=caps[4]['flag']=True
                    caps[1]['flag']=caps[2]['flag']=False
                    if move!=plrmv:
                        move_pos=find_move(playmode,board)
                    if move_pos is not None:
                        board[move_pos[0],move_pos[1]]=move
                        move_pos=None
                else:
                    caps[3]['flag']=caps[4]['flag']=False
                    caps[1]['flag']=caps[2]['flag']=True
                    if move_pos is not None:
                        board[move_pos[0],move_pos[1]]=move
                        move_pos=None
            res=list(checkwin(board))
            if len(np.argwhere(board<0))==0 and res[-1]==-1:
                caps[5]['flag']=True
            if caps[5]['flag']==True or res[-1]==1 or res[-1]==0:
                end=True
            for i in caps[:5]:
                if i['flag']:
                    scrs['scr3'].blit(i['txt'],i['loc'])
            if res[-1]==plrmv and flg:
                rec[0]+=1
                flg=False
            elif res[-1]==(1-plrmv) and flg:
                rec[1]+=1
                flg=False
            btns[1]['txt']=font.render(str(rec[0]),True,black)
            btns[2]['txt']=font.render(str(rec[1]),True,black)
            if type(res[0]) is str:
                if res[0]=="h":
                    pg.draw.lines(srf,red,True,points=[(25,25+box_dim//2+res[1]*b_side)
                                                       ,(15+3*b_side,25+box_dim//2+res[1]*b_side)],width=15)
                elif res[0]=="v":
                    pg.draw.lines(srf,red,True,points=[(25+box_dim//2+res[1]*b_side,25)
                                                       ,(25+box_dim//2+res[1]*b_side,15+3*b_side)],width=15)
                elif res[0]=="1d":
                    pg.draw.lines(srf,red,True,points=[(25,25)
                                                       ,(15+3*b_side,15+3*b_side)],width=15)
                elif res[0]=="2d":
                    pg.draw.lines(srf,red,True,points=[(25,15+3*b_side)
                                                       ,(15+3*b_side,25)],width=15)
            srf.set_alpha(int(alpha))
            scrs['scr3'].blit(srf,(0,0))
            if res[-1]==1:
                caps[6]['flag']=True
            elif res[-1]==0:
                caps[7]['flag']=True
            if end:
                alpha=max(10,alpha-10)
                for i in caps[5:]:
                    if i['flag']==True:
                        scrs['scr3'].blit(i['txt'],i['loc'])
        if screen!=prev and alp>=0:
            alp=alp-15
        else:
            prev=screen
            alp=min(alp+15,255)
        scrs[prev].set_alpha(alp)
        bkg.blit(scrs[prev],(0,0))
        pg.display.update()
        clock.tick(FPS)
    pg.quit()

def checkinvalid(board,a,b):
    if a>=0 and a<3 and b<3 and b>=0:
        if board[a][b]==-1:
            return True
        return False
    return False
def checkwin(board):
    N=3
    flag1=True
    flag2=True
    temp3=board[0][0]
    temp4=board[0][N-1]
    for i in range(N):
        #check horizontals
        flag=True
        temp1=board[i][0]
        for j in range(N):
            if temp1!=board[i][j] or temp1==-1:
                flag=False
                break
        if flag:
            return ("h",i,temp1)
        #check verticals
        flag=True
        temp2=board[0][i]
        for j in range(N):
            if temp2!=board[j][i] or temp2==-1:
                flag=False
                break
        if flag:
            return ("v",i,temp2)
        #check first diagonal
        if temp3!=board[i][i] or board[i][i]==-1:
            flag1=False
        #check second diagonal
        if temp4!=board[i][N-1-i] or board[i][N-1-i]==-1:
            flag2=False
    if flag1:
        return ("1d",temp3)
    if flag2:
        return ("2d",temp4) 
    return (-1,-1)

# Random Algorithm
def find_rnd_move(board):
    ind=np.argwhere(board<0)
    ch=np.random.choice(len(ind))
    return ind[ch]
def find_best_move(board):
    global data
    l=data[:,0].copy()
    poses=data[:,1:].astype(np.int)
    d={1:'X',0:'O',-1:'_'}
    for i in range(8):
        arr=board.copy()
        rem=i%2
        quo=i//2
        r=np.rot90(arr,k=quo)
        if rem!=0:
            r=np.fliplr(r)
        txt=''
        for j in range(3):
            for k in range(3):
                txt+=d[r[j,k]]
        if txt in l:
            mv=np.zeros(shape=(3,3))
            ind=np.where(l==txt)
            pos=poses[ind][0]
            mv[pos[0],pos[1]]=1
            if rem!=0:
                mv=np.fliplr(mv)
            mv=np.rot90(mv,4-quo)
            return np.argwhere(mv)[0]
def find_move(playmode,board):
    if playmode==2:
        res=find_rnd_move(board)
    elif playmode==4:
        ch=np.random.choice([0,1],p=[0.2,0.8])
        res=find_rnd_move(board) if ch==0 else find_best_move(board)
    else:
        res=find_best_move(board)
    return res 
def gen_rnd_board(steps=5):
    N=3
    x=np.array([-1]*(N*N)).reshape((N,N))
    move=1
    for i in range(steps):
        ind=np.argwhere(x==-1)
        ch=np.random.choice(len(ind))
        x[ind[ch][0]][ind[ch][1]]=move
        move=(move+1)%2
    return x
