import curses
import time
import random
stdscr = curses.initscr()

curses.curs_set(0)
sh, sw =  stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(1)
y = sh//4
x = sw//2

target = [sh//2, sw//2]
w.addch(target[0], target[1], 'O')

snake = [
	[y, x],
	[y, x-1],
	[y, x-2],
]
key = curses.KEY_RIGHT
while True:
	next_key = w.getch()
	if next_key==-1:
		key = key
	else:
		if next_key in allowed_keys:
			key = next_key
		else:
			key = key

	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_RIGHT:
		new_head[1] +=1
		allowed_keys = [curses.KEY_UP,curses.KEY_DOWN]
	if key == curses.KEY_LEFT:
		new_head[1] -=1
		allowed_keys = [curses.KEY_UP,curses.KEY_DOWN]
	if key == curses.KEY_UP:
		new_head[0] -=1
		allowed_keys = [curses.KEY_RIGHT,curses.KEY_LEFT]
	if key == curses.KEY_DOWN:
		new_head[0] +=1
		allowed_keys = [curses.KEY_RIGHT,curses.KEY_LEFT]
	if key == curses.KEY_NPAGE:
		break
	
	snake.insert(0, new_head)

	if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	if new_head == target:
		target = None
		nf = []
		while target is None:
			nf = [random.randint(0, sh-1), random.randint(0, sw-1)]

			target = nf if nf not in snake else None
		w.addch(target[0], target[1], 'O')
	else:
		k = snake.pop()
		w.addch(k[0], k[1], ' ')
	
	w.addch(snake[0][0], snake[0][1], '0')

w.keypad(0)
curses.curs_set(1)