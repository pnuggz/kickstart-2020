import itertools

t = 0 # number of cases
t_i = 0 # case number
n = 0 # number of houses
a = [] # house prices array
b = 0 # budget

max_sum = 0
max_arr = []
max_arr_len = 0

def read_file():
	global n
	global a
	global b

	line_1 = input()
	line_2 = input()

	line_1_arr = line_1.split(' ')
	n = int(line_1_arr[0])
	b = int(line_1_arr[1])
	a = line_2.split(' ')
	a = [int(price) for price in a if int(price) <= b]
	a.sort()


def calculate():
	global t_i
	global n
	global a
	global b
	global max_sum
	global max_arr
	global max_arr_len

	counter = 0
	total = 0
	
	for price in a:
		if price + total > b:
			break
		else:
			total += price
			counter += 1

	print('Case #{}: {}'.format(t_i, counter))

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

