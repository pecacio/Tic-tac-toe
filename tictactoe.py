#importing the necessary modules
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas import Series as sr

#NxN tic-tac-toe board

N=3

#function to check the winner
def checkwin(board,n=3):
  global N
  N=n
  flag1=True
  flag2=True
  temp3=board[0][0]
  temp4=board[0][N-1]
  for i in range(N):
    flag=True
    temp1=board[i][0]
    temp2=board[0][i]
    for j in range(N):
      if temp1!=board[i][j] or temp1==-1:
        flag=False
        break
    if flag:
      return temp1
    flag=True
    for j in range(N):
      if temp2!=board[j][i] or temp2==-1:
        flag=False
        break
    if flag:
      return temp2
    if temp3!=board[i][i]:
      flag1=False
    if temp4!=board[i][N-1-i]:
      flag2=False
  if flag1:
    return temp3
  if flag2:
    return temp4
  return -1


#function to generate random ti-tac-toe boards
#used for testing purposes
def gen_rnd_board(steps=5):
  global N
  x=np.array([-1]*(N*N)).reshape((N,N))
  move=1
  for i in range(steps):
    ind=np.argwhere(x==-1)
    ch=np.random.choice(len(ind))
    x[ind[ch][0]][ind[ch][1]]=move
    move=(move+1)%2
  return x

#Check if the move is invalid i.e., position of the new move is empty or not
def checkinvalid(board,a,b):
  global N
  if a>=0 and a<N and b<N and b>=0:
    if board[a][b]==-1:
      return True
    return False
  return False


#function to print the board in tic-tac-toe grid format
def print_board(board,flag=False):
  if flag:
    return
  txt=''
  x=np.where(board==-1,' ',np.where(board==0,'O','X'))
  for i in range(N):
    t1=' | '.join(x[i])
    print(t1)
    if i!=N-1:
      txt2=['_']*(3*N)
      t2=''.join(txt2)
      print(t2)

def print_(text,flag):
  if flag==False:
    print(text)
  return

#AI algorithm 1(SLOWER)
#generally it doesn't choose the move which ensures faster win but it is still undefeatable 
def find_best_move(t,depth=0):
  global N
  board=t.copy()
  ind=np.argwhere(board<0)
  move=(N-len(ind)+1)%2
  if len(ind)==0 or checkwin(board)==1 or checkwin(board)==0:
    winner=checkwin(board)
    if winner==1:
      return 1
    elif winner==0:
      return -1
    else:
      return 0
  scores=[]
  for i in range(len(ind)):
    indices=ind[i]
    board[indices[0]][indices[1]]=move
    scores.append(find_best_move(board,depth+1))
    board[indices[0]][indices[1]]=-1
  if move==0:
    if depth==0:
      return ind[(np.array(scores)).argmin()]
    return min(scores)
  if move==1:
    if depth==0:
      return ind[(np.array(scores)).argmax()]
    return max(scores)

#AI algorithm 2(LITTLE FASTER)
#chooses moves which ensures faster win by using a evaluating function for board which considers the number of moves ('depth') also
#impossible to defeat
def find_best_move2(t,depth=0):
  global N
  board=t.copy()
  ind=np.argwhere(board<0)
  move=(N-len(ind)+1)%2
  if len(ind)==0 or checkwin(board)==1 or checkwin(board)==0:
    winner=checkwin(board)
    if winner==1:
      return max(1-depth/(N*N),0.1)
    elif winner==0:
      return min(-1+depth/(N*N),-0.1)
    else:
      return 0
  scores=[]
  for i in range(len(ind)):
    indices=ind[i]
    board[indices[0]][indices[1]]=move
    scores.append(find_best_move2(board,depth+1))
    board[indices[0]][indices[1]]=-1
  if move==0:
    if depth==0:
      return ind[(np.array(scores)).argmin()]
    return min(scores)
  if move==1:
    if depth==0:
      return ind[(np.array(scores)).argmax()]
    return max(scores)


