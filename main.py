# Made by Saba Kharebava (J222J on Github)
#                                         ▓▓▓▓████████████████▒▒▒▒                                                                                    
#                             ████████████▓▓▓▓####        ####████████████                                                                            
#                     ░░░░████████                                        ████████                                                                    
#                 ████████                                                                                                                            
#             ████████                                                            ####                                                                
#             ████                                                                    ▓▓▓▓                                                            
#         ████            ████                                            ▒▒▒▒            ████                                                        
#     ▒▒▒▒▒▒▒▒            ████                    ▓▓▓▓                                    ████                                                        
#     ████                ▓▓▓▓░░░░                ████████            ▒▒▒▒####                ████                                                    
#     ████                    ########        ████    ████            ####▓▓▓▓                ████                                                    
# ▒▒▒▒░░░░                ####    ####                ▓▓▓▓████            ▒▒▒▒                ████░░░░                                                
# ████                    ▒▒▒▒    ####    ####            ████            ░░░░                ▒▒▒▒████                                                
# ████                    ▒▒▒▒    ####████                ▒▒▒▒            ░░░░                ####████                                                
# ████                    ####        ░░░░                    ████        ####                ####████                                                
# ▒▒▒▒####                ░░░░    ████▓▓▓▓░░░░                ####▒▒▒▒▓▓▓▓▓▓▓▓                ▒▒▒▒▒▒▒▒                                                
#     ████                ▒▒▒▒▓▓▓▓▒▒▒▒████████████████####████                                ████                                                    
#     ████                ▒▒▒▒▓▓▓▓        ████            ####        ▓▓▓▓                    ████                                                    
#     ▒▒▒▒░░░░                            ████████    ▒▒▒▒                                ████####                                                    
#         ████                                ████    ████                                ████                                                        
#             ████                            ████████                                ▒▒▒▒                                                            
#             ████░░░░                            ████                            ░░░░░░░░                                                            
#                 ████░░░░                                                    ####░░░░                                                                
#                     ▓▓▓▓░░░░                                            ░░░░
#                             ████░░░░                            ####
#
# To run the code you must use the following command
#
# python3 main.py -ow (width of the output) -oh (height of the output)
#

import random
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-oh', '--height', help = 'Height of the output')
parser.add_argument('-ow', '--width', help = 'Width of the output')
args = parser.parse_args()

maze = []

ix = 0
iy = 0

def generate_base(width, height):
	global maze, ix, iy
	ix = width-1
	iy = 0
	maze = []
	maze1 = []
	for i in range(width-1):
		maze1.append(3)
	maze1.append(0)
	maze.append(maze1)
	for i in range(height-1):
		newmaze = []
		newmaze.append(2)
		for i in range(width-1):
			newmaze.append(1)
		maze.append(newmaze)

def display_maze():
	global maze
	print('A', end = '')
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			up = False
			if (i > 0 and maze[i-1][j] == 4) or maze[i][j] == 2:
				up = True
			down = False
			if (i < len(maze)-1 and maze[i+1][j] == 2) or maze[i][j] == 4:
				down = True
			left = False
			if (j > 0 and maze[i][j-1] == 3) or maze[i][j] == 1:
				left = True
			right = False

			if i == 0 and j == 0:
				left = True
			elif i == len(maze)-1 and j == len(maze[i])-1:
				right = True

			if (j < len(maze[i])-1 and maze[i][j+1] == 1) or maze[i][j] == 3:
				right = True
			if up and left and down and not right:
				print('╣', end = '')
			elif up and down and not left and not right:
				print('║', end = '')
			elif up and not down and not left and not right:
				print('║', end = '')
			elif down and not up and not left and not right:
				print('║', end = '')
			elif left and down and not up and not right:
				print('╗', end = '')
			elif left and up and not down and not right:
				print('╝', end = '')
			elif up and right and not left and not down:
				print('╚', end = '')
			elif right and down and not left and not up:
				print('╔', end = '')
			elif left and up and right and not down:
				print('╩', end = '')
			elif left and down and right and not up:
				print('╦', end = '')
			elif up and right and down and not left:
				print('╠', end = '')
			elif left and right and not up and not down:
				print('═', end = '')
			elif left and not right and not up and not down:
				print('═', end = '')
			elif right and not left and not up and not down:
				print('═', end = '')
			elif left and up and right and down:
				print('╬', end = '')
		if i < len(maze)-1:
			print(end = '\n ')
		else:
			print('B')

generate_base(int(args.width), int(args.height))

for i in range(250000):
	directions = []
	if ix > 0:
		directions.append(1)
	if ix < len(maze[iy])-1:
		directions.append(3)
	if iy > 0:
		directions.append(2)
	if iy < len(maze)-1:
		directions.append(4)

	dir = random.choice(directions)
	maze[iy][ix] = dir

	if dir == 1:
		ix -= 1
	if dir == 2:
		iy -= 1
	if dir == 3:
		ix += 1
	if dir == 4:
		iy += 1

	maze[iy][ix] = 0

display_maze()