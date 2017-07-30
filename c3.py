from unicurses import *
def main():
	
	stdscr = initscr() #init sccreen
	r = True
	while r:
		key = getch()
		if key == 27: #break when ESC pressed
			r = False
			break
		elif chr(key) == 'a':
			move(2,0)
			addstr('Ty nazhal A !!!')
			continue
		move(50,50)
		addstr('Keycode was '+ str(key) + ' key was '+ chr(key)) # display keycode+key using getch()
		move(0,0)
	endwin()
	return 0;
	
if __name__ == '__main__':
	main()