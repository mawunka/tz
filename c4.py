from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	max_y,max_x = getmaxyx(stdscr)
	move(int(max_y/2),int(max_x/2)) #move to center of screen
	addstr('center')
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()