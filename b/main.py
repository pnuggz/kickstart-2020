# ALWAYS NECESSARY
t = 0 # number of cases
t_i = 0 # case number

# GLOBAL ARRAY BASED ON THE CASE
n = 0 # number of houses
a = [] # house prices array
b = 0 # budget

# WORKING VARIABLES


def read_file():
	# DEFINE GLOBALS HERE

	# READ THE LINES FOR EACH CASE
	line_1 = input()
	line_2 = input()

	# SPLIT LINES BY SPACE IF REQUIRED
	line_1_arr = line_1.split(' ')
	line_2_arr = line_2.split(' ')

	# ASSIGN THE VARIABLE TO THE GLOBAL


def calculate():
	# DEFINE GLOBALS HERE
	global t_i

	#DO CALCULATION HERE

	# CHANGE THE ... TO THE ANSWER VARIABLE
	print('Case #{}: {}'.format(t_i, ...))


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