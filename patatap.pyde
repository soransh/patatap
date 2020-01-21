def setup():
    add_library('sound')
#    fullScreen()
    size(600, 600)
    frameRate(40)
    background(0,0,0)
    noStroke()
 
def draw():
    F()
    N()
    M()
    Q()
    R()
    D()
    L()
    G()
    A()
    B()
    C()
    E()
    H()
    I()
    J()
    K()    
    O()
    P()
    S()
    T()
    U()
    V()
    W()
    X()
    Y()
    Z()
    

        
 
def keyPressed():
    global flagA,flagB,flagC,flagD,flagE,flagF,flagG,flagH,flagI,flagJ,flagK,flagL,flagM,flagN,flagO,flagP,flagQ,flagR,flagS,flagT,flagU,flagV,flagW,flagX,flagY,flagZ
    if (key == 'a')or(key=='A'):
        soundA=SoundFile(this,'piston-2.mp3')
        soundA.play()
        flagA=1
    if (key=='b')or(key=='B'):
        flagB=1
        soundB=SoundFile(this,'flash-3.mp3')
        soundB.play()
    if (key=='c')or(key=='C'):
        flagC=1
        soundC=SoundFile(this,'flash-1.mp3')
        soundC.play()
    if (key=='d')or(key=='D'):
        flagD=1
        soundD=SoundFile(this,'moon.mp3')
        soundD.play()
    if (key=='e')or(key=='E'):
        flagE=1
        soundE=SoundFile(this,'confetti.mp3')
        soundE.play()
    if(key=='f')or(key=='F'):
        flagF=1
        soundF=SoundFile(this,'corona.mp3')
        soundF.play()
    if(key=='g')or(key=='G'):
        flagG=1
        soundG=SoundFile(this,'flash-2.mp3')
        soundG.play()        
    if(key=='h')or(key=='H'):
        flagH=1
        soundH=SoundFile(this,'clay.mp3')
        soundH.play()
    if(key=='i')or(key=='I'):
        flagI=1
        soundI=SoundFile(this,'glimmer.mp3')
        soundI.play()
    if(key=='j')or(key=='J'):
        flagJ=1
        soundJ=SoundFile(this,'strike.mp3')
        soundJ.play()
    if(key=='k')or(key=='K'):
        flagK=1
        soundK=SoundFile(this,'pinwheel.mp3')
        soundK.play()
    if(key=='l')or(key=='L'):
        flagL=1
        soundL=SoundFile(this,'ufo.mp3')
        soundL.play()
    if(key=='m')or(key=='M'):
        flagM=1
        soundM=SoundFile(this,'splits.mp3')
        soundM.play()
    if(key=='n')or(key=='N'):
        flagN=1
        soundN=SoundFile(this,'prism-1.mp3')
        soundN.play()
    if(key=='o')or(key=='O'):
        flagO=1
        soundO=SoundFile(this,'dotted-spiral.mp3')
        soundO.play()
    if(key=='p')or(key=='P'):
        flagP=1
        soundP=SoundFile(this,'piston-1.mp3')
        soundP.play()
    if(key=='q')or(key=='Q'):
        flagQ=1
        soundQ=SoundFile(this,'squiggle.mp3')
        soundQ.play()
    if(key=='r')or(key=='R'):
        flagR=1
        soundR=SoundFile(this,'bubbles.mp3')
        soundR.play()
    if(key=='s')or(key=='S'):
        flagS=1
        soundS=SoundFile(this,'prism-2.mp3')
        soundS.play()
    if(key=='t')or(key=='T'):
        flagT=1
        soundT=SoundFile(this,'prism-3.mp3')
        soundT.play()
    if(key=='u')or(key=='U'):
        flagU=1
        soundU=SoundFile(this,'piston-3.mp3')
        soundU.play()
    if(key=='v')or(key=='V'):
        flagV=1
        soundV=SoundFile(this,'suspension.mp3')
        soundV.play()
    if(key=='w')or(key=='W'):
        flagW=1
        soundW=SoundFile(this,'timer.mp3')
        soundW.play()
    if(key=='x')or(key=='X'):
        flagX=1
        soundX=SoundFile(this,'veil.mp3')
        soundX.play()
    if(key=='y')or(key=='Y'):
        flagY=1
        soundY=SoundFile(this,'wipe.mp3')
        soundY.play()
    if(key=='z')or(key=='Z'):
        flagZ=1
        soundZ=SoundFile(this,'zig-zag.mp3')
        soundZ.play()
        
        
                        
