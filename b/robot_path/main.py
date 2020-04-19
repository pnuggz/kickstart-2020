# ALWAYS NECESSARY
t = 0 # number of cases
t_i = 0 # case number

# GLOBAL ARRAY BASED ON THE CASE
grid = [10**9,10**9] # grid [w,h] columns
instructions = []

# WORKING VARIABLES


def read_file():
	# DEFINE GLOBALS HERE
	global instructions
	instructions = []

	# READ THE LINES FOR EACH CASE
	line_1 = input()
	line_w = ''
	for i,char in enumerate(line_1):
		if(char.isdigit()):
			line_w = line_w + char
			continue
		if(char == '(' or char == ')'):
			line_w = line_w + char
			continue
		if i == 0:
			line_w = str(1) + char
		else:
			if(line_1[i-1].isdigit() == False):
				line_w = line_w + str(1) + char
			else:
				line_w = line_w + char

	line_1 = line_w

	# SPLIT LINES BY SPACE IF REQUIRED


	# ASSIGN THE VARIABLE TO THE GLOBAL
	mults = []
	num = ''
	for i,char in enumerate(line_1):
		if(char.isdigit()):
			num = num + str(char)

			if(line_1[i+1].isdigit()):
				continue
			else:
				mults.append(int(num))
				num = ''
				continue

		if(char == '('):
			continue

		if(char == ')'):
			mults = mults[0:len(mults)-1]
			continue

		curr_mult = 1
		for m in mults:
			curr_mult = curr_mult * m

		instructions.append((curr_mult,char))
		mults = mults[0:len(mults)-1]

def move(tup, pos):
	v = tup[1]

	if v == 'N':
		pos = [pos[0], pos[1] - int(tup[0])]
	if v == 'S':
		pos = [pos[0], pos[1] + int(tup[0])]
	if v == 'E':
		pos = [pos[0] + int(tup[0]), pos[1]]
	if v == 'W':
		pos = [pos[0] - int(tup[0]), pos[1]]

	if pos[0] > grid[0]:
		pos[0] = abs(grid[0] - abs(pos[0]))
	if pos[0] <= 0:
		pos[0] = abs(grid[0] - abs(pos[0]))

	if pos[1] > grid[1]:
		pos[1] = abs(grid[1] - abs(pos[1]))
	if pos[1] <= 0:
		pos[1] = abs(grid[1] - abs(pos[1]))

	return pos
		

def calculate():
	# DEFINE GLOBALS HERE
	global t_i
	global instructions
	#DO CALCULATION HERE
	run_pos = [1,1]
	for i,tup in enumerate(instructions):
		run_pos = move(tup,run_pos)

	# CHANGE THE ... TO THE ANSWER VARIABLE
	print('Case #{}: {} {}'.format(t_i, run_pos[0], run_pos[1]))


def main():
	global t
	global t_i
	
	t = int(input())

	for i in range(t):
		t_i = i+1
		read_file()
		calculate()


if __name__ == '__main__':
	main()