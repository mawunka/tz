import unicurses as curses
import time
import os
from random import randint, choice


os.environ['ESCDELAY'] = '25'
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.keypad(stdscr, 1)
curses.wborder(stdscr)
curses.curs_set(0)
middley, middlex = map(lambda x: x//2, curses.getmaxyx(stdscr)) # get middle coordinates depending on the size of the terminal


UP = 259    # ascii key codes
DOWN = 258
LEFT = 261
RIGHT = 260



asci ='''
   _____ _   _          _  ________ 
  / ____| \ | |   /\   | |/ /  ____|
 | (___ |  \| |  /  \  | ' /| |__   
  \___ \| . ` | / /\ \ |  < |  __|  
  ____) | |\  |/ ____ \| . \| |____ 
 |_____/|_| \_/_/    \_\_|\_\______|'''


def reset_game():
    
    '''
    >>> reset_game()
    False
    '''

    curses.clear()
    curses.refresh()
    return False    

def get_key(current_direction):

    # utility function to control snake with users input
    # doctest for main functions
    #'''
    #>>> get_key(DOWN)
    #258
    #>>> get_key(UP)
    #259
    #>>> get_key(LEFT)
    #261
    #>>> get_key(RIGHT)
    #260
    #>>> get_key(27)
    #27
    #'''
    KEY = curses.getch()    
    if KEY == UP:
        if current_direction == DOWN:
            return DOWN
        else:
            return UP
    elif KEY == DOWN:
        if current_direction == UP:
            return UP
        else:
            return DOWN        
    elif KEY == RIGHT:
        if current_direction == LEFT:
            return LEFT
        else:
            return RIGHT
    elif KEY == LEFT:
        if current_direction == RIGHT:
            return RIGHT
        else:
            return LEFT
    elif KEY == 27:
        return 27
    else:
        return current_direction


   
   
class Menu:
    
    def speed_menu(self):

        # draws the speed menu
        
        
        curses.mvwaddstr(stdscr, 8, middlex-7, 'Choose speed')
        curses.mvwaddstr(stdscr, 9, middlex-7, '<---------->')
        curses.wborder(stdscr)
        curses.refresh
    
    def draw_snake(self):
        

        # draws the snake ascii art
        
        
        for y, line in enumerate(asci.splitlines()):
            curses.mvwaddstr(stdscr, y, middlex-20, line)
        curses.wborder(stdscr)
        curses.refresh()
        
    def main_menu(self):

        # draws the main menu

        curses.wborder(stdscr)
        curses.mvwaddstr(stdscr, 8, middlex-5, 'New Game')
        curses.mvwaddstr(stdscr, 9, middlex-5 ,'Set Speed')
        curses.mvwaddstr(stdscr, 10, middlex-5 ,'Quit')
        curses.refresh()        
    
    def main_cursor(self, location):

        # draws the cursor in main menu
        
        curses.mvwaddstr(stdscr, 8, middlex-7, ' ')
        curses.mvwaddstr(stdscr, 9, middlex-7, ' ')
        curses.mvwaddstr(stdscr, 10, middlex-7, ' ')
        
        if location == 0:
            curses.mvwaddstr(stdscr, 8, middlex-7, '#')
        elif location == 1:
            curses.mvwaddstr(stdscr, 9, middlex-7, '#')
        else:
            curses.mvwaddstr(stdscr, 10, middlex-7, '#')
        curses.refresh()
        
    def speed_cursor(self, location):

        # draws the cursor in speed menu
        
        for i in range(10):
            curses.mvwaddstr(stdscr, 9, middlex-i+3, '-')
        curses.mvwaddstr(stdscr, 9, middlex-7+location, '#')
        curses.refresh()
    


class Snake:

    def __init__(self):
        self.y = 20
        self.x = 20
        self.lenght = 3
        self.count = 0
        self.reg = {} 
        self.sy, self.sx = curses.getmaxyx(stdscr)
        self.starting_lenght = self.lenght 
        
    def food(self):

        #return location of a new food and grow the snake by one
        
        while True:
            self.dot = (randint(2,self.sy-2),  randint(2, self.sx-2))
            if self.dot not in self.reg.values():
                break
        self.lenght+=1
        return self.dot
    
    def get_status(self):
         
        if self.y == self.sy-1 or self.y == 0:
            return 'dead'
        elif self.x == self.sx-1 or self.x == 0:
            return 'dead'
        elif len([i for i in self.reg.values() if i == (self.y, self.x)]) == 2:
            return 'dead'
        elif (self.y, self.x) == self.dot:       
            return 'grow'
        else:
            return False
        
    def draw(self, direction):
        
        # draw the pixel
        
        curses.mvwaddstr(stdscr, *self.dot, 'o')           
        if direction == UP:
            self.y -= 1
        if direction == DOWN:
            self.y += 1
        if direction == RIGHT:
            self.x -= 1
        if direction == LEFT:
            self.x += 1
            
        curses.mvwaddstr(stdscr, self.y ,self.x, '#')
        curses.refresh()        
        self.reg[self.count] = (self.y,self.x)   # a register of previous coords
        self.count +=1                           
        
    def delete(self, lenght):

        # delete the pixel from snake's tail
        
        try:
            curses.mvwaddstr(stdscr, *self.reg[self.count-self.lenght], ' ')
            del self.reg[self.count-self.lenght]
        except KeyError:
            pass


def speed_menu():

    # main loop for speed menu

    global SPEED    
    
    while True:
        reset_game()
        menu.draw_snake()
        menu.speed_menu()
        menu.speed_cursor(SPEED)
        
        KEY = curses.getch()
        
        if KEY == 27 or KEY == 10 or KEY == 459:
            break
        
        if KEY == RIGHT and SPEED > 1:
            SPEED -=1
            menu.speed_menu()
            menu.speed_cursor(SPEED)
            
            
        if KEY == LEFT and SPEED < 10:
            SPEED +=1
            menu.speed_menu()
            menu.speed_cursor(SPEED)
            
        


def main_menu():

    # main loop for main menu

    global CURSOR
    
    while True:
        curses.nodelay(stdscr, False)
        menu.draw_snake()
        menu.main_menu()
        menu.main_cursor(CURSOR)
        KEY = curses.getch()
        
        if KEY == UP and CURSOR > 0:
            CURSOR-=1
        elif KEY == DOWN and CURSOR < 2:
            CURSOR+=1
        elif KEY == 27:
            reset_game()
            break
        
        elif KEY == 10 or KEY == 459:
            
            if CURSOR == 0:
                reset_game()
                curses.wborder(stdscr)                
                game(SPEED)
                
            elif CURSOR == 1:
                reset_game()
                speed_menu()
                reset_game()
                
            elif CURSOR == 2:
                reset_game()
                break
                
               

def game(speed):
    
    snake.food()
    
    # main loop for the game

    global KEY
    curses.nodelay(stdscr, True)
    
    while True:
        
        KEY = get_key(KEY)
        
        if snake.get_status() == 'dead' or KEY == 27:

            # game over
            
            
            curses.clear()
            curses.wborder(stdscr)
            curses.mvwaddstr(stdscr, middley-1, middlex-6, '--GAME OVER--')
            curses.mvwaddstr(stdscr, middley, middlex-8,'Your score is -')
            curses.mvwaddstr(stdscr, middley, middlex+8, snake.lenght - snake.starting_lenght-1)
            curses.mvwaddstr(stdscr, middley+1, middlex-8,'Press Esc to quit')
            
            KEY = choice([RIGHT, LEFT])
            snake.food()
            curses.refresh()
            curses.nodelay(stdscr, False)
            while get_key(KEY) != 27:
               pass 
            reset_game()
            snake.__init__()
            break
                
        
        if snake.get_status() == 'grow':

            # eaten food
            
            snake.food()
            

        
        snake.draw(KEY)
        snake.delete(snake.lenght)
        time.sleep(1/speed/2)        
    
if __name__ == "__main__":
   snake = Snake() 
   menu = Menu()
   KEY = choice([RIGHT, LEFT]) # choose random direction for snake to go at start
   CURSOR = 0
   SPEED = 5
   main_menu()