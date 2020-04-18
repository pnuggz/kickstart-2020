t = 0 # cases
t_i = 0 # case number - not index
n = 0 # stacks of plates
k = 0 # plates per stacks
p = 0 # number of plates required
n_arr = [] # plates array
n_arr_og = []


def read_input():
	global n
	global k
	global p
	global n_arr
	global n_arr_og

	n_arr = []
	n_arr_og = []
	
	line_1_arr = input().split(' ')
	n = int(line_1_arr[0])
	k = int(line_1_arr[1])
	p = int(line_1_arr[2])

	for i in range(n):
		arr = input().split(' ')
		arr = [int(num) for j,num in enumerate(arr) if j < p]
		n_arr.append(arr)
		n_arr_og.append(arr)


def solve():
	global t_i
	global n_arr
	global n_arr_og
	global p

	counter = 0
	beauty = 0
	
	for i in range(1000000):
		if counter == p:
			break

		stack_index = 0
		stack_sum = 0
		for s,stack in enumerate(n_arr):
			if sum(stack) > stack_sum:
				stack_sum = sum(stack)
				stack_index = s

		for s,stack in enumerate(n_arr_og):
			if s == stack_index:
				beauty += stack[0]
				n_arr_og[s] = stack[1::]
				n_arr[s] = stack[1::]
			else:
				n_arr[s] = [n_sub_arr for i,n_sub_arr in enumerate(n_arr[s]) if i < p-counter-1]

		
		n_arr_og = [stack for stack in n_arr_og if len(stack) > 0]
		n_arr = [stack for stack in n_arr if len(stack) > 0]

		counter += 1

	print('Case #{}: {}'.format(t_i,beauty))


def main():
	global t_i

	t = int(input())

	for i in range(t):
		t_i = i+1
		read_input()
		solve()


if __name__ == '__main__':
	main()
