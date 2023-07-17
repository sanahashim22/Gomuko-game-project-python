
import os
import random
#from secrets import randbelow, randbits

def init1():
    B=[]
    dim=int(input("dim...."))
    nop=int(input("nop...."))

    for r in range(0,dim):
        arow=[]
        for c in range(0,dim):
            arow.append('-')
        B.append(arow)

    sym=[]
    pnames=[]
    for i in range(0,nop):
        pnames.append(input(f"player {i+1}'s name: "))
        sym.append(input(f"player {i+1}'s symbol: "))

    
    turn = random.randint(0,nop-1)
    return B, dim,nop,sym,pnames,turn
def printBoard (B,dim):
    os.system('cls')
    for r in range(0,dim):
        for c in range (0,dim):
            print(B[r][c],end="")
        print()
def turnmsg(player):
    print(f"{player}'s turn: ")
def slcpos(dim):
 
    while(1):
    
        pr = int(input(f"select row number(0...{dim}) ... "))
        if(pr<=dim and pr>=1):
            pr-=1
            break
        else:
            print("wrong coordinates, enter again: ")
    
    while(1):
    
        pc = int(input(f"select column number(0...{dim}) ... "))
        if(pc<=dim and pc>=1):
            pc-=1
            break
        else:
            print("wrong coordinates, enter again: ")
    for i in range(0,dim):
        if(B[pr][pc]!='-' or pr<0 or pr>dim or pc <0 or pc > dim):
            print("wrong coordinates, enter again: ")
            pr = int(input(f"select row number(0...{dim}) ... "))
            pc = int(input(f"select column number(0...{dim}) ... "))
            pr-=1
            pc-=1
    return pr, pc
def plcmov(B,pr,pc,haramisym):
    B[pr][pc]=haramisym
def trnchng(turn,nop):
    turn=(turn+1)%nop
    return turn

def isValidMove(pr,pc,dim,B):
    if ((pr >= 0 and pr < dim) and (pc >= 0 and pc < dim) and (B[pr][pc] == '-')):
         return True
    else:
         return False

