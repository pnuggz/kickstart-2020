def solve(t_case):
  k = int(input())
  k_arr = [int(v) for v in input().split(" ")]

  up = 0
  down = 0
  res = 0

  for i in range(1, len(k_arr)):
    if k_arr[i] > k_arr[i - 1]:
      up += 1
      down = 0
    else:
      down += 1
      up = 0

    if up > 3 or down > 3:
      res += 1
      up = down = 0

  print("Case #{}: {}".format(t_case, res))



def main():
  t = int(input())
  
  for t_case in range(t):
    solve(t_case + 1)


if __name__ == "__main__":
  main()