flagA=0
rA1=40
def A():
    global flagA,rA1
    if(flagA==1):
        fill(255)
        rect(100,100,100,100)
        fill(255,0,0)
        circle(200,200,rA1)
        rA1inc()

        
def rA1inc():
    global rA1,flagA
    rA1+=5
    if(rA1>80):
        stroke(125)
        line(500,0,450,600)
        line(480,0,430,600)
        line(460,0,410,600)
    if(rA1==140):
        flagA=0
        rA1=40
        background(0)
  
flagB=0
xB=0
xcB=50
countB=0    
def B():
    global flagB,xB,countB,xcB
    if(flagB==1):
        frameRate(30)
        fill(205,0,60)
        circle(436,300,xcB)
        fill(205,50,160)
        triangle(200+xB,250,200+xB,350,286+xB,300)
        countB+=1
        xB+=50
        xcB+=10
        if(countB>=5):
            flagB=0
            xB=0
            countB=0
            xcB=50
            background(0)

flagC=0            
xC=200
yC=200
aC=10
zC=0
cC=40
def C():
    global xC,yC,aC,zC,cC,flagC
    if(flagC==1):
        arcC()
        fill(125,125,255)
        rect(xC+zC,yC+aC,20,20)
        fill(240,120,0)
        circle(xC+9,yC+9,40+cC)
        cC=cC+10
        if(cC>160):
            flagC=0
            cC=40
            aC=10
            zC=0
            cC=40
            bC=0
            background(0)
    
bC=0
def arcC():
    global aC,bC,zC
    ras=radians(bC)
    aC=100*sin(ras)
    zC=100*cos(ras)
    bC=bC+30
    
flagD=0
cxD=200
cyD=200

def D():
    global cxD,cyD,flagD
    if(flagD==1):
#        background(0)
        fill(255)
        circle(300,300,400)
        fill(255,125,125)
        circle(cxD,200,30)
        fill(125,255,125)
        circle(cxD,200 + 50,30)        
        fill(125,125,255)
        circle(cxD,200 + 100,30)
        cxD+=5    
        fill(255,125,125)
        circle(200+50,cyD,30)
        fill(125,255,125)
        circle(200+100,cyD,30)        
        fill(125,125,255)
        circle(200+150,cyD,30)
        cxD+=5
        cyD+=5
        if(cxD>420):
            cxD=200
            cyD=200
            flagD=0
            background(0)
            
flagE=0
countE=1
crE=100
def E():
    global flagE,countE,crE
    if(flagE==1):
        if(countE%5==0):
            fill(255,125,155)
            rect(0,0,600,600)
        if(countE%5==3):
            fill(55,125,255)
            rect(0,0,600,600)
        fill(15,150,40)
        circle(300,300,crE)
        countE+=1
        crE+=10
        if(crE>275):
            flagE=0
            crE=100
            background(0)
            
flagF=0
ryF=-500
incF=22
def F():
    global flagF,ryF,incF
    if(flagF==1):
        background(0)
        fill(275,245,115)
        rect(0,ryF,600,600)
        ryF+=incF
        if(ryF>600):
            flagF=0
            ryF=-200
            background(0)
 
flagG=0
xG=150
yG=200
wG=40
def G():
    global flagG,xG,yG,wG
    if(flagG==1):
        fill(0,255,255)
        rect(xG,yG,wG,40)
        rect(xG,yG+50,wG,40)
        rect(xG,yG+100,wG,40)
        rect(xG,yG+150,wG,40)
        wG+=20
        if(wG>300):
            flagG=0
            wG=40
            background(0)  
            
flagH=0
xH=300
yH=300
bH=0
mH=50
def H():
    global bH,xH,yH,flagH,mH
    if(flagH==1):
        ras=radians(bH)
        aH=mH*sin(ras)
        zH =mH*cos(ras)
        bH=bH+30
        mH+=10
        fill(255,50,255)
        circle(xH+aH,yH+zH,15)
        if(bH>600):
            flagH=0
            bH=0
            mH=50
            background(0)
            
flagI=0
rI=50
def I():
    global flagI,rI
    if(flagI==1):
        fill(255,0,0)
        circle(200,200,rI)
        fill(255,255,0)
        circle(150,450,rI)
        fill(255,0,255)
        circle(500,300,rI)
        rI+=10
        if(rI>200):
            rI=50
            flagI=0
            background(0)    
            
