from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	start_color()
	noecho() #no echoing symbols
	curs_set(False) # hide cursor
	keypad(stdscr, True) #enable arrows
	
	window = newwin(3,20,4,4)
	box(window)
	wmove(window, 1,1)
	waddstr(window, 'HEYYYYY')
	panel = new_panel(window)
	update_panels()
	doupdate()
	r = True
	while r:
		key = getch()
		if key == 27:
			r = False
			break
			
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()