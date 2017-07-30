from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	start_color()
	noecho() #no echoing symbols
	curs_set(False) # hide cursor
	keypad(stdscr, True) #enable arrows
	
	window = newwin(10,25,3,3)
	
	
	box(window)
	wmove(window, 4,4)
	waddstr(window, 'HEYYYYY')
	
	r = True
	while r:
		key = wgetch(window)
		if key == 27:
			r = False
			break
			
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()