flagJ=0
xJ=280
yJ=280
angJ=90
def J():
    global flagJ,xJ,yJ,angJ
    if(flagJ==1):
        noStroke()
        fill(255,150,100)
        radJ=radians(angJ)
        x1J=xJ+(120*sin(radJ))
        y1J=yJ+(120*cos(radJ))
        rect(x1J,y1J,40,40,125,125,125,125)
        fill(125,125,220)
        x2J=xJ+(80*sin(radJ))
        y2J=yJ+(80*cos(radJ))
        rect(x2J,y2J,40,40,125,125,125,125)
        fill(100,225,100)
        x3J=xJ+(40*sin(radJ))
        y3J=yJ+(40*cos(radJ))
        rect(x3J,y3J,40,40,125,125,125,125)
        fill(255,150,100)
        rad1J=radians(angJ+180)
        x4J=xJ+(120*sin(rad1J))
        y4J=yJ+(120*cos(rad1J))
        rect(x4J,y4J,40,40,125,125,125,125)
        fill(125,125,220)
        x5J=xJ+(80*sin(rad1J))
        y5J=yJ+(80*cos(rad1J))
        rect(x5J,y5J,40,40,125,125,125,125)
        fill(100,225,100)
        x6J=xJ+(40*sin(rad1J))
        y6J=yJ+(40*cos(rad1J))
        rect(x6J,y6J,40,40,125,125,125,125)
        angJ+=5
        if(angJ==180):
            flagJ=0
            angJ=90
            background(0)
        
        
    
flagK=0
yK=-225
def K():
    global flagK,yK
    if(flagK==1):
        fill(0)
        noStroke()
        circle(400,yK,300)
        fill(100,225,100)
        circle(400,yK,250)
        fill(125,125,220)
        circle(400,yK,200)
        fill(255,150,100)
        circle(400,yK,150)
        yK+=19
        if(yK>350):
            yK=-225
            flagK=0
            background(0)
        
    
flagL=0
x1L=20
y2L=20
x3L=600
y4L=600
def L():
    global flagL,x1L,y2L,x3L,y4L
    if(flagL==1):
        noStroke()
        fill(125,255,255)
        rect(0,280,x1L,20,125,125,125,125)
        rect(280,0,20,y2L,125,125,125,125)
        rect(x3L,300,x1L,20,125,125,125,125)
        rect(300,y4L,20,y2L,125,125,125,125)
        x1L+=20
        y2L+=20
        x3L-=20
        y4L-=20
        if(x1L>640):
            flagL=0
            x1L=20
            y2L=20
            x3L=600
            y4L=600
            background(0)
            
        
        

flagM=0
x1M=300
x2M=300
y3M=300
y4M=300
def M():
    global flagM,x1M,x2M,y3M,y4M
    if(flagM==1):
        background(0)
        fill(125,125,255)
        circle(x1M,300,40)
        circle(x2M,300,40)
        circle(300,y3M,40)
        circle(300,y4M,40)
        fill(240,120,0)
        circle(x1M,y3M,40)
        circle(x1M,y4M,40)
        circle(x2M,y3M,40)
        circle(x2M,y4M,40)
        x1M+=20
        x2M-=20
        y3M+=20
        y4M-=20
        if(x1M>620):
            x1M=300
            x2M=300
            y3M=300
            y4M=300
            flagM=0
            background(0)


flagN=0
flag2N=0
countN=0
def N():
    global flagN,countN,flag2N
    if(flagN==1)and(flag2N==0):
        fill(255,132,205,195)
        rect(0,0,600,600)
        flag2N=1
    if(flagN==1)and(flag2N==1):
        countN+=1
        if(countN>40):
            background(0)
            countN=0
            flagN=0
            flag2N=0
    
flagO=0
xO=300
yO=300
angO=0
mO=300
def O():
    global flagO,xO,yO,angO,mO
    if(flagO==1):
        ras=radians(angO)
        x=mO*sin(ras)
        y=mO*cos(ras)
        mO-=10
        angO+=30
        fill(255,125,125)
        rect(xO+x,yO+y,20,20,125,125,125,125)
        if(angO>900):
            flagO=0
            xO=300
            yO=300
            angO=0
            mO=300
            background(0)
            
        
    
flagP=0
lP=1
def P():
    global flagP,lP
    if(flagP==1):
        if(lP>=1)and(lP<5):
            triangle(200,200,275,200,200,275)
            lP+=1
        if(lP>=5)and(lP<10):
            rect(200,200,75,75)
            lP+=1
        if(lP>=10)and(lP<=15):
            rect(200,200,75,75)
            triangle(200,210,200,285,175,237)
            triangle(275,200,275,275,300,237)
            triangle(200,200,275,200,237,175)
    
