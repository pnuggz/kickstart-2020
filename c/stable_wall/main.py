from itertools import permutations

t_i = 0


def solve():
	global t_i
	
	chars = []
	arr = []

	line_1 = input().split(' ')
	for i in range(int(line_1[0])):
		poly = input()
		arr.append([char for i,char in enumerate(poly)])
		
		for char in poly:
			if char not in chars:
				chars.append(char)
	
	match = []
	for p in permutations(chars):
		laid = []
		for i,char in enumerate(p):
			laid.append(char)
			for j in range(len(arr)):
				if arr[j][i] not in laid:
					laid = []
					break

			match = laid

	if len(match) == 0:
		print("Case {}: None".format(t_i))
	else:
		ans = [match[i] for i in range(len(match)-1,-1,-1)]
		ans = ''.join(ans)
		print("Case {}: {}".format(t_i, ans))
	


def main():
	global t_i

	t = int(input())

	for i in range(t):
		t_i = i+1
		solve()


if __name__ == "__main__":
	main()
