t = 0
t_i = 0
n = 0
k = 0
words = []


def getKey(item):
	return item[1]


def read_input():
	global n
	global k
	global words

	k = 0
	n = 0
	words_uo = []
	words = []
	
	line_1 = input().split(' ')
	n = int(line_1[0])
	k = int(line_1[1])

	for i in range(n):
		words_uo.append([char for char in input()])

	len_index = [(i,len(val)) for i,val in enumerate(words_uo)]
	len_index = sorted(len_index, key=getKey)
	
	words = [words_uo[val[0]] for val in len_index]
	print(words)


def main():
	global t
	global t_i

	t = int(input())

	for i in range(t):
		t_i = i+1
		read_input()


if __name__ == '__main__':
	main()
