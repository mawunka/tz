from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	c = getch()
	addstr(str(c))
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()