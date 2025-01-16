import pygame,sys



class Button:

    def __init__(self,text,pos:tuple(),width,height,color='#9699FC') -> None:

        self.rec= pygame.Rect(pos,(width,height))
        self.color=color

        font=pygame.font.Font(None,32)
        self.txt= font.render(text,True,(20,32,245))
        self.txt_rec=self.txt.get_rect(center=self.rec.center)

    
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rec,width=0,border_radius=3)
        window.blit(self.txt,self.txt_rec)




def draw_grid(a:list(),screen):

    main_board = pygame.Surface((600,600))
    main_board_rect=main_board.get_rect(topleft=[10,30])
    main_board.fill('#CCFFFF')

    
 
    y0=5
    for i in range(9):
        x0=5
        for j in range(9):
            
            if a[i][j] == 0:
                button=Button('',(x0,y0),60,60,'#FFFFFF')
                button.draw(main_board)
            else:
                 button=Button(str(a[i][j]),(x0,y0),60,60)
                 button.draw(main_board)
            
            if (j+1) % 3==0 and j != 8 :
                pygame.draw.line(main_board,'#4F846B',(x0+62,0),(x0+62,600),2)
           
            screen.blit(main_board,main_board_rect)
            x0 += 66
        if (i+1)%3 ==0:
                pygame.draw.line(main_board,'#4F846B',(0,y0+61),(600,y0+61),2)  
        y0 += 66

