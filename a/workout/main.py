import math

t = 0 # number of cases
t_i = 0 # current case number
n = 0 # number of sessions
m = [] # array of minutes for the ith session
k = 0 # additional classes
m_diff = []


def read_input():
	global n
	global m
	global k
	global m_diff
	
	n = 0
	m = 0
	k = 0
	m = []
	m_diff = []

	line_1 = input().split(' ')
	n = int(line_1[0])
	k = int(line_1[1])
	line_2 = input().split(' ')
	m = [int(v) for v in line_2]
	
	for i,v in enumerate(m):
		if i == 0:
			continue
		m_diff.append(m[i] - m[i-1])


def solve():
	global k
	global m_diff
	global m

	for i in range(k):
		max_val = 0
		max_val_index = 0

		for index,val in enumerate(m_diff):
			if val > max_val:
				max_val = val
				max_val_index = index

		new_val = math.floor(max_val//2)
		m.insert(max_val_index + 1, m[max_val_index] + new_val)
		m_diff = []

		for i,v in enumerate(m):
			if i == 0:
				continue
			m_diff.append(m[i] - m[i-1])
	
	print('Case #{}: {}'.format(t_i, max(m_diff)))


def main():
	global t
	global t_i

	t = int(input())
	
	for i in range(t):
		t_i = i+1
		read_input()
		solve()

if __name__ == '__main__':
	main()