flagQ=0
x1Q=0
y1Q=300
x2Q=600
y2Q=300
x3Q=300
y3Q=0
x4Q=300
y4Q=600
def Q():
    global x1Q,x2Q,x3Q,x4Q,y1Q,y2Q,y3Q,y4Q,flagQ
    if(flagQ==1):
        fill(255,125,125,125)
        triangle(300,300,0,300,0,y1Q)
        triangle(300,300,600,300,600,y2Q)
        triangle(300,300,300,0,x3Q,0)
        triangle(300,300,300,600,x4Q,600)
        y1Q-=10
        y2Q+=10
        x3Q+=10
        x4Q-=10
        if(y2Q>900):
            y1Q=300
            y2Q=300
            x3Q=300
            x4Q=300
            background(0)
            flagQ=0
            
        
         
        
    
flagR=0
xqR=125
yqR=125
xtR=550
ytR=550
def R():
    global flagR,xqR,yqR,ytR,xtR
    if(flagR==1):
        fill(0,125,255)
        quad(0,100,100,0,xqR,0,0,yqR)
        fill(255,125,0)
        triangle(600,600,600,ytR,xtR,600)
        xqR+=10
        yqR+=10
        xtR-=10
        ytR-=10
        if(xqR>550):
            xqR=100
            yqR=100
            xtR=550
            ytR=550
            background(0)
            flagR=0
        
        
    
flagS=0
rS=500
def S():
    global flagS,rS
    if(flagS==1):
        crS=random(0,255)
        cgS=random(0,255)
        cbS=random(0,255)
        fill(crS,cgS,cbS)
        circle(300,300,rS)
        rS-=30
        if(rS<30):
            rS=500
            flagS=0
            background(0)
            
        
    
flagT=0
angT=0
mT=100
xT=200
yT=300
def T():
    global flagT,angT,mT,xT,yT
    if(flagT==1):
        xT+=2
        rad=radians(angT)
        y=mT*sin(rad)
        angT+=123
        rect(xT,yT+y,20,20)
        if(xT>400):
            flagT=0
            angT=0
            mT=100
            xT=200
            yT=300
            background(0)
        
        
    
flagU=0
x1U=400
x2U=20
def U():
    global flagU,x1U,x2U
    if(flagU==1):
        fill(512,356,122)
        rect(x1U,180,x2U,30)
        rect(x1U,220,x2U,30)
        rect(x1U,260,x2U,30)
        rect(x1U,300,x2U,30)
        rect(x1U,340,x2U,30)
        rect(x1U,380,x2U,30)
        x1U-=20
        x2U+=20
        if(x2U>300):
            x1U=400
            x2U=20
            background(0)
            flagU=0
    
flagV=0
x1V=0
x2V=600
y1V=0
y2V=600
def V():
    global x1V,y1V,x2V,y2V,flagV
    if(flagV==1):
        r=random(0,256)
        g=random(0,256)
        b=random(0,256)
        fill(r,g,b)
        triangle(0,0,x1V,0,0,y1V)
        triangle(0,600,x1V,600,0,y2V)
        triangle(600,0,x2V,0,600,y1V)
        triangle(600,600,x2V,600,600,y2V)
        x1V+=10
        y1V+=10
        x2V-=10
        y2V-=10
        if(x1V>300):
            x1V=0
            x2V=600
            y1V=0
            y2V=600
            background(0)
            flagV=0
    
flagW=0
x1W=300
y1W=300
x2W=300
y2W=300
flag1W=0
def W():
    global x1W,x2W,y1W,y2W,flagW,flag1W
    if(flagW==1):
      background(0)
      fill(123,124,145)
      arc(x1W,y1W, 200, 200, QUARTER_PI, PI+QUARTER_PI)
      arc(x2W,y2W, 200, 200, PI+QUARTER_PI, PI+PI+QUARTER_PI)  
      x1W-=10
      x2W+=10
      y1W+=10
      y2W-=10
      if(x1W<250):
          x1W=300
          x2W=300
          y1W=300
          y2W=300
          flagW=0
          flag1W=0
          background(0)
          
    
flagX=0
x1X=300
y1X=300
x2X=300
y2X=300
x3X=300
y3X=300
x4X=300
y4X=300
def X():
    global flagX,x1X,y1X,x2X,y2X,x3X,y3X,x4X,y4X
    if(flagX==1):
        background(0)
        fill(213,125,11)
#        arc(x1X,y1X,200,200,PI,PI+HALF_PI)
        arc(x2X,y2X,200,200,PI+HALF_PI,PI+PI)
#        arc(x3X,y3X,200,200,0,HALF_PI)
        arc(x4X,y4X,200,200,HALF_PI,PI)
        
    
    
flagY=0
def Y():
    if(flagY==1):
        pass
    
flagZ=0
def Z():
    if(flagZ==1):
        pass
