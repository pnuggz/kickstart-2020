t_i = 0

N = 0
A = []
K = 0


def solve():
	global A
	global K
	global t_i

	answer_counter = 0
	current_counter = 9
	for i in range(len(A)):
		if A[i] == K or i + K - 1 < len(A):
			current_counter = 1
			for j in range(K, 0, -1):
				if A[i+K-j] != j:
					current_counter = 0
			answer_counter += current_counter
	
	print("Case {}: {}".format(t_i, answer_counter))
	return True


def read_file():
	global A
	global K

	line_1 = input().split(' ')
	line_2 = input().split(' ')
	N = int(line_1[0])
	K = int(line_1[1])
	A = [int(num) for num in line_2]
	return True


def main():
	global t_i

	t = int(input())

	for i in range(t):
		t_i = i+1
		read_file()
		solve()


if __name__ == '__main__':
	main()
