from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	start_color() #init colored text
	use_default_colors()
	init_pair(1, COLOR_BLUE, COLOR_BLACK) #color of text
	
	addstr('HELLO !', color_pair(1) + A_BOLD) #add colorised text
	addstr('HELLO !', color_pair(1))
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()