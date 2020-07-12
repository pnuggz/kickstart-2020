

def solve(t_case):
  n = int(input())
  v_arr = [int(i) for i in input().split(" ")]

  res = 0
  prev = 0
  k = -1
  for v in v_arr:
    k += 1
    v_arr_k = v_arr[0:k]

    if len(v_arr_k) == 0:
      v_arr_k = [0]

    if v <= max(v_arr_k):
      continue

    if k+1 < len(v_arr):
      if v <= v_arr[k+1]:
        continue
    res += 1

  print("Case #{}: {}".format(t_case, res))



def main():
  t = int(input())
  
  for t_case in range(t):
    solve(t_case + 1)


if __name__ == "__main__":
  main()