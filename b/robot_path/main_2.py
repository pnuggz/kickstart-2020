# ALWAYS NECESSARY
t = 0 # number of cases
t_i = 0 # case number

# GLOBAL ARRAY BASED ON THE CASE
grid = [10**9, 10**9] # grid [w,h] columns
instructions = []


def read_file():
	# DEFINE GLOBALS HERE
	global instructions
	instructions = []
	
	line_1 = input()
	line_w = ''
	for i,char in enumerate(line_1):
		if(char.isdigit()):
			line_w = line_w + char
			continue
		if(char == '(' or char == ')'):
			line_w = line_w + char
			continue
			
		if((i>0 and line_w[len(line_w)-1].isdigit() == False) or (i==0 and char.isdigit() == False)):
			line_w = line_w + str(1) + char
		else:
			line_w = line_w + char
	
	line_1 = line_w
	print(line_1)


def main():
	global t
	global t_i

	t = int(input())

	for i in range(t):
		t_i = i+1
		read_file()


if __name__ == '__main__':
	main()
