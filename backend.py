import pygame

import components as cmp
      
class sudoku:
    
    def __init__(self,a=[[0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     ]):
               
        self.a=a
        
        
    def check_possiblity (self,x,y,num):

    
    
        for column in range (9):
            if   self.a[x][column] == num:
             return False
        for row in range(9):
            if  self.a[row][y]== num:
             return False
    
        x0=(x//3)*3
        y0=(y//3)*3

        for i in range(3):
            for j in range(3):
                if self.a[x0+i][y0+j]==num:
                    return False

        return True

    def solve (self):
       
        for row in range (9):
         for column in range (9):
           
            if self.a[row][column] == 0:
                for num in range (1,10):
                    if self.check_possiblity(row,column,num) :
                        self.a[row][column]=num
                        update(self.a)
                        self.solve()
                        self.a[row][column]=0
                        update(self.a)
                   
                
                return
        input("Want more soluotion(if possible):")
       
        
     
    def update_data(self,num,x,y):
       self.a[x][y]=num

    def display (self):
        for i in range (len(self.a)):
         print(self.a[i]) 
        print('\n')



def update(a:list()): 
   global start
   start=True
   screen.fill((0,0,0))
   running=True
   while running: 
      screen.fill('#CCFFCC')  
      for event in pygame.event.get():
         if event.type==pygame.QUIT:
          running=False
          exit()

         if event.type==pygame.MOUSEBUTTONDOWN:
            if quit_button.rec.collidepoint(event.pos):
                exit()

         if event.type==pygame.MOUSEBUTTONDOWN:
            if start_button.rec.collidepoint(event.pos):
               start=False  
         if event.type==pygame.MOUSEBUTTONDOWN:
            if pause_button.rec.collidepoint(event.pos):
               pause=True
               while pause:
                  for event in pygame.event.get():
                     if event.type==pygame.MOUSEBUTTONDOWN:
                       if start_button.rec.collidepoint(event.pos):
                          pause=False
                   

      quit_button.draw(screen)
      pause_button.draw(screen)
      start_button.draw(screen)
      cmp.draw_grid(a,screen)
      pygame.time.delay(300)
      running=False
      clock.tick(60)
      pygame.display.update()
     




pygame.init()

screen= pygame.display.set_mode((700,700))
pygame.display.set_caption("sudoku")

clock=pygame.time.Clock()


done_button = cmp.Button("DONE",(500,650),100,30,"#000000")
generate_button = cmp.Button("GENERATE",(200,650),200,30,"#000000")
game1=sudoku()
input_screen_running=True
flag=False
done_button.draw(screen)
while input_screen_running:
   screen.fill('#CCFFCC')
   cmp.draw_grid(game1.a,screen)
   done_button.draw(screen)
   generate_button.draw(screen)  
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
           if generate_button.rec.collidepoint(event.pos):
              game1=sudoku([
                [7,8,0,4,0,0,1,2,0],
                [6,0,0,0,7,5,0,0,9],
                [0,0,0,6,0,1,0,7,8],
                [0,0,7,0,4,0,2,6,0],
                [0,0,1,0,5,0,9,3,0],
                [9,0,4,0,6,0,0,0,5],
                [0,7,0,2,0,0,0,1,2],
                [1,2,0,0,0,7,4,0,0],
                [0,4,9,2,0,6,0,5,7]
                ])
              input_screen_running=False

           if done_button.rec.collidepoint(event.pos):
             input_screen_running=False
           else:
            index=[]
            pos=pygame.mouse.get_pos()
            
            column=35
            for i in range(9): 
                row=15
                for j in range(9):
                 if row <= pos[0] <=row+60 and column <= pos[1] <= column+60:
                    
                    index.append(i)
                    index.append(j)
                    flag=True

                 row += 66

                column += 66     
            while flag:
                print(pos)
                print(index)
                user_input=''
                input_font= pygame.font.Font(None,32)
                y=index[0]*66+45
                x=index[1]*66+65
                user_rect=pygame.Rect((x-45,y-5),(50,50))
                pygame.draw.rect(screen,(0,0,0),user_rect,2)
                pygame.display.update()
       
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_BACKSPACE:
                            user_input=user_input[:-1]
                        else:
                            user_input=event.unicode
                            game1.update_data(int(user_input),index[0],index[1])
                            flag=False
                            print( game1.a[index[0]][index[1]])
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        flag=False
                    
                #user_text=input_font.render(user_input,True,(0,0,0))
                #screen.blit(user_text,user_rect.center)
               
   pygame.display.update()
      
      
      



game1.display()

quit_button=cmp.Button("QUIT",(50,650),100,30,'#3EDF59')
pause_button =cmp.Button("PAUSE",(200,650),100,30,'#3EDF59')
start_button = cmp.Button("START",(350,650),100,30,"#3EDF59")
update(game1.a)
while start:
    update(game1.a)

game1.solve()
