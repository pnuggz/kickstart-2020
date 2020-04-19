# ALWAYS NECESSARY
t = 0 # number of cases
t_i = 0 # case number

# GLOBAL ARRAY BASED ON THE CASE
n = 0 # number of bus routes
x = [] # day it runs
d = 0 # number of days she must finish

# WORKING VARIABLES


def read_file():
	# DEFINE GLOBALS HERE
	global n
	global d
	global x

	# READ THE LINES FOR EACH CASE
	line_1 = input()
	line_2 = input()

	# SPLIT LINES BY SPACE IF REQUIRED
	line_1_arr = line_1.split(' ')
	line_2_arr = line_2.split(' ')

	# ASSIGN THE VARIABLE TO THE GLOBAL
	n = int(line_1_arr[0])
	d = int(line_1_arr[1])
	x = [int(v) for i,v in enumerate(line_2_arr)]


def calculate():
	# DEFINE GLOBALS HERE
	global t_i
	global n
	global d
	global x
	x_r = x
	x_r.reverse()

	current_day = d
	#DO CALCULATION HERE
	for i in range(len(x)):
		val = x_r[i]

		for j in range(d,-1,-1):
			if j % val == 0:
				current_day = j
				break
		
		d = current_day

	# CHANGE THE ... TO THE ANSWER VARIABLE
	print('Case #{}: {}'.format(t_i, current_day))


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