
from solution import solve
import pygame
import time
pygame.font.init()


class game():
    clr_white = (255, 255, 255)  # white
    clr_offwhite = (200, 200, 200)
    clr_black = (0, 0, 0)
    clr_red = (255, 0, 0)
    clr_green= (0, 255, 0)
    clr_blue = (0, 0, 255)
    active_box = []
    #content = [[0 for i in range(9)] for j in range(9)] #9x9 array matrix
    content = [
        [0, 5, 2, 0, 0, 6, 0, 0, 0],
        [1, 6, 0, 9, 0, 0, 0, 0, 4],
        [0, 4, 9, 8, 0, 3, 6, 2, 0],

        [4, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 8, 3, 2, 0, 1, 5, 9, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2],

        [0, 9, 7, 3, 0, 5, 2, 4, 0],
        [2, 0, 0, 0, 0, 9, 0, 5, 6],
        [0, 0, 0, 1, 0, 0, 9, 7, 0]]


    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height

        self.start = 0
        self.top = height/10
        self.end = width
        self.num_gap = height/10
        self.box_gap = 3* self.num_gap

    def background(self):
        self.win.fill(self.clr_offwhite)
        #Draw Lines
        for i in range(4):  #BoxLines
            #Horizontal
            pygame.draw.line(self.win, self.clr_black, [ self.start, self.top + i* self.box_gap],[ self.end,  self.top + i* self.box_gap], 3)
            #Vertical
            pygame.draw.line(self.win, self.clr_black, [ self.start + i *  self.box_gap,  self.top], [ self.start + i *  self.box_gap,  self.top +  self.end], 3)
        for i in range(9):  #NumberLines
            pygame.draw.line(self.win, self.clr_black, [ self.start, self.top + i* self.num_gap],[ self.end,  self.top + i* self.num_gap], 1)
            pygame.draw.line(self.win, self.clr_black, [ self.start + i *  self.num_gap,  self.top], [ self.start + i *  self.num_gap,  self.top +  self.end], 1)


    def write_number(self,num_in):
        fnt = pygame.font.SysFont("Calibri",40)
        text = fnt.render(str(num_in),True,self.clr_blue)

        text_rect = text.get_rect()
        text_rect.center = [self.active_box[0] + self.num_gap/2,
                            self.active_box[1] + self.num_gap/2]
        self.win.blit(text, text_rect)
        #self.win.blit(text, self.active_box)

    def move_active(self, mouse_pos = [], x = [] , y = []):
        if len(mouse_pos) != 0:
            area = [mouse_pos[0] // 100 * 100, mouse_pos[1] // 100 * 100]
        else:
            area = [self.active_box[0] + self.num_gap * x,
                    self.active_box[1] - self.num_gap * y]
            if not (0 <= area[0] <= self.width - self.num_gap) or not (self.top <= area[1] <= self.height - self.num_gap):
                return
        self.active_box = area

    def highlight(self):
        if len(self.active_box) == 0:
            return
        box_attributes = pygame.Rect(self.active_box[0],self.active_box[1], self.top, self.top)
        pygame.draw.rect(self.win, self.clr_red, box_attributes,3)

    def save_number(self,num):
        row = int((self.active_box[1]- 100)//100)
        column = int(self.active_box[0]//100)
        self.content[row][column] = num

    def draw_all_numbers(self):
        temp = self.active_box
        self.active_box = [self.start,self.top]
        for i in self.content:
            for j in i:
                if j != 0:
                    self.write_number(j)
                self.move_active(x = 1, y = 0)
            self.move_active(x = -8, y = 0)
            self.move_active(x = 0, y = -1)
        self.active_box = temp

    def redraw(self):
        self.background()
        self.draw_all_numbers()
        self.highlight()


def main():
    height = 1000
    width = 900
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption("JHV SUDOKU")

    sudoku = game(win, width, height)
    sudoku.background()

    running = True
    while running:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                sudoku.move_active(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sudoku.move_active(x = -1, y = 0)
                    sudoku.highlight()
                if event.key == pygame.K_RIGHT:
                    sudoku.move_active(x = 1, y = 0)
                    sudoku.highlight()
                if event.key == pygame.K_UP:
                    sudoku.move_active(x = 0, y = 1)
                    sudoku.highlight()
                if event.key == pygame.K_DOWN:
                    sudoku.move_active(x = 0, y = -1)
                    sudoku.highlight()

                if event.key == pygame.K_KP_9:
                    sudoku.save_number(9)
                if event.key == pygame.K_KP_8:
                    sudoku.save_number(8)
                if event.key == pygame.K_KP_7:
                    sudoku.save_number(7)
                if event.key == pygame.K_KP_6:
                    sudoku.save_number(6)
                if event.key == pygame.K_KP_5:
                    sudoku.save_number(5)
                if event.key == pygame.K_KP_4:
                    sudoku.save_number(4)
                if event.key == pygame.K_KP_3:
                    sudoku.save_number(3)
                if event.key == pygame.K_KP_2:
                    sudoku.save_number(2)
                if event.key == pygame.K_KP_1:
                    sudoku.save_number(1)
                if event.key == pygame.K_DELETE :
                    sudoku.save_number(0)
                if event.key == pygame.K_SPACE:
                    print("SOLVE")
                    abc = solve()
                    sudoku.content = abc.backpropagation(sudoku.content)

                if event.key == pygame.K_KP_ENTER:
                    print(sudoku.content)

                if event.key == pygame.K_ESCAPE:
                    running = False
            sudoku.redraw()
        pygame.display.update()
    print("END")

main()