#AI algorithm 3 (FASTEST)
#uses alpha-beta pruning to increase the efficency in rejecting bad moves
#wins in minimum number of moves
#CAN'T BEAT IT
Max=1000
Min=-1000
def find_best_move3(t,alpha=-1000,beta=1000,depth=0):
  global N,Max,Min
  board=t.copy()
  ind=np.argwhere(board<0)
  move=(N-len(ind)+1)%2
  if len(ind)==0 or checkwin(board)==1 or checkwin(board)==0:
    winner=checkwin(board)
    if winner==1:
      return max(1-depth/(N*N),0.1)
    elif winner==0:
      return min(-1+depth/(N*N),-0.1)
    else:
      return 0
  scores=[]
  if move==0:
    best=Max
    minind=ind[0]
    for i in range(len(ind)):
      indices=ind[i]
      board[indices[0]][indices[1]]=move
      val=find_best_move3(board,alpha,beta,depth+1)
      board[indices[0]][indices[1]]=-1
      if best>=val:
        best=val
        minind=indices
      beta=min(beta,best)
      if beta<alpha:
        break
    if depth==0:
      return minind
    return best
  else:
    best=Min
    maxind=ind[0]
    for i in range(len(ind)):
      indices=ind[i]
      board[indices[0]][indices[1]]=move
      val=find_best_move3(board,alpha,beta,depth+1)
      board[indices[0]][indices[1]]=-1
      if best<=val:
        best=val
        maxind=indices
      alpha=max(alpha,best)
      if alpha>beta:
        break
    if depth==0:
      return maxind
    return best

#AI algorithm(WORST)
#plays with random moves
def find_best_move4(board):
  ind=np.argwhere(board<0)
  ch=np.random.choice(len(ind))
  return ind[ch]


#function to play human vs ai
#setting ai=1,2,3 or 4 you can choose the algorithm you want to play against
def pvsai(n=3,ai=3):
  global N
  N=n
  board=np.array([-1]*(N*N)).reshape((N,N))
  print('Do you want to start?(Y/N)')
  inp=str(input())
  if inp=='Y':
    cmove=0
  elif inp=='N':
    cmove=1
  else:
    print('wrong input')
  print_board(board)
  for i in range(N*N):
    if i%2==(cmove%2):
      print('Your turn')
      flag=True
      while(flag==True):
        print('Enter your move:')
        inp1=input().split(',')
        a,b=int(inp1[0]),int(inp1[1])
        if checkinvalid(board,a,b):
          board[a][b]=(cmove+1)%2
          flag=False
          break
        else:
          print('Invalid Input')
    else:
      print("Computer's Turn")
      if ai==1:
        a,b=find_best_move(board)
      elif ai==2:
        a,b=find_best_move2(board)
      elif ai==3:
        a,b=find_best_move3(board)
      else:
        a,b=find_best_move4(board)
      board[a][b]=cmove
    print_board(board)
    if i>=(2*N-2):
      winner=checkwin(board)
      if winner==cmove:
        print('Computer won')
        return
      elif winner==((cmove+1)%2):
        print('You won')
        return
      elif winner==-1 and i==(N*N-1):
        print('Draw')
        return


#function to play AI vs AI
#You can set ai1 and ai2 to be 1,2,3 or 4 to see which one is best 
def aivsai(ai1=3,ai2=3,many=False):
  board=np.array([-1]*(N*N)).reshape((N,N))
  for i in range(N*N):
    if i%2==0:
      print_("X's turn",many)
      if ai1==1:
        a,b=find_best_move(board)
      elif ai1==2:
        a,b=find_best_move2(board)
      elif ai1==3:
        a,b=find_best_move3(board)
      else:
        a,b=find_best_move4(board)
      board[a][b]=1
    else:
      print_("O's turn",many)
      if ai2==1:
        a,b=find_best_move(board)
      elif ai2==2:
        a,b=find_best_move2(board)
      elif ai2==3:
        a,b=find_best_move3(board)
      else:
        a,b=find_best_move4(board)
      board[a][b]=0
    print_board(board,many)
    if i>=(2*N-2):
      winner=checkwin(board)
      if winner==1:
        print_('X won',many)
        if many:
          return 1
        return
      elif winner==0:
        print_('O won',many)
        if many:
          return 0
        return
      elif winner==-1 and i==(N*N-1):
        print_('Draw',many)
        if many:
          return -1
        return

#function to play human vs human 
def pvsp():
  board=np.array([-1]*(N*N)).reshape((N,N))
  print_board(board)
  for i in range(N*N):
    if i%2==0:
      print("X's turn")
      flag=True
      while(flag==True):
        print('Enter your move:')
        inp1=input().split(',')
        a,b=int(inp1[0]),int(inp1[1])
        if checkinvalid(board,a,b):
          board[a][b]=1
          flag=False
          break
        else:
          print('Invalid Input')
    else:
      print("O's turn")
      flag=True
      while(flag==True):
        print('Enter your move:')
        inp1=input().split(',')
        a,b=int(inp1[0]),int(inp1[1])
        if checkinvalid(board,a,b):
          board[a][b]=0
          flag=False
          break
        else:
          print('Invalid Input')
    print_board(board)
    if i>=(2*N-2):
      winner=checkwin(board)
      if winner==1:
        print('X won')
        return
      elif winner==0:
        print('O won')
        return
      elif winner==-1 and i==(N*N-1):
        print('Draw')
        return
