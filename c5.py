from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	attron(A_BOLD) #enable attribute
	addstr('center \n')
	attroff(A_BOLD) #disable attribute
	addstr('center \n')
	attron(A_REVERSE) #enable attribute
	addstr('center \n')
	attroff(A_REVERSE) #disable attribute
	addstr('center \n', A_BOLD) #!!! attr in addstr()
	addstr('center \n', A_UNDERLINE) #!!! attr in addstr()
	addstr('center \n', A_UNDERLINE)
	getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()