def horiz(B,r,c,dim,wincount,sym):
    count = 0
    if (c + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(B[r][c+i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False
def vert(B,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(B[r+i][c]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False
def diag_left(B,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim or c + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(B[r+i][c+i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False
def diag_rig(B,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim or c -(wincount - 1) < 0):
        return False
    for i in range(0,wincount):
        if(B[r+i][c-i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False
def iswin(B,dim,sym,wincount):
    for r in range(0,dim):
        for c in range(0,dim):
            if(horiz(B, r, c, dim, wincount, sym) or
				vert(B, r, c, dim, wincount, sym) or
				diag_left(B, r, c, dim, wincount, sym) or
				diag_rig(B, r, c, dim, wincount, sym)):
                return True 
            
    return False
def game_over(B,dim):
    if(draw(B,dim)==0):
        return True
    return False
def draw(B,dim):
    count = 0
    for r in range(0,dim):
        for c in range (0,dim):
            if(B[r][c] == "-"):
              count+=1
    return count
def computerMove(B,dim,sym,wincount,human,computer):
    wc=0
    for wc in range(wincount,wc>1,-1):
        for r in range(0,dim):
            for c in range(0,dim):
                row=r
                col=c
                if(isValidMove(row,col,dim,B)):
                    B[r][c] = sym[computer]
                    if(iswin(B,dim,sym[computer],wc)):
                        B[r][c]='-'
                        return row,col
                    B[r][c]='-'
        for r in range(0,dim):
            for c in range(0,dim):
                row = r
                col = c
                if(isValidMove(row,col,dim,B)):
                    B[r][c] = sym[human]
                    if(iswin(B,dim,sym[human],wc)):
                        B[r][c]='-'
                        return row,col
                    B[r][c]='-'
    row = random.randint(0,dim-1)
    col = random.randint(0,dim-1)
    while(not isValidMove(row,col,dim,B)):
        row = random.randint(0,dim-1)
        col = random.randint(0,dim-1)
    return row,col




def init():
    b = []
    dim = int(input("Dimension: "))
    Nop = int(input("Number of players: "))
    for r in range(0,dim):
      #  arr = []
       # for c in range(0,dim):
          #  arr.append('-')
            b.append(dim*['-'])
    sym = []
    pname = []
    for i in range(0,Nop):
        pname.append(input(f"Player {i+1}'s name: "))
        sym.append(input(f"Player {i+1}'s symbol: ")) 
    
    turn = random.randint(0,Nop-1)
    return b,dim,Nop,sym,pname,turn

def printBoard(b,dim):
    for r in range(0,dim):
        for c in range (0,dim):
            print(b[r][c],end="")
        print()
def turnMsg(name):
    print(f"{name}'s turn : ")

def isvalid(pr,pc):
    if(pr<0 or pr>dim):
        return False;
    if(pc<0 or pc>dim):
        return False;
    if(b[pr][pc]!='-'):
        return False
    return True;

def selectPosition(dim):
    pr = int(input(f"enter row (1...{dim}) "))
    pc = int(input(f"enter col (1...{dim}) "))
    pr-=1 
    pc-=1
    while not isvalid(pr,pc):
        print("Wrong input....")
        pr = int(input(f"enter row (1...{dim}) ")) 
        pr-=1
        pc = int(input(f"enter col (1...{dim}) ")) 
        pc-=1
    
    return pr,pc
    
def placeMove(b,pr,pc,sym2):
    b[pr][pc] = sym2
    
    
def  turnChange(turn,Nop):
    turn = (turn+1)%Nop
    return turn    
  

def horiz(b,r,c,dim,wincount,sym):
    count = 0
    if (c + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(b[r][c+i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False

def vert(b,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(b[r+i][c]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False


def diag_left(b,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim or c + wincount - 1 >= dim):
        return False
    for i in range(0,wincount):
        if(b[r+i][c+i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False



def diag_rig(b,r,c,dim,wincount,sym):
    count = 0
    if (r + wincount - 1 >= dim or c -(wincount - 1) < 0):
        return False
    for i in range(0,wincount):
        if(b[r+i][c-i]==sym):
            count+=1
    if(count == wincount):
        return True
    else:
        return False



def iswin(b,dim,sym,wincount):
    for r in range(0,dim):
        for c in range(0,dim):
            if(horiz(b, r, c, dim, wincount, sym) or
				vert(b, r, c, dim, wincount, sym) or
				diag_left(b, r, c, dim, wincount, sym) or
				diag_rig(b, r, c, dim, wincount, sym)):
                return True 
            
    return False

def game_over(b,dim):
    if(draw(b,dim)==0):
        return True
    return False

def draw(b,dim):
    count = 0
    for r in range(0,dim):
        for c in range (0,dim):
            if(b[r][c] == "-"):
              count+=1
    return count

#int main(){

print("Enter 1 for player vs player game ")
print("Enter 2 for player vs computer game ")

choice = int(input("choice: "))








#    -------------------main2---------------
#{

if(choice==1):
    b,dim,Nop,sym,pname,turn = init()
    wincount = int(input("Enter winner count : "))
    printBoard(b,dim)
    while (True):
       turnMsg(pname[turn])
       pr,pc = selectPosition(dim)
       placeMove(b,pr,pc,sym[turn])
       printBoard(b,dim)
       if(iswin(b,dim,sym[turn],wincount)):
           print(f"{pname[turn]} is the winner")
           break
       if(game_over(b,dim)):
           print("Game draw")
           break
       turn = turnChange(turn,Nop)
    print("Game over!!!")
#}




#                                     main2
#{
if(choice==2):
    human=1
    computer=0
    B,dim,nop,sym,pname,turn = init1()
    wincount = int(input("Enter winner count : "))
    printBoard(B,dim)
    while (True):
        turnmsg(pname[turn])
   
        if(turn==human):
             pr,pc = slcpos(dim)
      
        else:
            pr,pc = computerMove(B,dim,sym,wincount,human,computer)
        plcmov(B,pr,pc,sym[turn])
        printBoard(B,dim)
        if(iswin(B,dim,sym[turn],wincount)):
             print(f"{pname[turn]} is the winner")
             break
        if(game_over(B,dim)):
              print("Game draw")
              break
        turn = trnchng(turn,nop)
    print("Game over!!!")
    #}


#}



