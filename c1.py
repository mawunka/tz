from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	#move(12,12) #cursor state
	#addstr('HELLO WORLD!')
	#mvaddstr(20,30,'HELLO WORLD!')
	#getch()
	for i in range(0,50):
		mvaddstr(10,i,'ASDASDASD! !!')
		getch()
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()