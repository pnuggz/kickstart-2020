# ALWAYS NECESSARY
t = 0 # number of cases
t_i = 0 # case number

# GLOBAL ARRAY BASED ON THE CASE
n = 0 # number of checkpoints
h = [] # height array


# WORKING VARIABLES


def read_file():
	# DEFINE GLOBALS HERE
	global n
	global h

	# READ THE LINES FOR EACH CASE
	line_1 = input()
	line_2 = input()

	# SPLIT LINES BY SPACE IF REQUIRED
	line_2_arr = line_2.split(' ')


	# ASSIGN THE VARIABLE TO THE GLOBAL
	n = int(line_1)
	h = [int(v) for i,v in enumerate(line_2_arr)]


def calculate():
	# DEFINE GLOBALS HERE
	global t_i
	global n
	global h

	peaks = 0
	#DO CALCULATION HERE
	for i in range(len(h)):
		if i == 0 or i+1 == len(h):
			continue
		
		val_i_p = h[i-1]
		val_i = h[i]
		val_i_n = h[i+1]

		if val_i > val_i_p and val_i > val_i_n:
			peaks += 1
		
	# CHANGE THE ... TO THE ANSWER VARIABLE
	print('Case #{}: {}'.format(t_i, peaks))


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